# Dữ liệu chờ xử lý

Dataset có 346 ảnh. Dùng hai tập train và val, theo vị trí ảnh hiện tại. 69 ảnh ở test cũ đã nằm trong train. Tập val giữ nguyên 35 ảnh.

| Split | Tổng ảnh | Nhãn 11 lớp chưa duyệt | Nhãn KITTI 7 lớp | Nhãn Sign một phần | Chưa có nhãn |
| --- | ---: | ---: | ---: | ---: | ---: |
| train | 311 | 45 | 180 | 27 | 59 |
| val | 35 | 5 | 20 | 3 | 7 |

Nhãn tham khảo nằm trong labels/train và labels/val, bên trong chia theo nguồn guideline11, kitti7 và vn_sign_30. Mỗi file TXT cùng tên gốc và split với ảnh. Các nhãn Sign cần rà, gán bổ sung trước khi đưa vào [data](../data/README.md). Xem [ghi chú nguồn vn_sign_30](sources/vn_sign_30/README.md).

Tra nguồn và 23 cặp nghi gần trùng trong split_manifest.json. Các cặp này nằm cùng split.
