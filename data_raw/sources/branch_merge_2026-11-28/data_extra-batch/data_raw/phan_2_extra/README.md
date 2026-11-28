# Bộ ảnh bổ sung · 117 ảnh

Dữ liệu thô bổ sung cho bốn thành viên, chia sẵn thành bốn thư mục, mỗi người một thư mục. Toàn bộ là ảnh chưa có nhãn; nhãn cần gán theo [guideline 11 lớp](../../labeling_guideline.md).

| Thư mục | Tổng ảnh | Tên COCO | Tên theo lớp | Ghi chú |
| --- | ---: | ---: | ---: | --- |
| data1 | 30 | 13 | 17 | bicycle, bus, truck |
| data2 | 28 | 12 | 16 | bicycle, bus, truck |
| data3 | 30 | 18 | 12 | bicycle, bus, truck |
| data4 | 29 | 13 | 16 | bicycle, bus |
| **Tổng** | **117** | 56 | 61 | |

## Nguồn và cách tạo

- Nguồn gốc: `~/Downloads/ai-action/chia_data`, gồm `data1`–`data4`, mỗi thư mục 30 ảnh.
- Đã loại 2 ảnh trùng nội dung với dữ liệu đang có trong repo (kiểm tra bằng SHA-1), vì vậy data4 và data2 bớt 1 ảnh:
  - `data4/000000274272.jpg` trùng `data_raw/images/train/guideline11__coco_000000274272.jpg`
  - `data2/000000577932.jpg` trùng `data/images/val/guideline11__coco_000000577932.jpg`. Nhãn của ảnh này vẫn được dùng, đã đưa vào `data/labels/val/guideline11__coco_000000577932.txt`.
- Đã loại `data2/000000423693.jpg` vì cảnh không có đối tượng nào thuộc 11 lớp.
- 117/117 ảnh còn lại đã được kiểm tra hash khớp với nguồn và đọc được header/trailer JPEG.

## Tên file

Mỗi thư mục trộn hai kiểu tên:

- Tên COCO gốc, ví dụ `000000138979.jpg`.
- Tên do người chia đặt lại theo lớp, ví dụ `bicycle21.jpg`, `truck11.jpg`, `bus15.jpg`. Tên này **không** phải nhãn; vẫn phải gán nhãn đầy đủ.

Không có tên file nào trùng giữa bốn thư mục, cũng không trùng với ảnh đã có trong `data_raw/images/`.

## Cách dùng

1. Mỗi thành viên nhận một thư mục, rà ảnh và gán nhãn theo guideline.
2. Khi duyệt xong, đưa cặp ảnh–nhãn sang [data/](../../data/README.md) theo tập train hoặc val, đổi tên ảnh theo quy ước `<nguồn>__<tên gốc>` nếu cần tránh trùng.
3. Giữ nguyên ảnh gốc trong thư mục này để còn đối chiếu.
