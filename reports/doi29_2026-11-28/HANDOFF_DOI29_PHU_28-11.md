# Handoff — Phú (Đội 29) — 28/11/2026

## 1. Đã làm hôm nay

| Việc | Kết quả | Vị trí |
| --- | --- | --- |
| Đồng bộ repo với main | Repo local ở `main` @ `4efc1ee`, `data/` = 372 train / 26 val | `F:\AI20k\team repo\hotkathanh` |
| PR #1 (Phần 1 đợt 1) | Đã đóng kèm bình luận: nội dung đã vào main qua `e7c5e4f` | github.com/LuuNhatNamm/hotkathanh/pull/1 |
| Phần 1 đợt 2 (`chia_data/data1`) | 26 ảnh mới gán xong trên CVAT (task 78), 234 đối tượng; bỏ 4 ảnh trùng md5 (bicycle17, bicycle21, bus14, bus20) | branch `Phu-1b` commit `6c02ac6`, đã push 10:04 |
| Train lượt run_372 | Colab T4, YOLO26n-seg, TEAM_ID 34, 60 epoch, batch 16, imgsz 640 | xem `BAO_CAO_MODEL_DOI29.md` |
| Điểm val (bộ chấm nhúng) | mask mAP@50 = 0,3616 → 100 × √mAP50 ≈ 60,1; mAP@[.5:.95] = 0,208 | `run_report.json` |
| Nộp bài | run_372: 47,13 (09:57). run_398 (thêm 26 ảnh Phần 1 đợt 2, 45 epoch): **49,48** (10:23), cao nhất đội. Private đã chọn: 49,48 + 48,49. Hạng public chốt: 56/87 | competition.antco.ai |

## 2. Thông tin bàn giao (mẫu mục 12 của hướng dẫn)

```text
Đội: 29 – Lưu Nhật Nam
TEAM_ID: 34
Dataset: data/ của repo, main @ 4efc1ee (giống ZIP 372train_26val_minitraffic)
Train/val: 372/26 ảnh
Mô hình: YOLO26n-seg
Epoch đã chạy: 60
Batch thực tế: 16
Kích thước ảnh: 640
GPU: Colab Tesla T4
Mask mAP@[.5:.95] theo Bước 5: 0,2082
Điểm val = 100 × mAP@[.5:.95]: 20,82  (theo công thức cuộc thi 100 × √mAP50: ≈ 60,1)
Điểm trên hệ thống nộp bài, nếu có: 47,13 (public, nộp 09:57 28/11; mAP@50 = 22,21)
Các lớp/lỗi cần sửa tiếp: Motorcycle, Bicycle, Bus, Other vehicle, Pedestrian (AP thấp); thiếu cảnh đường VN có xe máy
Link thư mục chứa best.pt, submission.zip, run_report.json: zip đính kèm (doi29_run372_bao_cao.zip)
```

## 3. Việc còn mở, cần nhóm quyết

1. `Phu-1b` **đã push** (10:04). Cần mở PR vào main: model train trên nhánh này được 49,48 (+2,35 so với 372 ảnh). Trước khi gộp, cân nhắc bỏ 3 ảnh không phải cảnh đường: `coco__000000102202` (tàu công viên), `coco__000000124277` (đường ray nhìn từ trên cao), `minitraffic__bicycle20` (ảnh sản phẩm nền trắng).
2. Tram trong `coco__000000139507` đang gán Bus; theo định nghĩa lớp có thể nên là Other vehicle.
3. Gán `chia_data/data2-4` (90 ảnh) theo cùng quy trình: lọc trùng md5 với `data/`, đổi tên `coco__` / `minitraffic__`, CVAT + SAM3, rà theo guideline, export 1 polygon mỗi instance. Công cụ: `F:\AI20k\tools\cvat_label\` (`stage_chia.py`, `cvat_chia.py`, `sam_label.py`, `cleanup.py`, `fix_export.py`, `check_data.py`).
4. Chọn tối đa 2 bài tính điểm private trên trang nộp bài trước 10:30.
5. Hướng nâng điểm chi tiết: mục 4 của `BAO_CAO_MODEL_DOI29.md`.

## 4. Lưu ý kỹ thuật

- Container CVAT `nuclio-nuclio-sam3-autolabel` giữ khoảng 6,7 GB VRAM khi chạy; dừng nó (`docker stop nuclio-nuclio-sam3-autolabel`) trước khi train local batch 16 trên RTX 3060.
- Venv train local đã cài sẵn: `F:\AI20k\venv-yolo` (torch CUDA + bản ghim của notebook).
- Không chạy `fix_merges.py` lại trên task 78: nó xoá nhầm 3 xe đạp rõ ở frame 1.
- Local `.git/info/exclude` có `chia_data/`, `__MACOSX/`, `docs/superpowers/`, `work/` (chỉ máy này).
