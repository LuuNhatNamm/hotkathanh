# Dữ liệu chờ xử lý

Bản gộp gồm dữ liệu trước đó và 39 ảnh trong RoboTaxi_v3_CVAT_moi. Ảnh cũ giữ nguyên split. Ảnh mới có cùng mã nhóm trong tên VisDrone được xếp cùng tập.

| Split | Tổng | Ảnh CVAT mới | Nhãn 11 lớp chưa duyệt | Nhãn KITTI 7 lớp | Chưa có nhãn |
| --- | ---: | ---: | ---: | ---: | ---: |
| train | 221 | 27 | 35 | 140 | 46 |
| test | 63 | 8 | 10 | 40 | 13 |
| val | 32 | 4 | 5 | 20 | 7 |

labels_reference/guideline11/ chứa 50 nhãn ánh xạ cần rà. labels_reference/kitti7/ chứa 200 nhãn nguồn cần chuyển sang 11 lớp. 66 ảnh còn lại chưa có nhãn. File tham khảo có cùng tên gốc và nằm cùng split với ảnh.

Đọc split_manifest.json để tra nguồn và 23 cặp nghi gần trùng. Các cặp này nằm cùng split. Chỉ đưa cặp ảnh và nhãn đã duyệt vào [data](../data/README.md).
