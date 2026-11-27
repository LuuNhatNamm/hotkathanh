# Dữ liệu chờ xử lý

Dataset có 403 ảnh chờ rà, gồm 346 ảnh ở bộ phân công ban đầu và 57 ảnh Mini Traffic Detection mới. Giữ split của từng nguồn.

| Split | Tổng ảnh | Nhãn 11 lớp ban đầu chưa duyệt | Nhãn KITTI 7 lớp | Nhãn Sign một phần | Chưa có nhãn | Mini Traffic Detection |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| train | 347 | 45 | 180 | 27 | 59 | 36 |
| val | 56 | 5 | 20 | 3 | 7 | 21 |

Nhãn tham khảo nằm trong labels/train và labels/val, bên trong chia theo nguồn guideline11, kitti7 và vn_sign_30. Mỗi file TXT cùng tên gốc và split với ảnh. Các nhãn Sign cần rà, gán bổ sung trước khi đưa vào [data](../data/README.md). Xem [ghi chú nguồn vn_sign_30](sources/vn_sign_30/README.md).

Tra nguồn và 23 cặp nghi gần trùng trong split_manifest.json. Các cặp này nằm cùng split.

Mini Traffic Detection có nhãn polygon ánh xạ sang bộ 11 lớp trong `labels/<split>/mini_traffic_detection/`. Xem [nguồn và danh sách import](sources/mini_traffic_detection/README.md).
