# Bản nguồn các nhánh và quyết định hợp nhất

Mỗi thư mục con là snapshot các file được thêm/sửa trên nhánh so với merge-base. Tên thư mục thay dấu `/` trong tên nhánh bằng `_`. Những đường dẫn `data/` bên trong snapshot là bản xuất của thành viên, chưa phải tập huấn luyện hiện hành.

Xem `reconciliation.json` để tra từng ảnh và quyết định. `qc_unified.json` kiểm tra tập đang dùng. Bộ huấn luyện chung nằm tại thư mục `data/` ở gốc repository. Quy trình chi tiết nằm tại `MERGE_DATA_2026-11-28.md` ở gốc.
