# Lọc batch mới theo labeling_guideline.md

Nguồn: nhánh `data/extra-batch`, commit `25e5cd3`. Đã xem ảnh cùng overlay 26 cặp train mới, đối chiếu toàn bộ guideline của repo. Đây là rà nội dung và hình học; ảnh nghi ngờ được giữ chờ sửa, không xóa nguồn.

## Kết quả

- 133 ảnh trong data của nhánh: 81 cặp trùng/gần trùng giữ nhãn hiện tại; 25 ảnh thiếu nhãn; 27 cặp chưa trùng.
- Trong 27 cặp chưa trùng: nhận 1 ảnh train sau sửa lớp; 25 cặp train cần sửa/rà; 1 cặp val mới giữ chờ rà để bảo toàn val 50.
- Dữ liệu đang dùng: **384 ảnh train / 5.496 instance**, **50 ảnh val / 641 instance**.
- Hai ảnh bicycle8 và bus11 từng được nhập tạm đã chuyển ra khỏi train sau lượt đọc guideline kỹ.

## Quyết định từng ảnh mới

| Ảnh | Quyết định / việc cần sửa | Mục guideline |
| --- | --- | --- |
| 000000423693.jpg | Ảnh tàu du lịch có TXT rỗng; cần quyết định Other vehicle và rà các đối tượng đủ lớn. | 1 Other vehicle; 2.3; 5.4 |
| 000000483165.jpg | Thiếu các xe đạp đỗ phía sau và có polygon tự cắt. | 2.1; 2.3; 3 Bicycle; 6 |
| 000000489107.jpg | Chỉ có người chính và cyclist; thiếu xe/đám người/biển báo rõ ở nền. | 2.3; 3 Sign |
| 000000508985.jpg | Các ô tô rõ ở làn đường chưa được gán. | 2.3; 3 Car |
| 000000514376.jpg | Xe điện đường ray đang ghi Bus; cần quy ước Other vehicle theo catch-all, bổ sung xe nền. | 1 Bus; 1 Other vehicle; 2.3; 5.4 |
| 000000514619.jpg | Xe nền và một số người đủ lớn chưa được gán. | 2.3 |
| 000000514904.jpg | Một người chính bị tách thành nhiều Pedestrian; có polygon lỗi, thiếu xe đạp ở nền. | 2.1; 2.3; 6 |
| 000000518853.jpg | Thiếu xe ô tô ở trái và biển đường rõ trong ảnh. | 2.3; 3 Car; 3 Sign |
| 000000521998.jpg | Một người và xe đạp bị tách thành nhiều instance; thiếu mask xe nền và biển đỗ xe, polygon lỗi. | 2.1; 2.3; 3 Sign; 6 |
| 000000530683.jpg | Cyclist chính bị tách người/xe; một số mảnh nhãn chồng hoặc tự cắt. | 3 Bicycle/Cyclist; 2.1; 2.2; 6 |
| 000000533739.jpg | Thiếu nhiều Car rõ phía trước. | 2.3; 3 Car |
| bicycle10.jpg | Xe có bàn đạp và người lái đang ghi Motorcyclist 5; cần Cyclist 7, bổ sung người phía sau đủ lớn. | 3 Bicycle/Cyclist; 2.3 |
| bicycle7.jpg | Xe đạp có người lái; đã sửa Motorcyclist 5 thành Cyclist 7, giữ một instance người+xe. | 3 Bicycle/Cyclist |
| bicycle8.jpg | Người đang dắt xe: Pedestrian 8 và Bicycle 6 đúng lớp, nhưng hai mask chồng nhau khoảng 23.9% diện tích mask xe; cần sửa phần che khuất. | 2.2; 3 Bicycle; 3 Pedestrian |
| bicycle9.jpg | Người đứng cạnh/đang dắt hoặc bước xuống xe, yên thấy trống; nhãn gộp Cyclist cần rà lại, có thể cần Pedestrian + Bicycle. | 3 Bicycle/Cyclist; 4 Người bước lên/bước xuống |
| bus11.jpg | Có người lộ phía trên nóc bus ngoài mask; cần xác nhận tư thế/instance theo guideline trước khi coi là đủ nhãn. | 2.3; 3 Pedestrian |
| bus12.jpg | Thiếu các Car đủ lớn ở hai bên bus. | 2.3; 3 Car |
| bus13.jpg | Thiếu người đứng bên trái bus; không gán tượng trên xe. | 2.3; 2.7; 3 Pedestrian |
| truck1.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck10.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck2.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck5.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck6.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck7.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck8.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |
| truck9.jpg | Nhãn Truck phủ cả xe; cần kiểm tra cấu trúc xe tải liền khối hay đầu kéo/rơ-moóc. Nếu là đầu kéo phải tách Truck 2 và Other vehicle 3 trước khi nhập. | 3 Truck; 3 Other vehicle; 4 Đầu kéo + container |

Các file chờ sửa nằm trong `data_raw/sources/extra_batch_remote/pending/`. Xem `sync_manifest.json` để tra ảnh gốc, nhánh và trạng thái từng file. Nhãn được rút khỏi train dùng tên `extra25e5__...`, bản nhãn gốc vẫn giữ tên nguồn.

Chưa tự sửa nhãn của 81 ảnh trùng vì chúng có thể là phiên bản cũ của nhãn đã sửa ở main. File TXT tồn tại hoặc commit ghi reviewed không phải bằng chứng gán đủ đối tượng.
