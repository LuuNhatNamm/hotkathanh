# Mini Traffic Detection

Nguồn [DatasetNinja](https://datasetninja.com/mini-traffic-detection) công bố 226 ảnh và ghi giấy phép [DbCL v1.0](https://opendatacommons.org/licenses/dbcl/1-0/).

Đã chọn 57 ảnh có polygon phù hợp và qua lượt rà toàn ảnh. Chia nguyên theo nguồn với 36 ảnh train và 21 ảnh val. Nhãn YOLO-seg chỉ dùng polygon, chuẩn hóa tọa độ theo kích thước ảnh và ánh xạ sang ID của bài. Hộp chữ nhật trong nguồn được dùng để kiểm tra độ đầy đủ của polygon.

| Lớp | ID | Instance train | Instance val |
| --- | ---: | ---: | ---: |
| car | 0 | 28 | 8 |
| bus | 1 | 9 | 3 |
| truck | 2 | 1 | 0 |
| motorcycle | 4 | 7 | 3 |
| bicycle | 6 | 1 | 3 |
| person | 8 | 0 | 3 |
| traffic_light | 10 | 2 | 2 |

Các ảnh có người đang đi xe nhưng mask chỉ phủ xe, ảnh có đầu kéo và rơ-moóc gộp chung, ảnh thấy đối tượng thuộc bộ lớp mà nguồn chưa gán, hoặc có vấn đề hình học được để lại để rà riêng. Một số ảnh chụp sản phẩm và cảnh ít liên quan cũng được để lại.

Danh sách ảnh qua lượt lọc ban đầu nằm trong [import_review.json](import_review.json).

## Dữ liệu đã đưa vào train của đội

57 cặp đã chọn cùng 13 cặp được vẽ bổ sung người lái đã nhập vào `data/images/train/` và `data/labels/train/`. Có 6 mask Cyclist và 7 mask Motorcyclist bổ sung, mỗi mask phủ phần nhìn thấy của xe và người lái. Ảnh nguồn dùng split train/val riêng. Trong bài của nhóm, toàn bộ 70 ảnh này nằm ở train, còn tập val 26 ảnh của nhóm dùng cho việc đối chiếu các lượt train.

Xem [danh sách cặp ảnh–nhãn và nguồn từng ảnh](train_import.json). Bộ dữ liệu sau nhập đã chạy kiểm tra của notebook với 0 polygon không hợp lệ và 0 cặp ảnh gần trùng giữa train và val.
