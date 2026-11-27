# Robotaxi · YOLO26n-seg

Mở [hướng dẫn HTML](huong-dan-robotaxi-yolo26.html) để xem sơ đồ use case và quy trình của nhóm.

| Vai trò | Đường dẫn | Việc làm |
| --- | --- | --- |
| Gán nhãn | [data_raw](data_raw/README.md) | Rà ảnh và nhãn tham khảo theo [guideline 11 lớp](labeling_guideline.md). Export cặp ảnh–nhãn đã duyệt sang data. |
| Huấn luyện | [data](data/README.md) và [notebook BTC](notebooks/train_and_export.ipynb) | Nạp dữ liệu đã duyệt, kiểm tra, train, đánh giá và tạo gói nộp. |
| Chạy demo | [demo](demo/README.md) | Dùng best.pt của nhóm để xuất video có mask. |
| Trưởng nhóm | [submission](submission/README.md) | Tập hợp submission.zip và run_report.json để bàn giao. |

Bộ data_raw có **346 ảnh**, chia **242 train / 69 test / 35 val**, gồm 39 ảnh CVAT chưa có nhãn và 30 ảnh vn_sign_30 có nhãn Sign một phần, cần rà và gán bổ sung. data/ có schema 11 lớp và chờ nhãn đã duyệt. Các bộ cũ được lưu trong archive/ để đối chiếu.
