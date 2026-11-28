# Báo cáo model — Đội 29 (Lưu Nhật Nam) — lượt run_372

Cuộc thi: AIInAction RoboTaxi Data Centric Competition (competition.antco.ai). Điểm = 100 × √(mask mAP@50). Hạn nộp 10:30 28/11/2026.

## 1. Cấu hình model và huấn luyện

| Mục | Giá trị |
| --- | --- |
| Kiến trúc | YOLO26n-seg (cố định theo cuộc thi), khởi tạo `yolo26n-seg.pt` pretrained COCO |
| Thư viện | ultralytics 8.4.214, onnx 1.23.2, onnxslim 0.1.99, onnxruntime 1.32.0 (bản ghim của notebook) |
| Notebook | `notebooks/train_and_export.ipynb` (NOTEBOOK_VERSION 3.0.0+7880385f), chạy trên Google Colab |
| GPU | Colab T4 |
| Seed / TEAM_ID | 34, `deterministic=True` |
| imgsz | 640 |
| Epoch / patience | 60/60 (chạy đủ, không dừng sớm), patience 20; 10 epoch cuối tắt mosaic |
| Thời gian train | khoảng 20 phút trên T4 (~20 s/epoch), GPU mem 6,6 GB |
| Batch | 16 |
| Tham số khác | mặc định của notebook (optimizer auto, augment mặc định Ultralytics, không sửa `TRAIN_ARGS`) |
| Export | ONNX `format="onnx", imgsz=640, batch=1, dynamic=False, simplify=True, opset=17`, fp32, không NMS |
| submission.zip | 9.672.243 byte (9,2 MiB), chỉ chứa `model.onnx` (10,6 MiB), sha256 `0663ed61edf6aafb75c3695f7c849b6c03f4787225ed0a5d9ad868a4ba251b79`; kiểm tra bằng mã hệ thống chấm: HỢP LỆ |
| Vân tay model | onnx sha256 `40c389a7…4094`, best.pt sha256 `c22a7df0…aae0` (đầy đủ trong `run_report.json`) |
| Môi trường Colab | Python 3.13.16, torch 2.14.1+cu130, numpy 2.4.6 |
| Dữ liệu | repo `LuuNhatNamm/hotkathanh`, `data/` tại main `4efc1ee` |

## 2. Dữ liệu

### 2.1 Số lượng (Bước 2 của notebook)

| Tập | Ảnh | Đối tượng | Ảnh rỗng |
| --- | ---: | ---: | ---: |
| Train | 372 | 5.338 | 0 |
| Val | 26 | 372 | 0 |

| id | Lớp | Train | Ảnh train | Val | Ảnh val | < 64 px |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | Car | 2391 | 300 | 211 | 22 | 331 |
| 1 | Bus | 86 | 56 | 3 | 2 | 7 |
| 2 | Truck | 141 | 86 | 12 | 7 | 18 |
| 3 | Other vehicle | 138 | 43 | 12 | 3 | 23 |
| 4 | Motorcycle | 238 | 56 | 9 | 2 | 18 |
| 5 | Motorcyclist | 285 | 63 | 23 | 6 | 42 |
| 6 | Bicycle | 115 | 44 | 8 | 5 | 2 |
| 7 | Cyclist | 93 | 48 | 9 | 4 | 12 |
| 8 | Pedestrian | 749 | 121 | 26 | 8 | 93 |
| 9 | Sign | 592 | 175 | 37 | 15 | 147 |
| 10 | Traffic light | 510 | 126 | 22 | 6 | 85 |

Cảnh báo của notebook:
- Ít ví dụ trong train (< 100): Bus (86), Cyclist (93).
- Val có < 10 đối tượng ở Bus (3), Motorcycle (9), Bicycle (8), Cyclist (9): AP các lớp này trên val dao động mạnh.
- 778 đối tượng < 64 px ở thang 640: hệ thống chấm bỏ qua.
- 5 ảnh có > 100 đối tượng (VisDrone, tối đa 152): hệ thống chấm chỉ giữ 100 dự đoán mỗi ảnh.
- 23 cặp ảnh gần giống (pHash ≤ 2), đều nằm cùng split (khung KITTI liền nhau). Không rò rỉ train/val.

### 2.2 Bộ dữ liệu công khai đã dùng

| Nguồn (tiền tố file) | Đường dẫn | Giấy phép | Train | Val | Ánh xạ về 11 lớp |
| --- | --- | --- | ---: | ---: | --- |
| KITTI Semantic Instance Segmentation 2015 (`kitti7__`) | https://www.cvlibs.net/datasets/kitti/eval_instance_seg.php?benchmark=instanceSeg2015 | CC BY-NC-SA 3.0 | 180 | 15 | person→Pedestrian, car→Car, truck→Truck, bus→Bus, motorcycle→Motorcycle, bicycle→Bicycle; rider gộp với xe thành Cyclist/Motorcyclist; vẽ thêm Sign, Traffic light |
| COCO val2017, tập con traffic_light_50 (`guideline11__coco_`) | https://cocodataset.org | Nhãn CC BY 4.0, ảnh Flickr theo license từng ảnh | 45 | 4 | Lớp COCO→11 lớp; polygon thô thay bằng mask SAM sát vật |
| VisDrone (`cvat__VisDrone_`) | https://github.com/VisDrone/VisDrone-Dataset | Dùng cho nghiên cứu (cần đội xác nhận) | 35 | 3 | Gán mới toàn bộ trên CVAT (SAM3 + sửa tay) |
| Zalo AI Challenge 2020 Traffic Sign (`vn_sign_30__`), mirror HF `vtdung23/zalo-traffic-2020` | https://huggingface.co/datasets/vtdung23/zalo-traffic-2020 | Không ghi license, ghi nguồn | 20 | 2 | Box biển → polygon; gán thêm các lớp còn thiếu |
| Mini Traffic Detection (`minitraffic__`) | https://datasetninja.com/mini-traffic-detection | DbCL v1.0 | 70 | 0 | car, bus, truck, motorcycle, bicycle, person, traffic_light → id tương ứng; 13 ảnh vẽ thêm người lái thành Cyclist/Motorcyclist |
| Ảnh chờ gán của đội (`pending__dataset__`, `pending__xe_tho_so__`) | — | Cần đội xác nhận nguồn | 22 | 2 | Gán mới 11 lớp |

### 2.3 Quy trình dữ liệu

1. Thu thập: gộp các nguồn trên, kiểm tra SHA-256 và dHash, giữ ảnh gần trùng cùng split.
2. Gán nhãn: chia 4 phần cho 4 thành viên, CVAT local, SAM3 tạo mask nháp, người sửa theo `labeling_guideline.md` (11 lớp).
3. Duyệt nhãn: dọn nhãn trùng (IoU ≥ 0.5 hoặc nằm ≥ 70% trong nhãn lớn), phần chồng nhau trả cho vật phía trước, bỏ bãi xe/kẹt xe quá dày, bỏ vật cạnh < 1,25% cạnh dài ảnh; gộp mỗi instance thành 1 polygon (IoU với mask CVAT trung bình 0,93).
4. Sửa hàng loạt trước khi train: 53 polygon tự cắt, 148 ID lớp trong 10 file, 320 annotation trùng trong một ảnh.
5. Bổ sung 70 ảnh Mini Traffic Detection vào train.
6. Kiểm tra bằng Bước 2 của notebook: 0 polygon lỗi, 0 rò rỉ train/val.

## 3. Kết quả

### 3.1 Trên val của đội (Bước 5, bộ chấm nhúng)

| Chỉ số | Giá trị |
| --- | ---: |
| mask mAP@50 | **0,3616** |
| Điểm theo công thức cuộc thi 100 × √(mAP@50) | **≈ 60,1** |
| mask mAP@[.5:.95] | 0,2082 (notebook in "điểm" 20,82 theo thang này) |
| Ảnh val | 26 |
| Thời gian suy luận p50 (ONNX, CPU, như máy chấm) | 219 ms/ảnh |

AP từng lớp (AP@50 là thước đo của cuộc thi; GT được chấm = sau khi bỏ 33 vật quá nhỏ):

| Lớp | AP@50 | AP@[.5:.95] | GT được chấm | Nhận xét |
| --- | ---: | ---: | ---: | --- |
| Motorcyclist | 0,758 | 0,431 | 17 | tốt |
| Car | 0,739 | 0,473 | 192 | tốt, lớp nhiều dữ liệu nhất |
| Traffic light | 0,715 | 0,358 | 22 | tốt |
| Sign | 0,497 | 0,348 | 31 | trung bình |
| Truck | 0,340 | 0,212 | 12 | trung bình |
| Cyclist | 0,316 | 0,211 | 9 | trung bình, val ít |
| Pedestrian | 0,300 | 0,104 | 25 | yếu, mask lệch biên nhiều |
| Other vehicle | 0,135 | 0,087 | 11 | yếu |
| Bicycle | 0,082 | 0,022 | 8 | rất yếu |
| Motorcycle | 0,049 | 0,013 | 9 | rất yếu |
| Bus | 0,048 | 0,034 | 3 | rất yếu, val chỉ 3 đối tượng nên nhiễu |

mAP@75 = 0,215. Model trả 2.582 dự đoán trên 26 ảnh (trung bình 99/ảnh, sát giới hạn 100 của máy chấm).

Diễn biến mask mAP@50 (validator Ultralytics) theo epoch: 0,21 (ep 5) → 0,27 (ep 17) → 0,28 (ep 34) → 0,29 (ep 50). Đường cong còn tăng nhẹ ở cuối, chưa bão hòa hẳn.

Lưu ý: `best.pt` được chọn theo val nên điểm val hơi lạc quan; val chỉ 26 ảnh, các lớp ít đối tượng dao động mạnh.

### 3.2 Trên hệ thống nộp bài (bộ test ẩn, public)

Nộp lúc 09:57 28/11/2026 (lượt thứ 3 của đội): **47,13 điểm** (mask mAP@50 = 22,21; mask mAP@[.5:.95] = 11,07, thang 0–100).

| Lớp | AP@50 test public (run_372) | AP@50 test public (bài 48,49 của đội) | AP@50 val (run_372) |
| --- | ---: | ---: | ---: |
| Car | 50,17 | 50,04 | 73,9 |
| Bus | 9,16 | 6,69 | 4,8 |
| Truck | 27,59 | 27,58 | 34,0 |
| Other vehicle | 0,34 | 0,20 | 13,5 |
| Motorcycle | 18,19 | 17,81 | 4,9 |
| Motorcyclist | 40,97 | 40,59 | 75,8 |
| Bicycle | 6,05 | 14,15 | 8,2 |
| Cyclist | 33,97 | 37,37 | 31,6 |
| Pedestrian | 25,68 | 26,48 | 30,0 |
| Sign | 10,91 | 12,20 | 49,7 |
| Traffic light | 21,32 | 25,56 | 71,5 |
| **mAP@50** | **22,21** | **23,52** | **36,16** |
| **Điểm 100 × √mAP@50** | **47,13** | **48,49** | **60,1** |

Các bài của đội trên bảng public: 47,06 (09:21), 48,49 (09:50), 47,13 (09:57, bài này). Đội đầu bảng lúc 08:20 đạt 61,62.

Nhận xét:
- Khoảng cách val → test rất lớn (36,2 → 22,2 mAP@50): val 26 ảnh của đội không đại diện cho test. Không nên chọn model chỉ dựa trên val hiện tại.
- Trên test, **Other vehicle gần như bằng 0** (0,34), **Sign** (10,9) và **Traffic light** (21,3) thấp hơn val rất nhiều: test có nhiều phương tiện kiểu Việt Nam (ba gác, xe lam, xích lô) và biển báo/đèn Việt Nam mà train hầu như không có.
- Bus, Bicycle, Motorcycle thấp ở cả val và test: thiếu dữ liệu.
- Car, Motorcyclist, Cyclist ổn định nhất.
- Chọn bài tính private: nếu không chọn, hệ thống lấy 2 bài chấm gần nhất (hiện là 47,13 và 48,49).

### 3.3 Phân tích lỗi

Bỏ sót (GT không có dự đoán khớp, ngưỡng tin cậy 0,25): Car 24, Sign 17, Pedestrian 17, Traffic light 10, Bicycle 8, Motorcycle 8, Truck 6, Other vehicle 5, Cyclist 5, Motorcyclist 2, Bus 2.

Nhầm lớp (thật → đoán): Truck → Car 3, Other vehicle → Bus 2, Other vehicle → Truck 2, Motorcyclist → Pedestrian 2, Other vehicle → Car 1, Cyclist → Motorcyclist 1, Cyclist → Pedestrian 1, Car → Truck 1, Bus → Car 1.

6 ảnh sai nhiều nhất (ảnh nhãn/dự đoán trong `colab_bundle/report/loi/`):

| Ảnh | GT | Dự đoán | Bỏ sót | Sai lớp | Dự đoán thừa |
| --- | ---: | ---: | ---: | ---: | ---: |
| cvat__VisDrone_0000276_04401_d_0000529 (drone) | 80 | 48 | 16 | 4 | 13 |
| cvat__VisDrone_0000335_03921_d_0000063 (drone) | 38 | 38 | 10 | 1 | 11 |
| cvat__VisDrone_0000280_00401_d_0000614 (drone) | 32 | 36 | 6 | 2 | 11 |
| pending__xe_tho_so__img_006 (xe thô sơ VN) | 13 | 19 | 3 | 3 | 12 |
| guideline11__coco_000000157756 (đêm) | 19 | 14 | 10 | 1 | 5 |
| vn_sign_30__zalo_5259 (biển báo VN) | 18 | 14 | 10 | 0 | 6 |

Nhận xét:
- Ảnh drone đông vật chiếm 3/6 ảnh lỗi: vật nhỏ, góc nhìn trên cao, dễ bỏ sót và nhận thừa.
- Xe thô sơ Việt Nam (ba gác, xe đẩy) bị nhầm lớp và nhận thừa: thiếu dữ liệu Other vehicle kiểu Việt Nam.
- Cảnh đêm: bỏ sót nhiều, nhận nhầm mặt đồng hồ tháp thành Sign.
- Biển báo Việt Nam nhỏ trong ảnh dashcam bị bỏ sót.

### 3.4 Lượt 2 — run_398 (thêm 26 ảnh Phần 1 đợt 2)

| Mục | run_372 | run_398 |
| --- | --- | --- |
| Dữ liệu | main `4efc1ee`: 372 train / 5.338 đối tượng | branch `Phu-1b` `6c02ac6`: 398 train / 5.572 đối tượng |
| Epoch | 60 | 45 (rút ngắn để kịp hạn nộp) |
| Batch / imgsz / seed | 16 / 640 / 34 | 16 / 640 / 34 |
| Val mask mAP@50 | 0,3616 | **0,3650** |
| Val 100 × √mAP@50 | 60,1 | **60,4** |
| Val mask mAP@[.5:.95] | 0,2082 | 0,2124 |
| submission.zip sha256 | `0663ed61…1b79` | `63a99f01…62c9` |
| Điểm public | 47,13 | **49,48** (cao nhất của đội) |

Điểm test public của run_398 (nộp 10:23): **49,48** (mask mAP@50 = 24,48; mAP@[.5:.95] = 13,18).

| Lớp | AP@50 test run_372 | AP@50 test run_398 | Chênh lệch |
| --- | ---: | ---: | ---: |
| Car | 50,17 | 49,95 | −0,2 |
| Bus | 9,16 | 10,81 | +1,7 |
| Truck | 27,59 | 25,53 | −2,1 |
| Other vehicle | 0,34 | 7,31 | **+7,0** |
| Motorcycle | 18,19 | 20,86 | +2,7 |
| Motorcyclist | 40,97 | 40,29 | −0,7 |
| Bicycle | 6,05 | 11,01 | **+5,0** |
| Cyclist | 33,97 | 40,74 | **+6,8** |
| Pedestrian | 25,68 | 28,65 | +3,0 |
| Sign | 10,91 | 10,05 | −0,9 |
| Traffic light | 21,32 | 24,06 | +2,7 |
| **mAP@50** | **22,21** | **24,48** | **+2,27** |
| **Điểm** | **47,13** | **49,48** | **+2,35** |

Kết luận: thêm 26 ảnh đúng lớp yếu (Bus, Other vehicle, Bicycle, Cyclist) tăng 2,35 điểm, dù số epoch giảm từ 60 xuống 45. Hướng data-centric có tác dụng thật trên test. Sign vẫn là lớp yếu nhất chưa được cải thiện.

Các bài đội đã nộp: 47,06 (09:21), 48,49 (09:50), 47,13 (09:57, run_372), 45,76 (10:16), **49,48 (10:23, run_398)**. Bài tính private đã chọn: 49,48 và 48,49.

AP@50 val từng lớp, run_372 → run_398: Bus 0,048 → **0,337**, Other vehicle 0,135 → **0,233**, Car 0,739 → 0,734, Motorcyclist 0,758 → 0,747, Traffic light 0,715 → 0,555, Sign 0,497 → 0,497, Truck 0,340 → 0,303, Cyclist 0,316 → 0,297, Pedestrian 0,300 → 0,264, Bicycle 0,082 → 0,028, Motorcycle 0,049 → 0,021.

Thêm 18 Bus và 8 Other vehicle trong 26 ảnh mới giúp rõ hai lớp này. Một số lớp giảm có thể do ít epoch hơn (45 so với 60) và do val các lớp này rất ít đối tượng. Lượt này đổi cùng lúc dữ liệu và số epoch, nên chưa tách được tác động riêng của từng thay đổi.

## 4. Dự đoán và hướng nâng điểm

### 4.1 Dự đoán

- Điểm val 60,1 so với test public 47,13: val lạc quan khoảng 13 điểm. Bộ test là cảnh giao thông Việt Nam (đề bài nhấn mạnh xe máy dày đặc, ba gác, xích lô, đêm, mưa), trong khi train chủ yếu là KITTI (Đức) và COCO.
- Theo AP@50 trên test, mỗi lớp góp 1/11 vào mAP. Kéo Other vehicle từ 0 lên khoảng 20, Sign từ 11 lên khoảng 30 và Bus từ 9 lên khoảng 25 sẽ nâng mAP@50 thêm khoảng 5 điểm, tức từ 22 lên 27. Khi đó điểm tăng từ khoảng 47 lên khoảng 52. Đây là ước lượng thô để ưu tiên việc, không phải cam kết.
- Thêm epoch hoặc đổi augmentation thường chỉ thay đổi 1–2 điểm (bài 47,06 / 48,49 / 47,13 của đội chênh nhau ít).

### 4.2 Xử lý dữ liệu (ưu tiên cao nhất, cuộc thi data-centric)

1. **Thêm cảnh đường Việt Nam**, ưu tiên theo điểm test thấp nhất: ba gác/xe lam/xích lô/xe công trình (Other vehicle, test 0,3), biển báo Việt Nam (Sign, test 10,9), xe buýt/xe khách Việt Nam (Bus, test 9,2), đèn giao thông Việt Nam (21,3), xe máy/xe đạp đỗ (Motorcycle 18,2, Bicycle 6,1). Hiện chỉ 43 ảnh train có Other vehicle và 56 ảnh có Motorcycle.
2. **Đưa 26 ảnh Phần 1 đợt 2 vào train** (đã gán xong trên branch `Phu-1b`, 234 đối tượng: Bus +18, Cyclist +11, Bicycle +13, Pedestrian +63). Bus và Cyclist sẽ vượt ngưỡng 100 đối tượng. Bỏ 3 ảnh không phải cảnh đường (`coco__000000102202`, `coco__000000124277`, `minitraffic__bicycle20`) trước khi gộp. Gán nốt `chia_data/data2-4` theo cùng quy trình.
3. **Giảm lệch miền:** KITTI chiếm 180/372 ảnh train và có 23 cặp khung liền nhau gần trùng. Giữ 1 ảnh mỗi cặp để dành chỗ cho ảnh Việt Nam.
4. **Ảnh drone VisDrone:** góc nhìn từ trên cao khác test. 5 ảnh có hơn 100 đối tượng, trong khi máy chấm chỉ giữ 100 dự đoán mỗi ảnh. Cắt nhỏ các ảnh này (tile) hoặc giảm số ảnh drone.
5. **Vật quá nhỏ:** 778 đối tượng dưới 64 px ở thang 640 bị máy chấm bỏ qua. Không tốn công gán thêm vật cỡ này; dồn công sức vào mask lớn và vừa.
6. **Thống nhất quy ước nhầm lẫn:** Motorcycle với Motorcyclist, Bicycle với Cyclist, Truck với Other vehicle (đầu kéo là Truck, rơ-moóc là Other vehicle). Rà chéo theo cặp hai người. Nhầm trong nhóm xe hai bánh chỉ bị phạt nửa điểm, nhưng bỏ sót thì mất trọn điểm.
7. **Tăng val cho lớp hiếm:** val chỉ có 3 Bus, 8 Bicycle, 9 Motorcycle, 9 Cyclist nên AP các lớp này rất nhiễu. Chuyển thêm vài ảnh có các lớp này sang val để so các lượt train cho đáng tin.
8. **Active learning:** chạy model hiện tại trên ảnh chưa gán, ưu tiên gán những ảnh model sai nhiều (ảnh lỗi ở Bước 5).

### 4.3 Tham số huấn luyện (thử sau khi dữ liệu đã ổn)

| Thay đổi | Lý do |
| --- | --- |
| `epochs=100`, `patience=30` | mAP còn tăng ở epoch 50–60; notebook gợi ý 60–100 epoch cho 300–1500 ảnh |
| `copy_paste=0.3` | augmentation riêng cho segmentation, nhân bản vật của lớp hiếm (Bus, Bicycle, Motorcycle) sang ảnh khác |
| `mixup=0.1`, `scale=0.5`, `fliplr=0.5` | đa dạng kích thước và bố cục, có lợi khi dữ liệu ít |
| `cos_lr=True`, `close_mosaic=10` | hội tụ ổn định hơn ở các epoch cuối |
| Giữ `imgsz=640`, `batch=16` | máy chấm chạy 640; T4 dùng 6,6 GB ở batch 16 |
| Lượt cuối: train trên train + val | thêm 26 ảnh cho bản nộp cuối, sau khi đã chọn được tham số |

Dự kiến: thay đổi tham số thường chỉ thêm 1–3 điểm; thêm dữ liệu đúng lớp yếu và đúng miền Việt Nam có tác động lớn hơn. Mỗi thay đổi nên chạy lại với cùng `TEAM_ID = 34` và so `run_report.json` trên cùng tập val.

## 5. Tệp kèm theo

| Tệp | Nội dung |
| --- | --- |
| `submission.zip` | bài nộp (model.onnx), sha256 `0663ed61…1b79` |
| `best.pt` | trọng số tốt nhất, để đánh giá lại hoặc train tiếp |
| `run_report.json` | bản kê tái lập của notebook (seed, hash dữ liệu, tham số, phiên bản, điểm val) |
| `metrics.json` | kết quả Bước 5 đầy đủ (AP từng lớp, nhầm lẫn, ảnh lỗi) |
| `train_log/` | `results.csv`, `results.png`, ma trận nhầm lẫn, đường PR mask, `args.yaml`, báo cáo dữ liệu Bước 2 |
| `anh_loi/` | 6 ảnh val sai nhiều nhất (trái: nhãn, phải: dự đoán) |
| `HANDOFF_DOI29_PHU_28-11.md` | bàn giao công việc và việc còn mở |
| `run_398/` | lượt 2: `submission.zip` (49,48 điểm), `best.pt`, `run_report.json`, `metrics.json`, `results.csv/png`, ảnh lỗi |
