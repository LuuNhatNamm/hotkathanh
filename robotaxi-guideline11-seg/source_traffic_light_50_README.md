# traffic_light_50: 50 ảnh có đèn giao thông, nhãn YOLO-seg 11 lớp của cuộc thi

Nguồn: COCO val2017 (ảnh Flickr, giấy phép từng ảnh ở cột `license` của review.csv; nhãn COCO CC BY 4.0).
Ghi vào báo cáo cuộc thi: "public dataset COCO 2017, 50 ảnh chọn lọc, đã ánh xạ lại 11 lớp".

- images/    50 ảnh gốc
- labels/    nhãn YOLO-seg 11 lớp (`class x1 y1 ...`)
- previews/  ảnh vẽ nhãn để soát
- review.csv số instance mỗi lớp, cột `reviewed` để đánh dấu đã soát
- build_tl50.py  script đã sinh bộ này

Cách chuyển nhãn (tự động):
- car→Car, bus→Bus, truck→Truck, person→Pedestrian, traffic light→Traffic light, stop sign→Sign.
- Người ngồi trên motorcycle/bicycle (dò theo vị trí box) được gộp với xe thành MỘT instance Motorcyclist/Cyclist.
- Bỏ ảnh có vùng crowd hoặc có tàu hỏa; bỏ vật có cạnh ngắn < 1,25% cạnh dài ảnh hoặc < 64 px ở thang 640.
- Mask không chồng nhau: vật nhỏ hơn được coi là ở phía trước.

CẦN SỬA TAY trước khi dùng (mở bằng CVAT / Label Studio):
1. Sign: COCO chỉ có biển STOP. Các biển báo và biển chỉ dẫn khác trong ảnh chưa được gán → phải tự vẽ thêm.
2. Người ngồi trong ô tô, người trên áp phích: COCO có thể đã gán là person → xóa đi.
3. Gộp rider có thể sai khi người đứng sát xe → kiểm tra trong previews/.
4. Cột fragmented_instances > 0: vật bị che nặng, polygon có thể thiếu mảnh hoặc còn viền thừa quanh vật phía trước.
5. Polygon của COCO khá thô so với yêu cầu mAP@.95 → nên làm mịn lại bằng SAM.
