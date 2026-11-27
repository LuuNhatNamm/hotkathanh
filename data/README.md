# Dữ liệu YOLO-seg 11 lớp đã duyệt

Thư mục đang chờ nhóm hoàn tất gán nhãn và duyệt. data.yaml đã khai báo thứ tự 11 lớp của BTC.

1. Rà ảnh trong [data_raw](../data_raw/README.md) theo [guideline](../labeling_guideline.md).
2. Xuất nhãn YOLO-seg sau khi duyệt. Chép ảnh và file TXT cùng tên gốc vào images/<split>/ và labels/<split>/, giữ split từ manifest. Ảnh nền phải được rà và có file TXT rỗng chủ ý.
3. Trỏ DATASET_PATH của [notebook BTC](../notebooks/train_and_export.ipynb) vào data/ hoặc ZIP tạo từ thư mục này. Chạy kiểm tra trước khi train. Notebook dùng train và val. Giữ test riêng.
