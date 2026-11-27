# Robotaxi · YOLO26n-seg

Mở [hướng dẫn HTML](huong-dan-robotaxi-yolo26.html) để xem sơ đồ use case, guideline 11 lớp và các bước chạy.

| Vai trò | Thư mục | Việc làm |
| --- | --- | --- |
| Thành viên gán nhãn | [robotaxi-dataset-merged](robotaxi-dataset-merged/README.md) | Rà ảnh và split, sửa mask theo [guideline](labeling_guideline.md), export YOLO-seg 11 lớp. |
| Thành viên huấn luyện | [notebooks/train_and_export.ipynb](notebooks/train_and_export.ipynb) | Đặt TEAM_ID và DATASET_PATH, chạy kiểm tra dữ liệu, train, đánh giá và xuất gói BTC. |
| Người chạy demo | [demo](demo/README.md) | Dùng best.pt của nhóm để xuất video có mask. |
| Trưởng nhóm | [submission](submission/README.md) | Nhận submission.zip và run_report.json, kiểm tra rồi nộp trên website BTC. |

## Dữ liệu

- **Bộ rà nhãn** là robotaxi-dataset-merged, có 277 ảnh: 194 train, 55 test, 28 validation. Nhãn 7 lớp và 11 lớp nằm riêng. Đọc split_report.json để tra ảnh gốc và các cặp gần trùng.
- **Đầu vào notebook** là robotaxi-guideline11-seg. Bản hiện tại có 50 cặp ảnh–nhãn (35 train, 10 test, 5 validation) và vẫn cần rà nhãn nguồn. Sau khi duyệt, đưa từng cặp ảnh–nhãn 11 lớp vào đúng split tương ứng. Với Colab, đưa bản export này lên Drive rồi đặt DATASET_PATH tới thư mục hoặc ZIP đó.
- **Bản nguồn** gồm robotaxi-kitti200-seg và robotaxi-guideline11-pending-labels. Giữ để đối chiếu khi chỉnh nhãn.

Thư mục work/ do notebook tạo khi chạy local. Thư mục runs/ xuất hiện sau khi chạy lệnh demo hoặc thử nghiệm Windows.
