# Dataset Robotaxi 11 lớp

Nguồn hiện tại: traffic_light_50, 50 ảnh và nhãn polygon COCO đã ánh xạ. Chia 35 train, 10 test và 5 validation. Seed chia là 42. Giữ split có sẵn khi chạy notebook BTC và dùng test riêng nếu cần đánh giá bổ sung.

Nhãn nguồn vẫn cần QC theo source_traffic_light_50_README.md và source_traffic_light_50_review.csv. Thiếu Other vehicle. Rà biển báo thiếu, ghép người–xe và các polygon nhiều mảnh trước khi train.

27 ảnh chưa có nhãn nằm ở thư mục robotaxi-guideline11-pending-labels bên cạnh. Gán và kiểm tra nhãn rồi mới đưa ảnh vào tập tương ứng. File split_manifest.json ghi nguồn, SHA-256 và số lượng theo lớp.
