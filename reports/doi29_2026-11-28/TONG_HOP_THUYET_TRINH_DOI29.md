# Tổng hợp cho bài thuyết trình — Đội 29 (Lưu Nhật Nam)

AIInAction RoboTaxi Data Centric Competition · YOLO26n-seg · 11 lớp · Điểm = 100 × √(mask mAP@50) · TEAM_ID 34

## 1. Kết quả chốt

| Chỉ số | Giá trị |
| --- | --- |
| Điểm public cao nhất của đội | **49,48** (run_398, nộp 10:23 28/11) |
| Thứ hạng public | **56 / 87 đội** (77 đội có điểm). Top 1: 61,62; top 10: 58,70 |
| Bài chọn tính private | 49,48 (run_398) và 48,49 (bài 09:50 của đội) |
| Số lượt đã nộp | 6 / 20 |
| Private | công bố sau 11:10, chưa có số |

Các bài đội đã nộp (điểm public):

| Giờ | Điểm | Nguồn |
| --- | ---: | --- |
| 09:21 | 47,06 | thành viên khác |
| 09:50 | **48,49** | thành viên khác (đã chọn private) |
| 09:57 | 47,13 | run_372 (Phú) |
| 10:16 | 45,76 | thành viên khác |
| 10:23 | **49,48** | run_398 (Phú, đã chọn private) |
| 10:36 | 46,75 | thành viên khác |

## 2. Lịch sử công việc (phần của Phú)

| Thời điểm | Việc | Kết quả |
| --- | --- | --- |
| 27/11 | Phần 1: dựng CVAT local (project 5), gán 87 ảnh (78 train, 9 val) bằng SAM3 + sửa tay theo guideline 11 lớp | train 1.288 nhãn, val 116 nhãn; polygon khớp mask CVAT IoU 0,934; PR #1 |
| 27/11 | Dọn nhãn: bỏ trùng (IoU ≥ 0,5), giải quyết chồng mask, bỏ bãi xe/kẹt xe quá dày, gộp Rider đúng cặp người–xe | 0 cặp trùng, 0 chồng đáng kể |
| 28/11 08:20 | Đồng bộ repo với main (đội gộp 4 phần, sửa 53 polygon tự cắt, thêm 70 ảnh Mini Traffic) | `data/` = 372 train / 26 val |
| 28/11 08:20–08:36 | Phần 1 đợt 2 (`chia_data/data1`, 30 ảnh): lọc 4 ảnh trùng md5, gán 26 ảnh mới trên CVAT task 78 | 234 đối tượng, IoU 0,931, 0 rò rỉ train/val; branch `Phu-1b` |
| 28/11 08:50–09:22 | run_372 trên Colab T4 | val 60,1 → nộp 47,13 |
| 28/11 10:04 | Push `Phu-1b` | GitHub `origin/Phu-1b` @ `6c02ac6` |
| 28/11 10:06–10:21 | run_398 trên Colab T4 | val 60,4 → nộp **49,48** |
| 28/11 10:33–~10:45 | run_398_aug (thử tham số) | dừng giữa chừng ở khoảng epoch 16/35, không có kết quả cuối |

## 3. Dữ liệu

| Nguồn (tiền tố) | Giấy phép | Ảnh train | Ảnh val |
| --- | --- | ---: | ---: |
| KITTI Semantic Instance Seg. 2015 (`kitti7__`) | CC BY-NC-SA 3.0 | 180 | 15 |
| Mini Traffic Detection, DatasetNinja (`minitraffic__`) | DbCL v1.0 | 70 (+13 ở run_398) | 0 |
| COCO val2017 (`guideline11__coco_`, `coco__`) | nhãn CC BY 4.0, ảnh Flickr | 45 (+13 ở run_398) | 4 |
| VisDrone (`cvat__VisDrone_`) | nghiên cứu (cần xác nhận) | 35 | 3 |
| Ảnh đội thu (`pending__dataset__`, `pending__xe_tho_so__`) | cần xác nhận | 22 | 2 |
| Zalo AI 2020 Traffic Sign (`vn_sign_30__`) | không ghi license | 20 | 2 |
| **Tổng** |  | **372 → 398** | **26** |

Quy trình: thu thập → lọc trùng (SHA-256, dHash, md5) → CVAT + SAM3 gán nháp → người sửa theo `labeling_guideline.md` → dọn trùng/chồng mask → export 1 polygon mỗi instance → kiểm tra bằng Bước 2 của notebook (0 polygon lỗi, 0 rò rỉ).

Phân bố lớp train (run_372): Car 2.391, Pedestrian 749, Sign 592, Traffic light 510, Motorcyclist 285, Motorcycle 238, Truck 141, Other vehicle 138, Bicycle 115, Cyclist 93, Bus 86. run_398 thêm: Car +56, Pedestrian +63, Sign +28, Traffic light +21, Bus +18, Bicycle +13, Cyclist +11, Truck +8, Other vehicle +8, Motorcycle +6, Motorcyclist +2.

## 4. Các lần chạy

| Lần | Dữ liệu | Tham số | Val mAP@50 | Val điểm | Test mAP@50 | Test điểm |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| run_372 | 372 / 5.338 đối tượng (main `4efc1ee`) | 60 epoch, batch 16, imgsz 640, mặc định | 0,3616 | 60,1 | 22,21 | 47,13 |
| run_398 | 398 / 5.572 (`Phu-1b` `6c02ac6`) | 45 epoch, còn lại như trên | 0,3650 | 60,4 | 24,48 | **49,48** |
| run_398_aug | 398 / 5.572 | 35 epoch + `copy_paste=0.3`, `mixup=0.1`, `cos_lr=True` | dừng ở ~epoch 16 (Ultralytics val mAP50 ≈ 0,23–0,25) | — | — | — |

Chung cho mọi lần: Colab Tesla T4, ultralytics 8.4.214, seed 34, `deterministic=True`, export ONNX opset 17 fp32, `submission.zip` ~9,2 MiB.

## 5. AP@50 từng lớp trên test public

| Lớp | run_372 | run_398 | Thay đổi |
| --- | ---: | ---: | ---: |
| Car | 50,17 | 49,95 | −0,2 |
| Motorcyclist | 40,97 | 40,29 | −0,7 |
| Cyclist | 33,97 | 40,74 | **+6,8** |
| Pedestrian | 25,68 | 28,65 | +3,0 |
| Truck | 27,59 | 25,53 | −2,1 |
| Traffic light | 21,32 | 24,06 | +2,7 |
| Motorcycle | 18,19 | 20,86 | +2,7 |
| Bicycle | 6,05 | 11,01 | **+5,0** |
| Bus | 9,16 | 10,81 | +1,7 |
| Sign | 10,91 | 10,05 | −0,9 |
| Other vehicle | 0,34 | 7,31 | **+7,0** |
| **mAP@50** | **22,21** | **24,48** | **+2,27** |

## 6. Bài học chính

1. **Thêm đúng dữ liệu cho lớp yếu có tác dụng thật:** chỉ 26 ảnh mới (+4% số ảnh) mà điểm test tăng 2,35, dù số epoch giảm từ 60 xuống 45. Ba lớp tăng mạnh nhất (Other vehicle, Cyclist, Bicycle) đúng là các lớp có trong ảnh mới.
2. **Val của đội không đại diện cho test:** val 60 điểm nhưng test 47–49 điểm. Val chỉ 26 ảnh, nhiều KITTI/COCO; test là đường Việt Nam. Các lớp Sign, Traffic light, Other vehicle tụt mạnh nhất từ val sang test.
3. **Lệch miền:** train chủ yếu KITTI (Đức) và COCO; test có xe máy dày đặc, ba gác, xích lô, biển báo Việt Nam. Sign (~10) và Other vehicle (~7) là hai lớp kéo điểm xuống nhiều nhất.
4. **Ảnh lỗi trên val:** 3/6 ảnh sai nhiều nhất là ảnh drone VisDrone (vật nhỏ, đông). Xe thô sơ Việt Nam bị nhầm lớp. Cảnh đêm bỏ sót nhiều, nhận nhầm mặt đồng hồ thành Sign.
5. **Quy trình gán nhãn:** SAM3 bỏ sót xe trắng/xám và xe ba bánh, nhận nhầm biển quảng cáo. Gộp người–xe theo bbox sai ở cảnh đông (một Rider nuốt 23 người), nên phải gộp theo mask chạm nhau, tối đa 2 người mỗi xe.

## 7. Hướng cải thiện tiếp

1. Thu thêm ảnh đường Việt Nam có ba gác/xe lam (Other vehicle), biển báo Việt Nam (Sign), xe buýt Việt Nam (Bus).
2. Gán nốt `chia_data/data2-4` (90 ảnh) cùng quy trình.
3. Làm lại val theo miền Việt Nam để chọn model đáng tin hơn.
4. Giảm KITTI gần trùng (23 cặp) và ảnh drone; cắt ảnh có hơn 100 đối tượng.
5. Sau khi dữ liệu ổn: thử 100 epoch, `copy_paste`, `cos_lr` (lượt thử bị dừng giữa chừng, chưa có kết luận).

## 8. Gợi ý dàn slide (10 slide)

1. **Bài toán & cách chấm:** 11 lớp, YOLO26n-seg cố định, điểm 100 × √mAP@50; kết quả 49,48, hạng public 56/87.
2. **Dữ liệu dùng:** bảng nguồn mục 3 (tên, giấy phép, số ảnh, ánh xạ lớp).
3. **Quy trình dữ liệu:** thu thập → lọc trùng → CVAT + SAM3 → sửa tay → dọn trùng/chồng → export → kiểm tra.
4. **Label guideline:** quy ước Rider (Motorcyclist/Cyclist), đầu kéo vs rơ-moóc, ngưỡng vật nhỏ, bỏ bãi xe quá dày.
5. **Duyệt nhãn:** lỗi SAM3 hay gặp và cách sửa; số liệu dọn nhãn.
6. **Phân bố lớp & cảnh báo:** bảng mục 3, Bus/Cyclist < 100, 778 vật < 64 px bị bỏ qua.
7. **Huấn luyện:** cấu hình mục 4.
8. **Vòng cải thiện:** run_372 → run_398, bảng mục 5 (+2,35 điểm nhờ 26 ảnh đúng lớp yếu).
9. **Phân tích lỗi:** khoảng cách val–test, lớp yếu, 6 ảnh lỗi (thư mục `anh_loi/`).
10. **Bài học & hướng tiếp:** mục 6 và 7.

Tệp kèm theo trong zip: `BAO_CAO_MODEL_DOI29.md` (báo cáo đầy đủ), `HANDOFF_DOI29_PHU_28-11.md`, `run_report.json` của hai lượt, `metrics.json`, đồ thị train (`train_log/`), ảnh lỗi (`anh_loi/`, `run_398/anh_loi/`).
