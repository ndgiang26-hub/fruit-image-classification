# PHÂN LOẠI TRÁI CÂY ỨNG DỤNG XỬ LÝ HÌNH ẢNH

## Giới thiệu

Project sử dụng mạng CNN để phân loại 3 loại trái cây:

- Apple
- Banana
- Orange

## Thư viện sử dụng

- Python
- TensorFlow/Keras
- NumPy

## Cấu trúc project

fruit_project/
 -train_fruit.py
 -test_fruit.py
 -evaluate_test.py
 -fruit_model.h5
 -dataset/

## Huấn luyện mô hình

Chạy:

python train_fruit.py

Sau khi huấn luyện xong sẽ tạo file:

fruit_model.h5

## Chạy demo

Đặt ảnh cần kiểm tra vào thư mục project.

Sửa:

img_path = "test.png"

Sau đó chạy:

python test_fruit.py

Kết quả:

Ket qua du doan: apple
Do tin cay: 100%

## Đánh giá mô hình

Chạy:

python evaluate_test.py

Kết quả:

Train Accuracy: 98.13%
Validation Accuracy: 99.47%
Test Accuracy: 99.05%
