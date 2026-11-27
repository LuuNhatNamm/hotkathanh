"""Convert the official KITTI instance masks to a local YOLO segment dataset."""

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import cv2
import numpy as np


CLASSES = {
    24: "person",
    25: "rider",
    26: "car",
    27: "truck",
    28: "bus",
    32: "motorcycle",
    33: "bicycle",
}
SOURCE_TO_YOLO = {source_id: yolo_id for yolo_id, source_id in enumerate(CLASSES)}


def read_png(archive, member, mode):
    image = cv2.imdecode(np.frombuffer(archive.read(member), dtype=np.uint8), mode)
    if image is None:
        raise ValueError(f"Unreadable PNG: {member}")
    return image


def polygon_from_mask(binary):
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    parts = [contour[:, 0] for contour in contours if cv2.contourArea(contour) > 0]
    if not parts:
        return None
    polygon = parts[0]
    for part in parts[1:]:
        # Retrace the bridge so disconnected regions still yield one annotation.
        distances = ((polygon[:, None] - part[None, :]) ** 2).sum(axis=2)
        start, end = np.unravel_index(distances.argmin(), distances.shape)
        polygon = np.concatenate(
            (polygon[: start + 1], part[end:], part[: end + 1], polygon[start:])
        )
    return polygon


def convert_mask(instance_map):
    height, width = instance_map.shape
    rows, class_ids, overlaps = [], [], []
    skipped = 0
    for instance_id in np.unique(instance_map):
        # KITTI packs the semantic class byte above the per-class instance byte.
        source_class, object_id = divmod(int(instance_id), 256)
        class_id = SOURCE_TO_YOLO.get(source_class)
        if class_id is None or object_id == 0:
            continue
        binary = (instance_map == instance_id).astype(np.uint8)
        polygon = polygon_from_mask(binary)
        if polygon is None:
            skipped += 1
            continue
        raster = np.zeros_like(binary)
        cv2.fillPoly(raster, [polygon], 1)
        overlap = np.count_nonzero(binary & raster) / np.count_nonzero(binary | raster)
        points = (polygon / [width, height]).ravel()
        rows.append(f"{class_id} " + " ".join(f"{point:.7f}" for point in points))
        class_ids.append(class_id)
        overlaps.append(overlap)
    return rows, class_ids, overlaps, skipped


def split_frames(records):
    counts = np.array(
        [np.bincount(record[1], minlength=len(CLASSES)) for record in records]
    )
    present = counts > 0
    available = present.sum(axis=0)
    expected = available * 0.2
    rng = np.random.default_rng(243)
    best_score = float("inf")
    best_split = None
    for _ in range(2048):
        indices = rng.choice(len(records), size=40, replace=False)
        val_presence = present[indices].sum(axis=0)
        missing_in_split = (available > 1) & (
            (val_presence == 0) | (val_presence == available)
        )
        score = 100 * missing_in_split.sum()
        score += np.sum((val_presence - expected) ** 2 / np.maximum(expected, 1))
        if score < best_score:
            best_score, best_split = score, indices
    return set(best_split)


def prepare(archive_path, output):
    output.mkdir(parents=True, exist_ok=True)
    for split in ("train", "val"):
        for folder in ("images", "labels"):
            (output / folder / split).mkdir(parents=True, exist_ok=True)

    with ZipFile(archive_path) as archive:
        images = {}
        masks = {}
        for member in archive.namelist():
            if member.startswith("training/image_2/") and member.endswith(".png"):
                images[Path(member).stem] = member
            if member.startswith("training/instance/") and member.endswith(".png"):
                masks[Path(member).stem] = member
        if len(masks) != 200 or masks.keys() != images.keys():
            raise ValueError("Expected 200 matching KITTI training images and masks.")

        stems = sorted(masks)
        records = []
        mask_shapes = []
        for stem in stems:
            instance_map = read_png(archive, masks[stem], cv2.IMREAD_UNCHANGED)
            if instance_map.dtype != np.uint16 or instance_map.ndim != 2:
                raise ValueError(f"Expected a 16-bit instance mask for {stem}")
            records.append(convert_mask(instance_map))
            mask_shapes.append(instance_map.shape)

        if not any(record[0] for record in records):
            raise ValueError("No supported KITTI instance masks were found.")
        val_indices = split_frames(records)
        hashes = set()
        split_stats = {}
        for index, stem in enumerate(stems):
            split = "val" if index in val_indices else "train"
            other_split = "train" if split == "val" else "val"
            rows, class_ids, _, _ = records[index]
            image = read_png(archive, images[stem], cv2.IMREAD_COLOR)
            if image.shape[:2] != mask_shapes[index]:
                raise ValueError(f"Image and mask dimensions differ for {stem}")
            digest = hashlib.sha256(image.tobytes()).hexdigest()
            if digest in hashes:
                raise ValueError(f"Duplicate source image: {stem}")
            hashes.add(digest)
            success, jpeg = cv2.imencode(".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 92])
            if not success:
                raise ValueError(f"Unable to encode {stem}")
            (output / "images" / split / f"{stem}.jpg").write_bytes(jpeg.tobytes())
            (output / "labels" / split / f"{stem}.txt").write_text(
                "".join(f"{row}\n" for row in rows), encoding="ascii"
            )
            (output / "images" / other_split / f"{stem}.jpg").unlink(missing_ok=True)
            (output / "labels" / other_split / f"{stem}.txt").unlink(missing_ok=True)
            stats = split_stats.setdefault(
                split, {"images": 0, "empty_labels": 0, "instances": [0] * len(CLASSES)}
            )
            stats["images"] += 1
            stats["empty_labels"] += int(not rows)
            for class_id in class_ids:
                stats["instances"][class_id] += 1

    names = "".join(f"  {index}: {name}\n" for index, name in enumerate(CLASSES.values()))
    (output / "data.yaml").write_text(
        "train: images/train\nval: images/val\nnames:\n" + names, encoding="ascii"
    )
    overlaps = [overlap for _, _, values, _ in records for overlap in values]
    stats = {
        "source": "KITTI Semantic Instance Segmentation, official training split",
        "classes": list(CLASSES.values()),
        "splits": split_stats,
        "instances_skipped_no_positive_area_polygon": sum(record[3] for record in records),
        "polygon_mask_iou_mean": round(float(np.mean(overlaps)), 4),
        "polygon_mask_iou_p05": round(float(np.quantile(overlaps, 0.05)), 4),
    }
    (output / "stats.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="ascii")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Official KITTI data_semantics.zip")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    prepare(args.archive, args.output)
