# Bổ sung ảnh có Bus, xe máy hoặc xe đạp

Nguồn cục bộ: `E:\hackathon\dataset\New folder`, 300 ảnh có polygon YOLO-seg 7 lớp. Tên ảnh dạng COCO; nguồn chưa cung cấp thông tin giấy phép trong thư mục này.

Đã chọn 35 ảnh qua lượt xem ảnh và overlay, gồm **11 train, 24 val**. Mỗi ảnh có ít nhất một instance Bus, Motorcycle, Motorcyclist, Bicycle hoặc Cyclist sau chuyển đổi. Giữ nhãn các lớp khác trong cùng ảnh. Các ảnh chưa chọn vẫn nằm ở nguồn, chưa tự động coi là nhãn đạt chuẩn.

## Chuyển sang schema 11 lớp

| Lớp nguồn | ID nguồn | ID đội |
| --- | ---: | ---: |
| bicycle | 0 | 6 hoặc 7 khi gộp người lái |
| bus | 1 | 1 |
| car | 2 | 0 |
| motorcycle | 3 | 4 hoặc 5 khi gộp người lái |
| person | 4 | 8 khi không ngồi trên xe |
| traffic light | 5 | 10 |
| truck | 6 | 2; chỉnh từng ca bán tải, bus hoặc rơ-moóc |

Đã gộp các mảnh cùng instance, gộp người và xe khi nhận ra người ngồi trên xe, bỏ nhãn hành khách trong cửa kính, bỏ vật thể dưới ngưỡng cạnh ngắn của guideline và bổ sung một số mặt biển báo còn thiếu. Những ca che khuất hoặc polygon quá thiếu được để lại. Polygon nhiều phần được nối bằng đường hẹp để biểu diễn trong một dòng YOLO-seg. Đây là nhãn hỗ trợ bằng công cụ và đã xem overlay; kiểm tra hình học không chứng minh toàn bộ ngữ nghĩa/đường viền đều chính xác tuyệt đối.

## Phân chia và kết quả kiểm tra

- Giữ nguyên 26 ảnh val trước đó; thêm 24 ảnh để đủ 50. Các ảnh chọn vào val không được thêm vào train.
- Train hiện có **383 ảnh / 5.495 instance**. Val có **50 ảnh / 641 instance**.
- Chạy lại hàm kiểm tra từ notebook: 0 polygon lỗi, 0 lỗi chặn, 0 rò rỉ ảnh trùng/gần trùng train–val.
- Phần thêm mới còn kiểm tra pHash với ngưỡng khoảng cách 4 và dHash ngưỡng 2, không phát hiện cặp nghi trùng liên quan đến ảnh mới.
- Val bổ sung chủ đích thiên về Bus. Để so mô hình cũ/mới, chấm cả hai trên cùng val 50; không so trực tiếp điểm với val 26 trước đó. Danh sách 26 ảnh cũ có trong manifest.

## Dấu vết kiểm tra

- `import_manifest.json`: ảnh nguồn, split đích, thao tác gộp/xóa/bổ sung và SHA256 ảnh.
- `source_labels_selected.zip`: nhãn nguồn 7 lớp của các ảnh được chọn, giữ bản trước sửa.
- `qc_additions.json`: kiểm tra phần bổ sung.
- `qc_full_dataset.json`: kết quả kiểm tra toàn bộ data bằng hàm notebook.
- `not_imported.json`: các ảnh còn lại và phạm vi cần rà tiếp.

Nhãn và ảnh dùng train nằm tại `data/labels/{train,val}` và `data/images/{train,val}`. File nguồn không bị sửa.
