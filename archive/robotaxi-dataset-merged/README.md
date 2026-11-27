# Dataset Robotaxi gộp để rà và gán nhãn

Nguồn là ảnh của dataset 11 lớp, ảnh chờ gán nhãn và 200 ảnh KITTI. Ảnh của hai thư mục đầu giữ split hiện có. Ảnh KITTI được chia lại với seed 42 cho đủ tỉ lệ 70 train / 20 test / 10 val. Nhóm ảnh gần trùng nằm cùng split.

| Tập | Có nhãn 11 lớp | KITTI 7 lớp | Chưa có nhãn | Tổng |
| --- | ---: | ---: | ---: | ---: |
| train | 35 | 140 | 19 | 194 |
| test | 10 | 40 | 5 | 55 |
| val | 5 | 20 | 3 | 28 |

Kiểm tra SHA-256 file và pixel RGB đã giải mã. Có 0 ảnh trùng khớp và 23 cặp nghi gần trùng theo dHash với khoảng cách Hamming tối đa 2. Ảnh gần trùng được giữ cùng split để giảm rò rỉ. Xem split_report.json để truy nguồn.

Nhãn nguồn nằm trong labels_guideline11 và labels_kitti7, tách theo schema. Chỉ xuất thành images/ và labels/ cho notebook BTC sau khi đã chuẩn hóa nhãn KITTI, gán nhãn cho ảnh còn thiếu và rà soát chất lượng. Tập KITTI 7 lớp chưa tương đương schema 11 lớp. Đích train hiện tại là robotaxi-guideline11-seg.
