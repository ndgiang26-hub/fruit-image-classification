# Phân Loại Trái Cây Sử Dụng Mạng CNN

## Giới thiệu

Đây là project xây dựng mô hình học máy sử dụng mạng nơ-ron tích chập (CNN) để phân loại hình ảnh trái cây thành 3 lớp:

* Táo (Apple)
* Chuối (Banana)
* Cam (Orange)

Mô hình được huấn luyện bằng TensorFlow/Keras và hỗ trợ nhận diện trực tiếp qua webcam theo thời gian thực.

---

## Yêu cầu

Cài đặt các thư viện cần thiết:

```bash
pip install tensorflow opencv-python numpy
```

---

## Cấu trúc thư mục

```text
fruit_project/
│
├── dataset/
│   ├── apple/
│   ├── banana/
│   └── orange/
│
├── test_dataset/
│   ├── apple/
│   ├── banana/
│   └── orange/
│
├── train_fruit.py
├── evaluate_test.py
├── webcam_laptop.py
├── fruit_model.h5
└── README.md
```

---

## Huấn luyện mô hình

Chạy file:

```bash
python train_fruit.py
```

Sau khi huấn luyện hoàn tất, mô hình sẽ được lưu thành:

```text
fruit_model.h5
```

---

## Đánh giá mô hình

Chạy file:

```bash
python evaluate_test.py
```

Ví dụ kết quả:

```text
Test Accuracy: 98.88%
```

---

## Nhận diện thời gian thực bằng Webcam

Chạy file:

```bash
python webcam_laptop.py
```

Phím điều khiển:

```text
ESC : Thoát chương trình
Q   : Thoát chương trình
```

Chương trình sẽ hiển thị:

* Loại trái cây được dự đoán
* Độ tin cậy dự đoán (%)
* Xác suất của từng lớp

Ví dụ:

```text
apple 98.3%
A:98% B:1% O:1%
```

Trong đó:

* A: Apple
* B: Banana
* O: Orange

---

## Tập dữ liệu

Tập dữ liệu gồm hơn 5000 ảnh trái cây thuộc 3 lớp:

* Apple
* Banana
* Orange

Ngoài các ảnh thu thập từ Internet, tập dữ liệu còn được bổ sung thêm ảnh thực tế do nhóm tự chụp với nhiều điều kiện khác nhau về:

* Góc chụp
* Ánh sáng
* Khoảng cách
* Màu nền

Việc bổ sung dữ liệu giúp tăng khả năng nhận diện trong môi trường thực tế.

---

## Kết quả thực nghiệm

| Thông số                  | Giá trị   |
| ------------------------- | --------- |
| Số lớp phân loại          | 3         |
| Kích thước ảnh            | 100 × 100 |
| Epoch huấn luyện          | 10        |
| Độ chính xác tập kiểm tra | 98.88%    |

Mô hình có khả năng nhận diện chính xác táo, chuối và cam thông qua webcam trong thời gian thực.

---

## Hướng phát triển

* Bổ sung thêm nhiều loại trái cây khác.
* Thu thập thêm dữ liệu thực tế.
* Nâng cấp mô hình bằng MobileNet hoặc EfficientNet.
* Triển khai trên thiết bị nhúng hoặc robot.
* Kết hợp với các mô hình phát hiện vật thể để nhận diện nhiều loại trái cây trong cùng một khung hình.

---

## Tác giả

Nguyễn Đức Giang

MSSV: 2421060167
