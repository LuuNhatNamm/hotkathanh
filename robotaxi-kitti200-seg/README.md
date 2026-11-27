# KITTI 200 ảnh cho robotaxi

Dataset thử nghiệm cho **instance segmentation** với YOLO26n-seg. Nguồn là 200 ảnh camera trước bên trái có nhãn của [KITTI Semantic Instance Segmentation](https://www.cvlibs.net/datasets/kitti/eval_instance_seg.php?benchmark=instanceSeg2015).

| ID | Lớp |
| ---: | --- |
| 0 | `person` — người đi bộ |
| 1 | `rider` — người đang đi xe |
| 2 | `car` — ô tô |
| 3 | `truck` — xe tải |
| 4 | `bus` — xe buýt |
| 5 | `motorcycle` — xe máy |
| 6 | `bicycle` — xe đạp |

Dataset chia 160 ảnh train và 40 ảnh validation, lấy từ tập train công khai của KITTI. Phép chia theo ảnh dùng seed 243 và cân đối số ảnh có từng lớp. Tập validation phục vụ kiểm tra trong quá trình thử nghiệm. Tập test cho demo nên dùng video hoặc cảnh quay riêng từ môi trường mục tiêu.

Ảnh giữ nguyên độ phân giải và được nén JPEG ở mức chất lượng 92. Mỗi dòng nhãn chứa một ID lớp và các cặp tọa độ polygon chuẩn hóa. Khi chuyển mask, đường nối mảnh giữ các phần rời của cùng một đối tượng trong một polygon. Polygon ngoài có thể lấp các lỗ bên trong. Các vùng quá mảnh không tạo được polygon có diện tích dương được bỏ qua và ghi số lượng trong `stats.json`.

Dataset có 1.981 nhãn. Ô tô chiếm 1.678 nhãn, còn xe máy có 6 nhãn train và 1 nhãn validation. Nếu đề tài cần nhận diện xe máy, cần thêm ảnh gần với môi trường demo trước khi đánh giá lớp này.

Phạm vi nhãn là bảy lớp đối tượng trong bảng. Dataset thiếu nhãn làn đường, vùng chạy được, biển báo và đèn giao thông. `preview.jpg` minh họa polygon trên ảnh validation. `stats.json` chứa số lượng theo lớp và IoU đo mức khớp giữa polygon và mask gốc ở độ phân giải gốc.

## Chạy thử

Mở PowerShell ở thư mục `hackathon` và dùng Ultralytics có hỗ trợ YOLO26.

```powershell
$dataset = (Resolve-Path '.\robotaxi-kitti200-seg\data.yaml').Path
yolo segment train model=yolo26n-seg.pt data="$dataset" epochs=20 imgsz=640 batch=4 workers=0
```

Lệnh dùng trọng số COCO đã pretrain của Ultralytics để fine-tune trên ảnh giao thông. [Hướng dẫn YOLO26 instance segmentation](https://docs.ultralytics.com/tasks/segment/)

## Tạo lại dataset

```powershell
python .\robotaxi-kitti200-seg\prepare.py 'C:\duong-dan\data_semantics.zip'
```

Script cần NumPy và OpenCV. Tải `data_semantics.zip` từ trang benchmark KITTI.

## Nguồn và giấy phép

Ảnh và mask gốc thuộc KITTI Vision Benchmark Suite. Bản chuyển đổi sử dụng [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/), theo [điều khoản của KITTI](https://www.cvlibs.net/datasets/kitti/).

Trích dẫn theo benchmark: H. A. Alhaija, S. K. Mustikovela, L. Mescheder, A. Geiger và C. Rother. “Augmented Reality Meets Computer Vision: Efficient Data Generation for Urban Driving Scenes.” International Journal of Computer Vision, 2018.
