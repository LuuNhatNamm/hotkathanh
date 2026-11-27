# Chạy video demo Robotaxi

Đặt clip tại input.mp4 trong thư mục này hoặc truyền đường dẫn với -Video. Dùng checkpoint best.pt đã fine-tune của nhóm.

Mở PowerShell ở thư mục gốc dự án:

    .\demo\run-demo.ps1 -Weights 'C:\duong-dan-den\best.pt'

Kết quả được lưu trong runs/robotaxi/demo-<mã-lần-chạy>/. Nếu lệnh yolo chưa có, cài Ultralytics trong môi trường Python đang dùng.

Notebook BTC xử lý export ONNX và bài nộp. Video demo dùng để trình bày và rà lỗi dự đoán.
