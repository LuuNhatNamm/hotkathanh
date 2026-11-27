# Dữ liệu chờ xử lý

Bộ gộp có 346 ảnh, gồm 39 ảnh CVAT và 30 ảnh từ vn_sign_30. Các ảnh trước đó giữ nguyên split.

| Split | Tổng | Ảnh CVAT | Nhãn 11 lớp chưa duyệt | Nhãn KITTI 7 lớp | Nhãn Sign một phần | Chưa có nhãn |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| train | 242 | 27 | 35 | 140 | 21 | 46 |
| test | 69 | 8 | 10 | 40 | 6 | 13 |
| val | 35 | 4 | 5 | 20 | 3 | 7 |

Nhãn tham khảo có cùng tên gốc và split với ảnh. Bộ vn_sign_30 có 127 nhãn Sign (ID 9) chuyển từ box. Cần kiểm tra biên, thêm biển bị thiếu và gán các lớp đối tượng còn lại trước khi đưa vào [data](../data/README.md). Xem [ghi chú nguồn vn_sign_30](sources/vn_sign_30/README.md).

Đọc split_manifest.json để tra nguồn và 23 cặp nghi gần trùng. Các cặp này nằm cùng split.
