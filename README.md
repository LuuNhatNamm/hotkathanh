# Robotaxi · YOLO26n-seg

Mở [hướng dẫn HTML](huong-dan-robotaxi-yolo26.html) để xem sơ đồ use case và quy trình của nhóm.

| Vai trò | Đường dẫn | Việc làm |
| --- | --- | --- |
| Gán nhãn | [data_raw](data_raw/README.md) | Rà ảnh và nhãn tham khảo theo [guideline 11 lớp](labeling_guideline.md). Export cặp ảnh–nhãn đã duyệt sang data. |
| Huấn luyện | [data](data/README.md) và [notebook BTC](notebooks/train_and_export.ipynb) | Nạp dữ liệu đã duyệt, kiểm tra, train, đánh giá và tạo gói nộp. |
| Chạy demo | [demo](demo/README.md) | Dùng best.pt của nhóm để xuất video có mask. |
| Trưởng nhóm | [submission](submission/README.md) | Tập hợp submission.zip và run_report.json để bàn giao. |

Bộ data_raw ban đầu có **346 ảnh**, chia **311 train / 35 val**, gồm 39 ảnh CVAT chưa có nhãn và 30 ảnh vn_sign_30 có nhãn Sign một phần, cần rà và gán bổ sung. data/ có schema 11 lớp và chứa dữ liệu đã chuẩn bị cho huấn luyện. Các bộ cũ được lưu trong archive/ để đối chiếu.

## Chạy tiếp phần huấn luyện của đội

Đọc [hướng dẫn từng bước cho Đội 29](HUONG_DAN_TRAIN_COLAB_DOI29.md). Seed `TEAM_ID = 34`.

Bộ dữ liệu dùng để chạy hiện nằm trong `data/`, gồm **372 ảnh train / 5.338 đối tượng** và **26 ảnh val / 372 đối tượng**. Đã bổ sung 70 ảnh Mini Traffic Detection vào train và cập nhật nhãn đã rà. Phần phân công bên dưới lưu lại bộ ảnh gốc của nhóm.

Có thể clone repo ngay trong Colab và đặt `DATASET_PATH = "/content/hotkathanh/data"`. Hướng dẫn có sẵn ô lệnh clone, thứ tự chạy notebook, cấu hình và danh sách file cần bàn giao.

## Phân công gán nhãn

Mỗi thành viên nhận một phần. Ghi tên người phụ trách cạnh phần đã nhận. Danh sách bên dưới là đường dẫn ảnh tính từ thư mục gốc project.

| Phần | Tổng ảnh | Train | Val | Nhãn 11 lớp chờ rà | KITTI 7 lớp cần chuyển | Nhãn Sign một phần | Chưa có nhãn |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Phần 1 | 87 | 78 | 9 | 13 | 50 | 7 | 17 |
| Phần 2 | 87 | 78 | 9 | 13 | 50 | 7 | 17 |
| Phần 3 | 86 | 78 | 8 | 12 | 50 | 8 | 16 |
| Phần 4 | 86 | 77 | 9 | 12 | 50 | 8 | 16 |

- Dùng nhãn cùng tên gốc và cùng tập trong [data_raw/labels](data_raw/labels) làm tham khảo. Rà và bổ sung đủ lớp theo [guideline](labeling_guideline.md), kể cả với ảnh đã có nhãn.
- Các nhóm ảnh nghi gần trùng được giao cùng một người để giữ cách gán nhất quán.
- Sau khi duyệt, đưa ảnh và nhãn YOLO-seg 11 lớp vào [data/](data/README.md) theo tập train hoặc val đã ghi. Giữ nguyên tên gốc của ảnh.

<details>
<summary>Phần 1 · 87 ảnh</summary>

**train** (78 ảnh)

```text
data_raw/images/train/cvat__VisDrone_0000193_02029_d_0000114.jpg
data_raw/images/train/cvat__VisDrone_0000242_01475_d_0000007.jpg
data_raw/images/train/cvat__VisDrone_0000244_04000_d_0000009.jpg
data_raw/images/train/cvat__VisDrone_0000277_02001_d_0000549.jpg
data_raw/images/train/cvat__VisDrone_0000291_02201_d_0000879.jpg
data_raw/images/train/cvat__VisDrone_0000330_04201_d_0000821.jpg
data_raw/images/train/cvat__VisDrone_0000346_02549_d_0000359.jpg
data_raw/images/train/cvat__VisDrone_0000356_01569_d_0000637.jpg
data_raw/images/train/cvat__VisDrone_0000360_07057_d_0000749.jpg
data_raw/images/train/guideline11__coco_000000011197.jpg
data_raw/images/train/guideline11__coco_000000144706.jpg
data_raw/images/train/guideline11__coco_000000178982.jpg
data_raw/images/train/guideline11__coco_000000183246.jpg
data_raw/images/train/guideline11__coco_000000183709.jpg
data_raw/images/train/guideline11__coco_000000215723.jpg
data_raw/images/train/guideline11__coco_000000269942.jpg
data_raw/images/train/guideline11__coco_000000287291.jpg
data_raw/images/train/guideline11__coco_000000301376.jpg
data_raw/images/train/guideline11__coco_000000315450.jpg
data_raw/images/train/guideline11__coco_000000526392.jpg
data_raw/images/train/guideline11__coco_000000569030.jpg
data_raw/images/train/kitti7__000003_10.jpg
data_raw/images/train/kitti7__000004_10.jpg
data_raw/images/train/kitti7__000006_10.jpg
data_raw/images/train/kitti7__000009_10.jpg
data_raw/images/train/kitti7__000011_10.jpg
data_raw/images/train/kitti7__000014_10.jpg
data_raw/images/train/kitti7__000016_10.jpg
data_raw/images/train/kitti7__000023_10.jpg
data_raw/images/train/kitti7__000027_10.jpg
data_raw/images/train/kitti7__000034_10.jpg
data_raw/images/train/kitti7__000040_10.jpg
data_raw/images/train/kitti7__000041_10.jpg
data_raw/images/train/kitti7__000044_10.jpg
data_raw/images/train/kitti7__000053_10.jpg
data_raw/images/train/kitti7__000054_10.jpg
data_raw/images/train/kitti7__000058_10.jpg
data_raw/images/train/kitti7__000063_10.jpg
data_raw/images/train/kitti7__000068_10.jpg
data_raw/images/train/kitti7__000069_10.jpg
data_raw/images/train/kitti7__000082_10.jpg
data_raw/images/train/kitti7__000093_10.jpg
data_raw/images/train/kitti7__000098_10.jpg
data_raw/images/train/kitti7__000099_10.jpg
data_raw/images/train/kitti7__000102_10.jpg
data_raw/images/train/kitti7__000111_10.jpg
data_raw/images/train/kitti7__000112_10.jpg
data_raw/images/train/kitti7__000113_10.jpg
data_raw/images/train/kitti7__000114_10.jpg
data_raw/images/train/kitti7__000116_10.jpg
data_raw/images/train/kitti7__000127_10.jpg
data_raw/images/train/kitti7__000134_10.jpg
data_raw/images/train/kitti7__000137_10.jpg
data_raw/images/train/kitti7__000138_10.jpg
data_raw/images/train/kitti7__000140_10.jpg
data_raw/images/train/kitti7__000153_10.jpg
data_raw/images/train/kitti7__000156_10.jpg
data_raw/images/train/kitti7__000172_10.jpg
data_raw/images/train/kitti7__000180_10.jpg
data_raw/images/train/kitti7__000186_10.jpg
data_raw/images/train/kitti7__000187_10.jpg
data_raw/images/train/kitti7__000189_10.jpg
data_raw/images/train/kitti7__000191_10.jpg
data_raw/images/train/kitti7__000192_10.jpg
data_raw/images/train/kitti7__000195_10.jpg
data_raw/images/train/kitti7__000199_10.jpg
data_raw/images/train/pending__dataset__12.jpg
data_raw/images/train/pending__dataset__13.jpg
data_raw/images/train/pending__dataset__4.jpg
data_raw/images/train/pending__xe_tho_so__img_021.jpg
data_raw/images/train/pending__xe_tho_so__img_023.jpg
data_raw/images/train/pending__xe_tho_so__img_026.jpg
data_raw/images/train/vn_sign_30__zalo_1827.png
data_raw/images/train/vn_sign_30__zalo_1995.png
data_raw/images/train/vn_sign_30__zalo_5042.png
data_raw/images/train/vn_sign_30__zalo_6244.png
data_raw/images/train/vn_sign_30__zalo_758.png
data_raw/images/train/vn_sign_30__zalo_9000.png
```

**val** (9 ảnh)

```text
data_raw/images/val/cvat__VisDrone_0000335_03921_d_0000063.jpg
data_raw/images/val/guideline11__coco_000000157756.jpg
data_raw/images/val/kitti7__000028_10.jpg
data_raw/images/val/kitti7__000035_10.jpg
data_raw/images/val/kitti7__000136_10.jpg
data_raw/images/val/kitti7__000168_10.jpg
data_raw/images/val/kitti7__000188_10.jpg
data_raw/images/val/pending__dataset__2.jpg
data_raw/images/val/vn_sign_30__zalo_5259.png
```

</details>

<details>
<summary>Phần 2 · 87 ảnh</summary>

**train** (78 ảnh)

```text
data_raw/images/train/cvat__VisDrone_0000022_01036_d_0000006.jpg
data_raw/images/train/cvat__VisDrone_0000069_02163_d_0000006.jpg
data_raw/images/train/cvat__VisDrone_0000103_03349_d_0000031.jpg
data_raw/images/train/cvat__VisDrone_0000213_05745_d_0000247.jpg
data_raw/images/train/cvat__VisDrone_0000242_00001_d_0000001.jpg
data_raw/images/train/cvat__VisDrone_0000291_04201_d_0000889.jpg
data_raw/images/train/cvat__VisDrone_0000308_04401_d_0000327.jpg
data_raw/images/train/cvat__VisDrone_0000360_02941_d_0000728.jpg
data_raw/images/train/cvat__VisDrone_0000364_01765_d_0000782.jpg
data_raw/images/train/guideline11__coco_000000109441.jpg
data_raw/images/train/guideline11__coco_000000133819.jpg
data_raw/images/train/guideline11__coco_000000204871.jpg
data_raw/images/train/guideline11__coco_000000226417.jpg
data_raw/images/train/guideline11__coco_000000260266.jpg
data_raw/images/train/guideline11__coco_000000289222.jpg
data_raw/images/train/guideline11__coco_000000396200.jpg
data_raw/images/train/guideline11__coco_000000453841.jpg
data_raw/images/train/guideline11__coco_000000480944.jpg
data_raw/images/train/guideline11__coco_000000492077.jpg
data_raw/images/train/guideline11__coco_000000520009.jpg
data_raw/images/train/kitti7__000001_10.jpg
data_raw/images/train/kitti7__000005_10.jpg
data_raw/images/train/kitti7__000010_10.jpg
data_raw/images/train/kitti7__000018_10.jpg
data_raw/images/train/kitti7__000022_10.jpg
data_raw/images/train/kitti7__000024_10.jpg
data_raw/images/train/kitti7__000025_10.jpg
data_raw/images/train/kitti7__000030_10.jpg
data_raw/images/train/kitti7__000031_10.jpg
data_raw/images/train/kitti7__000032_10.jpg
data_raw/images/train/kitti7__000033_10.jpg
data_raw/images/train/kitti7__000037_10.jpg
data_raw/images/train/kitti7__000038_10.jpg
data_raw/images/train/kitti7__000049_10.jpg
data_raw/images/train/kitti7__000050_10.jpg
data_raw/images/train/kitti7__000052_10.jpg
data_raw/images/train/kitti7__000056_10.jpg
data_raw/images/train/kitti7__000060_10.jpg
data_raw/images/train/kitti7__000061_10.jpg
data_raw/images/train/kitti7__000064_10.jpg
data_raw/images/train/kitti7__000067_10.jpg
data_raw/images/train/kitti7__000071_10.jpg
data_raw/images/train/kitti7__000073_10.jpg
data_raw/images/train/kitti7__000076_10.jpg
data_raw/images/train/kitti7__000083_10.jpg
data_raw/images/train/kitti7__000089_10.jpg
data_raw/images/train/kitti7__000091_10.jpg
data_raw/images/train/kitti7__000092_10.jpg
data_raw/images/train/kitti7__000094_10.jpg
data_raw/images/train/kitti7__000096_10.jpg
data_raw/images/train/kitti7__000097_10.jpg
data_raw/images/train/kitti7__000109_10.jpg
data_raw/images/train/kitti7__000131_10.jpg
data_raw/images/train/kitti7__000143_10.jpg
data_raw/images/train/kitti7__000147_10.jpg
data_raw/images/train/kitti7__000149_10.jpg
data_raw/images/train/kitti7__000150_10.jpg
data_raw/images/train/kitti7__000158_10.jpg
data_raw/images/train/kitti7__000160_10.jpg
data_raw/images/train/kitti7__000165_10.jpg
data_raw/images/train/kitti7__000170_10.jpg
data_raw/images/train/kitti7__000181_10.jpg
data_raw/images/train/kitti7__000183_10.jpg
data_raw/images/train/kitti7__000190_10.jpg
data_raw/images/train/kitti7__000197_10.jpg
data_raw/images/train/pending__dataset__11.jpg
data_raw/images/train/pending__dataset__5.jpg
data_raw/images/train/pending__dataset__7.jpg
data_raw/images/train/pending__xe_tho_so__img_014.jpg
data_raw/images/train/pending__xe_tho_so__img_031.jpg
data_raw/images/train/pending__xe_tho_so__img_034.jpg
data_raw/images/train/vn_sign_30__zalo_1069.png
data_raw/images/train/vn_sign_30__zalo_12213.png
data_raw/images/train/vn_sign_30__zalo_3426.png
data_raw/images/train/vn_sign_30__zalo_4737.png
data_raw/images/train/vn_sign_30__zalo_4816.png
data_raw/images/train/vn_sign_30__zalo_698.png
data_raw/images/train/vn_sign_30__zalo_9576.png
```

**val** (9 ảnh)

```text
data_raw/images/val/cvat__VisDrone_0000276_04401_d_0000529.jpg
data_raw/images/val/guideline11__coco_000000198928.jpg
data_raw/images/val/guideline11__coco_000000467511.jpg
data_raw/images/val/kitti7__000013_10.jpg
data_raw/images/val/kitti7__000075_10.jpg
data_raw/images/val/kitti7__000078_10.jpg
data_raw/images/val/kitti7__000086_10.jpg
data_raw/images/val/kitti7__000110_10.jpg
data_raw/images/val/pending__xe_tho_so__img_006.jpg
```

</details>

<details>
<summary>Phần 3 · 86 ảnh</summary>

**train** (78 ảnh)

```text
data_raw/images/train/cvat__VisDrone_0000023_00868_d_0000010.jpg
data_raw/images/train/cvat__VisDrone_0000154_01601_d_0000001.jpg
data_raw/images/train/cvat__VisDrone_0000271_00201_d_0000375.jpg
data_raw/images/train/cvat__VisDrone_0000287_00801_d_0000763.jpg
data_raw/images/train/cvat__VisDrone_0000287_04801_d_0000781.jpg
data_raw/images/train/cvat__VisDrone_0000289_04601_d_0000834.jpg
data_raw/images/train/cvat__VisDrone_0000291_03601_d_0000886.jpg
data_raw/images/train/cvat__VisDrone_0000359_00785_d_0000703.jpg
data_raw/images/train/cvat__VisDrone_0000364_00589_d_0000798.jpg
data_raw/images/train/guideline11__coco_000000142585.jpg
data_raw/images/train/guideline11__coco_000000155451.jpg
data_raw/images/train/guideline11__coco_000000165039.jpg
data_raw/images/train/guideline11__coco_000000193717.jpg
data_raw/images/train/guideline11__coco_000000221754.jpg
data_raw/images/train/guideline11__coco_000000292997.jpg
data_raw/images/train/guideline11__coco_000000307074.jpg
data_raw/images/train/guideline11__coco_000000377946.jpg
data_raw/images/train/guideline11__coco_000000454661.jpg
data_raw/images/train/guideline11__coco_000000531134.jpg
data_raw/images/train/guideline11__coco_000000553511.jpg
data_raw/images/train/kitti7__000002_10.jpg
data_raw/images/train/kitti7__000007_10.jpg
data_raw/images/train/kitti7__000008_10.jpg
data_raw/images/train/kitti7__000015_10.jpg
data_raw/images/train/kitti7__000017_10.jpg
data_raw/images/train/kitti7__000026_10.jpg
data_raw/images/train/kitti7__000029_10.jpg
data_raw/images/train/kitti7__000042_10.jpg
data_raw/images/train/kitti7__000043_10.jpg
data_raw/images/train/kitti7__000045_10.jpg
data_raw/images/train/kitti7__000046_10.jpg
data_raw/images/train/kitti7__000047_10.jpg
data_raw/images/train/kitti7__000055_10.jpg
data_raw/images/train/kitti7__000057_10.jpg
data_raw/images/train/kitti7__000059_10.jpg
data_raw/images/train/kitti7__000072_10.jpg
data_raw/images/train/kitti7__000081_10.jpg
data_raw/images/train/kitti7__000084_10.jpg
data_raw/images/train/kitti7__000103_10.jpg
data_raw/images/train/kitti7__000104_10.jpg
data_raw/images/train/kitti7__000105_10.jpg
data_raw/images/train/kitti7__000106_10.jpg
data_raw/images/train/kitti7__000107_10.jpg
data_raw/images/train/kitti7__000115_10.jpg
data_raw/images/train/kitti7__000118_10.jpg
data_raw/images/train/kitti7__000119_10.jpg
data_raw/images/train/kitti7__000126_10.jpg
data_raw/images/train/kitti7__000130_10.jpg
data_raw/images/train/kitti7__000135_10.jpg
data_raw/images/train/kitti7__000142_10.jpg
data_raw/images/train/kitti7__000146_10.jpg
data_raw/images/train/kitti7__000148_10.jpg
data_raw/images/train/kitti7__000154_10.jpg
data_raw/images/train/kitti7__000159_10.jpg
data_raw/images/train/kitti7__000161_10.jpg
data_raw/images/train/kitti7__000164_10.jpg
data_raw/images/train/kitti7__000166_10.jpg
data_raw/images/train/kitti7__000169_10.jpg
data_raw/images/train/kitti7__000173_10.jpg
data_raw/images/train/kitti7__000176_10.jpg
data_raw/images/train/kitti7__000182_10.jpg
data_raw/images/train/kitti7__000185_10.jpg
data_raw/images/train/kitti7__000193_10.jpg
data_raw/images/train/kitti7__000194_10.jpg
data_raw/images/train/kitti7__000196_10.jpg
data_raw/images/train/pending__dataset__9.jpg
data_raw/images/train/pending__xe_tho_so__img_005.jpg
data_raw/images/train/pending__xe_tho_so__img_009.jpg
data_raw/images/train/pending__xe_tho_so__img_010.jpg
data_raw/images/train/pending__xe_tho_so__img_029.jpg
data_raw/images/train/pending__xe_tho_so__img_039.jpg
data_raw/images/train/vn_sign_30__zalo_10877.png
data_raw/images/train/vn_sign_30__zalo_11178.png
data_raw/images/train/vn_sign_30__zalo_254.png
data_raw/images/train/vn_sign_30__zalo_5025.png
data_raw/images/train/vn_sign_30__zalo_5046.png
data_raw/images/train/vn_sign_30__zalo_9309.png
data_raw/images/train/vn_sign_30__zalo_9530.png
```

**val** (8 ảnh)

```text
data_raw/images/val/cvat__VisDrone_0000280_00401_d_0000614.jpg
data_raw/images/val/guideline11__coco_000000354753.jpg
data_raw/images/val/kitti7__000065_10.jpg
data_raw/images/val/kitti7__000121_10.jpg
data_raw/images/val/kitti7__000151_10.jpg
data_raw/images/val/kitti7__000163_10.jpg
data_raw/images/val/kitti7__000175_10.jpg
data_raw/images/val/vn_sign_30__zalo_4692.png
```

</details>

<details>
<summary>Phần 4 · 86 ảnh</summary>

**train** (77 ảnh)

```text
data_raw/images/train/cvat__VisDrone_0000103_02964_d_0000030.jpg
data_raw/images/train/cvat__VisDrone_0000117_02708_d_0000090.jpg
data_raw/images/train/cvat__VisDrone_0000155_00001_d_0000001.jpg
data_raw/images/train/cvat__VisDrone_0000155_01871_d_0000001.jpg
data_raw/images/train/cvat__VisDrone_0000289_05201_d_0000837.jpg
data_raw/images/train/cvat__VisDrone_0000291_01601_d_0000876.jpg
data_raw/images/train/cvat__VisDrone_0000301_00001_d_0000156.jpg
data_raw/images/train/cvat__VisDrone_0000360_06665_d_0000747.jpg
data_raw/images/train/guideline11__coco_000000076417.jpg
data_raw/images/train/guideline11__coco_000000115946.jpg
data_raw/images/train/guideline11__coco_000000169996.jpg
data_raw/images/train/guideline11__coco_000000212573.jpg
data_raw/images/train/guideline11__coco_000000274272.jpg
data_raw/images/train/guideline11__coco_000000319607.jpg
data_raw/images/train/guideline11__coco_000000334371.jpg
data_raw/images/train/guideline11__coco_000000475484.jpg
data_raw/images/train/guideline11__coco_000000499181.jpg
data_raw/images/train/guideline11__coco_000000505942.jpg
data_raw/images/train/guideline11__coco_000000555050.jpg
data_raw/images/train/kitti7__000000_10.jpg
data_raw/images/train/kitti7__000012_10.jpg
data_raw/images/train/kitti7__000019_10.jpg
data_raw/images/train/kitti7__000020_10.jpg
data_raw/images/train/kitti7__000021_10.jpg
data_raw/images/train/kitti7__000036_10.jpg
data_raw/images/train/kitti7__000039_10.jpg
data_raw/images/train/kitti7__000048_10.jpg
data_raw/images/train/kitti7__000051_10.jpg
data_raw/images/train/kitti7__000062_10.jpg
data_raw/images/train/kitti7__000066_10.jpg
data_raw/images/train/kitti7__000070_10.jpg
data_raw/images/train/kitti7__000079_10.jpg
data_raw/images/train/kitti7__000080_10.jpg
data_raw/images/train/kitti7__000085_10.jpg
data_raw/images/train/kitti7__000087_10.jpg
data_raw/images/train/kitti7__000088_10.jpg
data_raw/images/train/kitti7__000090_10.jpg
data_raw/images/train/kitti7__000095_10.jpg
data_raw/images/train/kitti7__000100_10.jpg
data_raw/images/train/kitti7__000101_10.jpg
data_raw/images/train/kitti7__000120_10.jpg
data_raw/images/train/kitti7__000122_10.jpg
data_raw/images/train/kitti7__000123_10.jpg
data_raw/images/train/kitti7__000124_10.jpg
data_raw/images/train/kitti7__000125_10.jpg
data_raw/images/train/kitti7__000128_10.jpg
data_raw/images/train/kitti7__000129_10.jpg
data_raw/images/train/kitti7__000132_10.jpg
data_raw/images/train/kitti7__000133_10.jpg
data_raw/images/train/kitti7__000139_10.jpg
data_raw/images/train/kitti7__000141_10.jpg
data_raw/images/train/kitti7__000144_10.jpg
data_raw/images/train/kitti7__000145_10.jpg
data_raw/images/train/kitti7__000152_10.jpg
data_raw/images/train/kitti7__000155_10.jpg
data_raw/images/train/kitti7__000157_10.jpg
data_raw/images/train/kitti7__000167_10.jpg
data_raw/images/train/kitti7__000171_10.jpg
data_raw/images/train/kitti7__000174_10.jpg
data_raw/images/train/kitti7__000177_10.jpg
data_raw/images/train/kitti7__000178_10.jpg
data_raw/images/train/kitti7__000179_10.jpg
data_raw/images/train/kitti7__000184_10.jpg
data_raw/images/train/kitti7__000198_10.jpg
data_raw/images/train/pending__dataset__1.jpg
data_raw/images/train/pending__dataset__10.jpg
data_raw/images/train/pending__dataset__3.jpg
data_raw/images/train/pending__dataset__6.jpg
data_raw/images/train/pending__dataset__8.jpg
data_raw/images/train/pending__xe_tho_so__img_003.jpg
data_raw/images/train/vn_sign_30__zalo_10246.png
data_raw/images/train/vn_sign_30__zalo_10657.png
data_raw/images/train/vn_sign_30__zalo_12267.png
data_raw/images/train/vn_sign_30__zalo_6652.png
data_raw/images/train/vn_sign_30__zalo_86.png
data_raw/images/train/vn_sign_30__zalo_935.png
data_raw/images/train/vn_sign_30__zalo_9894.png
```

**val** (9 ảnh)

```text
data_raw/images/val/cvat__VisDrone_0000327_00601_d_0000714.jpg
data_raw/images/val/guideline11__coco_000000577932.jpg
data_raw/images/val/kitti7__000074_10.jpg
data_raw/images/val/kitti7__000077_10.jpg
data_raw/images/val/kitti7__000108_10.jpg
data_raw/images/val/kitti7__000117_10.jpg
data_raw/images/val/kitti7__000162_10.jpg
data_raw/images/val/pending__xe_tho_so__img_008.jpg
data_raw/images/val/vn_sign_30__zalo_9767.png
```

</details>
