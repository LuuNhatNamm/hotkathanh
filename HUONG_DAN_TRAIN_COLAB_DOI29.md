# Hướng dẫn chạy Colab và bàn giao kết quả — Đội 29

Đội **29 – Lưu Nhật Nam**, seed điền vào ô **`TEAM_ID = 34`**. Mọi thành viên dùng cùng seed này.

Tài liệu hướng dẫn chạy bộ dữ liệu mới, kiểm tra kết quả và chuẩn bị bài nộp. Chưa có kết quả huấn luyện cho bộ 372 ảnh train tại thời điểm viết hướng dẫn.

## 1. Lấy dữ liệu từ GitHub hoặc ZIP

Repo của đội: https://github.com/LuuNhatNamm/hotkathanh

### Cách A — Clone trực tiếp trong Colab

Tạo một ô code trước Bước 1, chạy:

```python
from pathlib import Path
import subprocess

repo_dir = Path("/content/hotkathanh")
if repo_dir.exists():
    subprocess.run(["git", "-C", str(repo_dir), "pull", "--ff-only"], check=True)
else:
    subprocess.run(["git", "clone", "--depth", "1",
                    "https://github.com/LuuNhatNamm/hotkathanh.git",
                    str(repo_dir)], check=True)
```

Trong ô tham số, đặt `DATASET_PATH = "/content/hotkathanh/data"`, chạy lại ô tham số rồi chạy Bước 1. Dùng đúng thư mục `data/` để train và val. `data_raw/` chứa nhãn tham khảo và dữ liệu cần rà.

Đồng đội đã có repo trên máy có thể chạy `git pull --ff-only` tại thư mục repo để cập nhật, sau khi lưu công việc đang làm.

### Cách B — Tải ZIP từ máy

Nếu dùng ZIP đã đóng gói, nhận từ Nam file sau và lưu trên máy trước khi mở Colab:

```text
hotkathanh_dataset_372train_26val_minitraffic.zip
```

Trên máy Nam, file nằm tại:

```text
E:\hackathon\hotkathanh_dataset_372train_26val_minitraffic.zip
```

File khoảng **91,72 MiB**. ZIP là lựa chọn thay thế khi không clone trực tiếp. Nội dung train/val tương ứng với bộ `data/` được bàn giao trong repo.

ZIP có cấu trúc:

```text
images/
  train/
  val/
labels/
  train/
  val/
data.yaml
```

Số liệu cần đối chiếu khi chạy kiểm tra:

| Tập | Ảnh | File nhãn | Đối tượng |
| --- | ---: | ---: | ---: |
| Train | 372 | 372 | 5.338 |
| Val | 26 | 26 | 372 |

Những phần đã xử lý trong dữ liệu bàn giao:

- Sửa 53 polygon tự cắt nhau.
- Rà và đổi 148 ID lớp trong 10 file nhãn.
- Loại 320 annotation trùng trong một ảnh train.
- Bổ sung 70 ảnh Mini Traffic Detection vào train, thêm 83 đối tượng. Trong đó 57 ảnh dùng polygon nguồn đã ánh xạ lớp, 13 ảnh được bổ sung mask người lái cùng phương tiện.
- Giữ 26 ảnh val của đội. Có sửa lớp trong nhãn val nên cần đánh giá lại khi so với mô hình cũ.

Kiểm tra bằng notebook trên ZIP mới cho kết quả **0 polygon không hợp lệ, 0 lỗi chặn và 0 cặp ảnh trùng/gần giống giữa train và val**. Kiểm tra này xác nhận cấu trúc và hình học nhãn, chất lượng đường viền và lớp vẫn cần xem qua ảnh minh họa.

## 2. Mở notebook và bật GPU

1. Mở [notebook Colab của đội](https://colab.research.google.com/drive/1avS8bArozgSf8Ww3EHmGQUtulP83bXL-?usp=sharing).
2. Nếu cần bản riêng, chọn **Tệp → Lưu bản sao trong Drive**.
3. Chọn **Thời gian chạy → Thay đổi loại thời gian chạy**.
4. Chọn **Python 3**, bật **GPU T4**, bấm **Lưu** rồi kết nối runtime.

Notebook gốc để đối chiếu: [Colab hướng dẫn cuộc thi](https://colab.research.google.com/drive/1qlJb8AYDsHpY-0kp2yMC_5CHouf6G5eQ?usp=sharing). Trong repo có bản `notebooks/train_and_export.ipynb`.

## 3. Chạy các ô khai báo đầu notebook

Chạy lần lượt, đợi mỗi ô hoàn thành rồi mới chạy ô kế tiếp:

1. **Hằng số của cuộc thi**.
2. **Thư viện 1/4**.
3. **Thư viện 2/4**.
4. **Thư viện 3/4**.
5. **Thư viện 4/4**.

Các ô này tạo biến và hàm dùng cho toàn bộ notebook. Sau khi runtime khởi động lại, phải chạy lại các ô đầu trước khi tiếp tục.

## 4. Điền ô “Tham số của đội”

Sửa các giá trị tương ứng trong ô tham số có sẵn, giữ các dòng còn lại của ô:

```python
TEAM_ID = 34
DATASET_PATH = "/content/hotkathanh/data"
MODEL_SIZE = "n"
EPOCHS = 60
BATCH = 16
PATIENCE = 20
TRAIN_IMGSZ = 640
INSTALL_PACKAGES = True
REQUIRE_GPU = True
DRIVE_OUTPUT_DIR = "/content/drive/MyDrive/doi29_seed34/run_372"
```

- Nếu đã clone theo Cách A, dùng `DATASET_PATH = "/content/hotkathanh/data"`. Nếu chọn upload ZIP, đặt `DATASET_PATH = ""` để Bước 1 hiện nút chọn file.
- Giữ `MODEL_SIZE = "n"` theo kiến trúc YOLO26n-seg của cuộc thi.
- Thư mục `run_372` dùng lưu kết quả lượt chạy mới. Nếu chạy thêm thí nghiệm, đổi sang thư mục riêng để giữ lại mô hình cũ.
- `VAL_RATIO` giữ mặc định. Bộ ZIP đã chia sẵn train/val nên không cần chia lại.

Chạy ô tham số sau khi chỉnh xong. Không dán đè toàn bộ ô bằng đoạn ngắn phía trên vì cuối ô còn có phần khởi tạo cần thiết.

## 5. Chạy Bước 0 — Chuẩn bị môi trường

1. Chạy ô **Bước 0**.
2. Cho phép kết nối Google Drive khi Colab yêu cầu để lưu kết quả.
3. Đợi cài thư viện và kiểm tra GPU hoàn tất.
4. Nếu notebook yêu cầu khởi động lại runtime sau khi cài đặt, thực hiện rồi chạy lại các ô đầu theo thứ tự.

Giữ phiên bản thư viện và cấu hình xuất mô hình của notebook. Chỉ chuyển bước khi ô đã chạy xong và không còn lỗi.

## 6. Chạy Bước 1 — Nạp dữ liệu

1. Chạy ô **Bước 1**.
2. Nếu clone repo, kiểm tra `DATASET_PATH` trỏ tới `/content/hotkathanh/data`. Nếu dùng ZIP, chọn file `hotkathanh_dataset_372train_26val_minitraffic.zip` khi được yêu cầu.
3. Đợi chuẩn bị dữ liệu hoàn tất.
4. Kiểm tra notebook nhận đúng **372 ảnh train, 26 ảnh val**.

Đường dẫn `E:\...` là đường dẫn trên máy Windows. Colab cần file được tải lên hoặc đường dẫn Google Drive đã mount.

Nếu muốn đọc ZIP từ Drive, tải ZIP vào Drive trước rồi điền đường dẫn thực tế, ví dụ:

```python
DATASET_PATH = "/content/drive/MyDrive/hotkathanh_dataset_372train_26val_minitraffic.zip"
```

Sau khi đổi đường dẫn, chạy lại ô tham số và Bước 1.

## 7. Chạy Bước 2 — Kiểm tra dữ liệu

1. Chạy ô **Bước 2**.
2. Đối chiếu số ảnh và đối tượng với bảng ở mục 1.
3. Kiểm tra không có polygon lỗi hoặc lỗi chặn.
4. Xem ảnh preview để kiểm tra polygon bám vật thể, đúng lớp và không có nhãn lặp rõ ràng.
5. Nếu có cảnh báo trùng/gần giống giữa train và val, kiểm tra lại trước khi train.

Các cảnh báo về lớp hiếm, vật thể nhỏ, ảnh nhiều đối tượng hoặc ảnh gần giống trong cùng train vẫn có thể xuất hiện. Ghi lại các cảnh báo đó để xem hạn chế dữ liệu.

**Điểm dừng kiểm tra:** nếu chỉ thấy 302 ảnh train, có thể đang dùng ZIP cũ. Chọn lại ZIP 372 ảnh và chạy lại từ Bước 1.

## 8. Chạy Bước 3 — Huấn luyện

1. Chạy ô **Bước 3**.
2. Theo dõi log epoch, loss và điểm val.
3. Đợi huấn luyện kết thúc hoặc dừng sớm theo `PATIENCE`.
4. Ghi lại đường dẫn `best.pt` notebook in ra và kiểm tra file đã được lưu sang Drive theo cấu hình.

Lượt đầu dùng 60 epoch, batch 16, ảnh 640. Nếu báo `CUDA out of memory`, giảm `BATCH = 8`, chạy lại ô tham số rồi chạy lại bước train. Nếu còn thiếu bộ nhớ, giảm tiếp và ghi lại batch thực tế trong bàn giao.

Thư mục Drive nhận các file ở những bước notebook thực hiện sao chép. Cấu hình này không đảm bảo tự sao lưu checkpoint sau từng epoch khi runtime mất kết nối.

## 9. Chạy Bước 4 — Xuất mô hình

1. Chạy ô **Bước 4** sau khi có `best.pt`.
2. Đợi xuất ONNX và đóng gói hoàn tất.
3. Kiểm tra notebook báo tạo được `submission.zip`.

Giữ cấu hình export có sẵn. File nộp cần chứa **`model.onnx` ngay ở gốc ZIP**, dung lượng theo giới hạn notebook là **không quá 42 MiB**.

Không thêm dataset, ảnh báo cáo hoặc `best.pt` vào ZIP nộp.

## 10. Chạy Bước 5 — Chấm thử theo cuộc thi

1. Chạy ô **Bước 5**.
2. Đợi suy luận đủ 26 ảnh val và tính điểm.
3. Ghi lại `mask mAP@[.5:.95]`, điểm `100 × mAP`, AP từng lớp và thời gian suy luận.
4. Xem 6 ảnh lỗi nhất trong phần báo cáo, thường nằm tại `/content/work/report/loi/`.

Ưu tiên xem các lớp còn yếu như Bus, Motorcycle, Bicycle và các lỗi nhầm Other vehicle thành Car, bỏ sót người hoặc biển báo.

Điểm **23,74** của lượt cũ được đo trước khi sửa lớp trong nhãn val. Muốn kết luận cải thiện, cần chấm mô hình cũ và mô hình mới trên **cùng bộ val đã sửa**, bằng cùng bộ chấm. Điểm val dùng để theo dõi thí nghiệm, điểm nộp chính thức phụ thuộc bộ test ẩn.

## 11. Chạy Bước 6 — Lưu và tải kết quả

1. Chạy ô **Bước 6** để tạo `run_report.json`.
2. Tải `submission.zip` và `run_report.json` theo nút tải của notebook.
3. Kiểm tra trong Drive có đủ ba file sau:

| File | Mục đích |
| --- | --- |
| `best.pt` | Giữ trọng số để đánh giá lại hoặc train tiếp |
| `submission.zip` | File mô hình để nộp theo hướng dẫn cuộc thi |
| `run_report.json` | Lưu cấu hình và kết quả để đối chiếu lượt chạy |

4. Lưu thêm ảnh hoặc log điểm ở Bước 5 để nhóm đối chiếu.
5. Nộp `submission.zip` lên hệ thống cuộc thi theo hướng dẫn trên trang nộp bài, rồi ghi lại điểm trả về.

## 12. Bàn giao cho cả nhóm

Gửi các file kết quả qua thư mục dùng chung của nhóm, kèm nội dung sau:

```text
Đội: 29 – Lưu Nhật Nam
TEAM_ID: 34
Dataset: hotkathanh_dataset_372train_26val_minitraffic.zip
Train/val: 372/26 ảnh
Mô hình: YOLO26n-seg
Epoch đã chạy: ...
Batch thực tế: ...
Kích thước ảnh: 640
GPU: ...
Mask mAP@[.5:.95] theo Bước 5: ...
Điểm val = 100 × mAP: ...
Điểm trên hệ thống nộp bài, nếu có: ...
Các lớp/lỗi cần sửa tiếp: ...
Link thư mục chứa best.pt, submission.zip, run_report.json: ...
```

Chưa có bằng chứng rằng thêm 70 ảnh sẽ tăng điểm bao nhiêu. Sau lượt chạy này, dùng điểm và ảnh lỗi để quyết định bổ sung ảnh đúng lớp còn yếu, thay vì tăng số lượng ảnh chung.

## 13. Xử lý lỗi thường gặp

| Hiện tượng | Cách xử lý |
| --- | --- |
| `IN_COLAB is not defined` | Chạy lại các ô đầu từ Hằng số và Thư viện 1/4 đến 4/4, rồi chạy ô tham số |
| `validate_team_id is not defined` | Chạy lại các ô thư viện trước Bước 0 |
| `TEAM_ID` chưa hợp lệ | Sửa thành `34` và chạy lại ô tham số |
| Không tìm thấy ZIP | Chọn lại file upload hoặc kiểm tra đúng đường dẫn Drive |
| Chỉ nhận 302 ảnh train | Đổi sang ZIP `372train_26val_minitraffic` rồi chạy lại Bước 1–2 |
| Hết bộ nhớ GPU | Giảm batch xuống 8, chạy lại ô tham số và bước train |
| Mất biến sau khi runtime khởi động lại | Chạy lại các ô khai báo và các bước tạo dữ liệu/biến cần thiết theo thứ tự |
| Không thấy kết quả trong Drive | Kiểm tra mount Drive, `DRIVE_OUTPUT_DIR` và thông báo sao chép ở từng bước; tải file về máy trước khi đóng runtime |

## Checklist trước khi báo hoàn thành

- [ ] Dùng đúng ZIP mới và `TEAM_ID = 34`.
- [ ] QC đủ 372 train, 26 val, không có lỗi chặn.
- [ ] Train hoàn tất và đã giữ `best.pt`.
- [ ] Export được `submission.zip` đúng cấu trúc.
- [ ] Chấm Bước 5, lưu điểm và xem ảnh lỗi.
- [ ] Chạy Bước 6, giữ `run_report.json`.
- [ ] Sao lưu kết quả ra Drive hoặc máy cá nhân.
- [ ] Bàn giao link file và cấu hình cho nhóm.
- [ ] Nộp bài và kiểm tra phản hồi của hệ thống.
