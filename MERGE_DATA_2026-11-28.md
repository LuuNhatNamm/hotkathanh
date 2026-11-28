# Hợp nhất các nhánh dữ liệu ngày 28/11/2026

`main` là nơi nhóm lấy bộ dữ liệu thống nhất. Các snapshot nhánh và nhãn còn cần rà nằm trong `data_raw/sources/branch_merge_2026-11-28/`.

## Bộ dùng để huấn luyện

| Split | Ảnh | TXT | Instance |
| --- | ---: | ---: | ---: |
| train | 404 | 404 | 5.544 |
| val | 50 | 50 | 641 |

Ảnh và nhãn đặt trực tiếp trong `data/images/{train,val}` và `data/labels/{train,val}`. Dùng `data/data.yaml`, giữ thứ tự 11 lớp. `data/split_manifest.json` ghi hash ảnh, hash nhãn và split của từng cặp.

## Các nhánh đã đối chiếu và gộp lịch sử

| Nhánh | Commit nguồn |
| --- | --- |
| `Phu-1` | `b8f1205` |
| `Phu-1b` | `6c02ac6` |
| `data/phan-2` | `586d661` |
| `vietanh` | `e2dfd12` |
| `data/extra-batch` | `3642a8c` |

Các thay đổi nội dung được đối chiếu và đưa vào cây dữ liệu thống nhất trước khi tạo merge commit. Merge giữ cây đã đối chiếu bằng chiến lược `ours`, đồng thời nối lịch sử của từng nhánh vào `main`. Không dùng snapshot cũ để ghi đè hàng loạt tập nhãn đã sửa.

## Quyết định khi gặp các phiên bản khác nhau

- Phần 1 và Phần 2 đã được hợp nhất và sửa nhãn trong các commit main trước đó. Giữ các bản sửa hiện tại khi nhánh thành viên mang lại bản cũ.
- `vietanh`: nhận 71 file nhãn train hợp lệ từ bản cập nhật mới. Hai file đã giống bản hiện tại. Năm file còn polygon lỗi theo notebook giữ nhãn main đã sửa; bản nhánh được lưu để rà tiếp.
- `Phu-1b`: đưa 20 cặp ảnh–nhãn mới vào train. Hai ảnh trùng/gần trùng giữ cặp hiện tại và split hiện tại. Bốn ảnh cần xác nhận ngữ cảnh hoặc lớp theo báo cáo của thành viên giữ trong raw: `coco__000000102202`, `coco__000000124277`, `coco__000000139507`, `minitraffic__bicycle20`.
- `data/extra-batch`: giữ quyết định QC trước đó cho bicycle7 và các ảnh chờ rà. Nhãn mới không được coi là hoàn chỉnh chỉ vì file TXT tồn tại. Bản nguồn và 118 ảnh raw bổ sung của nhánh có trong snapshot.
- Giữ nguyên ảnh và nhãn của val50 để cấu hình tuning và baseline còn so sánh trên cùng dữ liệu. Nhãn val khác giữa các nhánh được lưu trong raw để xem xét theo một phiên bản val mới riêng.

## Kiểm tra sau hợp nhất

- 0 cặp thiếu ảnh/nhãn, 0 nhãn mồ côi.
- 0 polygon lỗi theo hàm kiểm tra trong notebook BTC.
- 0 cặp ảnh trùng hệt trong dataset đang dùng.
- 0 cặp trùng/gần trùng giữa train và val theo hash ảnh, hash pixel RGB, pHash ≤ 2 hoặc dHash ≤ 2.
- 8 cặp gần giống trong cùng split được ghi trong báo cáo.
- Nội dung val50 giữ nguyên so với commit `637422e`; cấu hình khóa val vẫn áp dụng.

Kiểm tra hình học và trùng ảnh không xác nhận mọi instance đã đủ hoặc mọi đường viền đều chính xác về nội dung. Các nguồn chờ rà vẫn nằm trong raw.

## Đọc báo cáo và rà phần còn lại

- [Quyết định cho từng ảnh nguồn](data_raw/sources/branch_merge_2026-11-28/reconciliation.json).
- [Báo cáo QC toàn bộ dữ liệu](data_raw/sources/branch_merge_2026-11-28/qc_unified.json).
- [Quyết định guideline batch extra trước đó](data_raw/sources/extra_batch_remote/LOC_THEO_GUIDELINE.md).

Trong `reconciliation.json`, lọc các quyết định bắt đầu bằng `pending_` hoặc `keep_repaired_main_label_pending_geometry` để lấy danh sách cần sửa. Khi duyệt xong, đưa đúng cặp ảnh–nhãn vào `data/`, giữ tên và split đã thống nhất, chạy lại QC và cập nhật manifest.

Các điểm số trong slide và báo cáo run_372/run_398 thuộc những phiên bản thí nghiệm đó. Bộ 404/50 sau hợp nhất chưa có kết quả huấn luyện mới.
