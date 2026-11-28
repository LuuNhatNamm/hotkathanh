# Đội 29 — dữ liệu đã lọc và thử cấu hình YOLO26n-seg

## Bộ đang dùng

- Đã pull main: không có commit mới. Dữ liệu mới nằm trên nhánh `data/extra-batch`, commit `25e5cd3`, đã fetch và tải về để kiểm tra.
- Không merge cả nhánh vào main vì lịch sử riêng và có thể ghi đè nhãn đã sửa.
- Theo guideline, chỉ nhận thêm bicycle7, sửa Motorcyclist 5 thành Cyclist 7. Giữ 81 ảnh trùng/gần trùng ngoài lượt nhập mới; 51 ảnh thiếu nhãn/cần sửa hoặc rà được giữ trong pending.
- Bộ dùng train hiện: **384 ảnh / 5.496 instance**, val **50 ảnh / 641 instance**. Giữ nguyên nội dung val 50 đã dùng chấm mô hình cũ.
- Kiểm tra bằng hàm notebook: 0 polygon lỗi, 0 lỗi chặn, 0 trùng/gần trùng giữa train và val. Kiểm tra này không khẳng định mọi đường viền/nhãn cũ đều hoàn hảo.
- Đọc [quyết định lọc từng ảnh mới](data_raw/sources/extra_batch_remote/LOC_THEO_GUIDELINE.md).

## Mô hình làm mốc

`out/submission.zip` đã kiểm tra ONNX và SHA256 khớp `out/run_report.json`. Báo cáo ghi mask mAP 0,273063, tương ứng **27,31 điểm trên val 50**. Train 60 epoch, batch 16, patience 20, YOLO26n-seg pretrained, GPU L4. AP Motorcycle khoảng 0,0165 và Bicycle khoảng 0,0386 còn yếu.

Không sửa trực tiếp trọng số ONNX để tạo mô hình tốt hơn. Bản notebook mới sẽ huấn luyện từ pretrained `.pt`, giữ mô hình ONNX cũ làm ứng viên so sánh. Chưa có best.pt của lượt cũ trong out nên không fine-tune từ trọng số cũ.

## Chạy từng bước

1. Mở Colab, chọn **Tệp → Tải notebook lên**. Chọn `notebooks/train_and_export_team34_tuning.ipynb` trong repo.
2. Bật GPU L4 nếu có; T4 cũng có thể chạy. Giữ batch 16; nếu cấu hình mask_ratio 2 hết bộ nhớ thì giảm batch 8 cho tất cả cấu hình để so công bằng và chạy lại.
3. Chạy các ô đầu theo thứ tự: Hằng số → Thư viện 1/4 đến 4/4 → Tham số → Bước 0. TEAM_ID đã đặt 34.
4. Ở Bước 1, upload **`E:\hackathon\hotkathanh_tuning_384train_50val.zip`**. Gói gồm data và baseline model/report/khóa val. Không dùng ZIP chỉ có dataset vì ô tuning cần baseline.
5. Chạy Bước 2, đối chiếu 384 train / 50 val, không có lỗi chặn hoặc polygon lỗi.
6. Chạy Bước 3. Notebook khóa nội dung val bằng hash, chấm lại baseline, rồi thử các cấu hình trong bảng bên dưới. Mỗi cấu hình khởi tạo độc lập từ yolo26n-seg.pt và dùng cùng seed 34.
7. Đợi tất cả cấu hình kết thúc. Đọc thông báo ứng viên được chọn và lỗi nếu có. Nếu cấu hình nào lỗi, thử nghiệm chưa đủ; kiểm tra tuning_results.json trước khi quyết định chạy lại.
8. Chạy Bước 4–6 để chấm lại ứng viên được chọn, xem ảnh lỗi, xuất báo cáo và tải submission.zip. Hợp đồng ONNX và bộ chấm giữ nguyên của notebook gốc.
9. Kết quả nằm trong Drive `doi29_seed34/tuning_v2/<thời điểm chạy>/`. Mỗi cấu hình có thư mục riêng; file được chọn nằm trong `selected/`. tuning_results.json ghi các lượt và trạng thái.

| Cấu hình | Epoch tối đa | Patience | Thay đổi |
| --- | ---: | ---: | --- |
| baseline_existing | không train | — | Chấm lại ONNX 27,31 điểm trên đúng val hiện tại |
| default60 | 60 | 20 | Mặc định, optimizer auto, trên train đã cập nhật |
| mask2_100 | 100 | 25 | optimizer auto, mask_ratio=2 |
| mild_mask2_100 | 100 | 25 | mask_ratio=2, mosaic=0.5, scale=0.3, mixup=0, copy_paste=0, cos_lr=True |

Tổng tối đa 260 epoch cho ba lượt mới; có dừng sớm. mask_ratio=2 tăng độ phân giải nhãn mask trong huấn luyện, không đổi kích thước mask đầu ra ONNX. Đây là các giả thuyết cần chấm, chưa khẳng định cấu hình nào tốt nhất.

## Cách chọn và giữ mô hình

- Chọn bằng mask mAP@[.5:.95] của bộ chấm ở cùng val 50. Khi bằng điểm, giữ ứng viên xuất hiện trước, baseline được ưu tiên.
- Nếu baseline thắng, selected chứa ZIP cũ và báo cáo có ghi tuning; không có best.pt cũ vì file này chưa được cung cấp. Thông tin huấn luyện gốc trong báo cáo được giữ nguyên.
- Nếu mô hình mới thắng, lưu cả best.pt mới, submission.zip, run_report.json và bảng so sánh.
- Đã thử logic chọn ứng viên bằng mô phỏng: mô hình mới thắng, baseline thắng và cả ba lượt train lỗi. Đã chạy nạp dữ liệu thật bằng hàm notebook và kiểm tra khóa val. Chưa train các cấu hình mới vì máy local có PyTorch CPU, không có CUDA.
- Điểm val đã dùng chọn cấu hình nên có thể lạc quan; kết quả cuối cùng cần kiểm tra trên test ẩn.

Cấu hình chi tiết: `configs/team34_tuning.json`. Notebook nhúng các cấu hình này để có thể upload chạy độc lập; muốn thay hãy sửa danh sách TUNING_PROFILES trong ô tham số của notebook.

Các thay đổi mới được bàn giao cùng bản cập nhật repository này. Không sửa hay thay thế file nộp cũ ở out.
