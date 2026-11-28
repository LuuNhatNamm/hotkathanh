# Dữ liệu YOLO-seg 11 lớp

## Tập dùng để huấn luyện và đánh giá

| Split | Ảnh | File nhãn | Đường dẫn |
| --- | ---: | ---: | --- |
| Train đã sửa | 398 | 398 | `images/train/`, `labels/train/` |
| Val đã sửa | 26 | 26 | `images/val/`, `labels/val/` |

Ảnh và nhãn được đặt trực tiếp trong thư mục split, giữ tên gốc. Các thư mục p1–p4 đã được gom về cấu trúc này. `data.yaml` dùng schema 11 lớp trong `labeling_guideline.md`.

Dùng `data/data.yaml` cho bước train/val. Tập train gồm 302 ảnh của đội và 70 ảnh Mini Traffic Detection, bổ sung 83 đối tượng. Trong số ảnh bổ sung, 57 ảnh dùng polygon nguồn đã ánh xạ và 13 ảnh được vẽ thêm phần người lái để tạo mask Cyclist hoặc Motorcyclist. Xem [nguồn và danh sách ảnh](../data_raw/sources/mini_traffic_detection/README.md).

Phần 1 đợt 2 bổ sung 26 ảnh từ chia_data/data1 (13 COCO, 13 Mini Traffic Detection), bỏ 4 ảnh trùng với ảnh đã có. Xem [manifest](../data_raw/sources/chia_data/part1_manifest.json).

## Val chờ rà

Chín ảnh thuộc val ban đầu được tách vào `images/val_review/`. Bảy file nhãn gốc hiện có được giữ nguyên trong `labels/val_review/<nguồn>/`. Hai ảnh còn lại chưa có nhãn gốc.

Nhãn trong val_review dùng schema của từng nguồn. Đặc biệt, KITTI gốc dùng 7 lớp với thứ tự `person, rider, car, truck, bus, motorcycle, bicycle`. Cần rà và ánh xạ sang 11 lớp trước khi chuyển cặp ảnh–nhãn vào `images/val/`, `labels/val/`.

| Ảnh | Nguồn nhãn gốc |
| --- | --- |
| cvat__VisDrone_0000327_00601_d_0000714.jpg | chưa có nhãn gốc |
| guideline11__coco_000000577932.jpg | guideline11 |
| kitti7__000074_10.jpg | kitti7 |
| kitti7__000077_10.jpg | kitti7 |
| kitti7__000108_10.jpg | kitti7 |
| kitti7__000117_10.jpg | kitti7 |
| kitti7__000162_10.jpg | kitti7 |
| pending__xe_tho_so__img_008.jpg | chưa có nhãn gốc |
| vn_sign_30__zalo_9767.png | vn_sign_30 |

## Train chờ hoàn thiện

Chín ảnh train ban đầu còn thiếu nhãn đã sửa được giữ tại `data_raw/images/train/`. Nhãn tham khảo hiện có nằm trong `data_raw/labels/train/<nguồn>/`.

- `pending__xe_tho_so__img_031.jpg`
- `pending__xe_tho_so__img_034.jpg`
- `vn_sign_30__zalo_1069.png`
- `vn_sign_30__zalo_12213.png`
- `vn_sign_30__zalo_3426.png`
- `vn_sign_30__zalo_4737.png`
- `vn_sign_30__zalo_4816.png`
- `vn_sign_30__zalo_698.png`
- `vn_sign_30__zalo_9576.png`

Phân chia gốc của bộ ảnh nhóm là 311 train và 35 val. Các ảnh gốc chờ rà giữ split cũ khi bổ sung. 70 ảnh Mini Traffic Detection chỉ bổ sung vào train của nhóm.

Trỏ dataset của notebook vào thư mục `data/`, kiểm tra nhãn rồi chạy train. Mỗi file TXT chứa polygon YOLO-seg cùng tên gốc với ảnh tương ứng.
