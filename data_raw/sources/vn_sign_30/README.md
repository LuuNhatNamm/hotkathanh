# vn_sign_30: 30 ảnh dashcam đường phố Việt Nam có biển báo (lớp Sign = 9)

Nguồn: Zalo AI Challenge 2020, Traffic Sign Detection (bản trên Hugging Face: vtdung23/zalo-traffic-2020).
Mỗi ảnh lấy từ một tuyến đường khác nhau (street_id) để tránh các khung hình gần trùng nhau.
Box gốc được chuyển thành polygon: biển tròn thành ellipse 24 điểm nội tiếp box, biển "Nguy hiểm" thành tam giác.

CẦN SỬA TAY:
- Zalo chỉ gán biển cấm, biển nguy hiểm và biển hiệu lệnh. Biển chỉ dẫn xanh, biển phụ ("1000m", "CẤM ... TẤN") và
  cổng long môn chưa được gán → vẽ thêm với nhãn Sign.
- Zalo đôi khi gán biểu tượng tròn NẰM TRONG một tấm biển lớn (ví dụ bảng ZONE). Theo guideline, mask phải phủ cả mặt
  tấm biển → sửa lại thành một polygon cho cả tấm.
- Các lớp khác (xe máy, ô tô, người...) chưa có nhãn. Cần gán đủ trước khi train, nếu không mô hình sẽ học rằng xe là nền.
- Giấy phép: dữ liệu của cuộc thi Zalo, bản mirror không ghi license. Ghi rõ nguồn trong báo cáo.
