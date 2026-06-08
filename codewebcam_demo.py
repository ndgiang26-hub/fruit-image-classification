import cv2
import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model("fruit_model.h5")

classes = ["apple", "banana", "orange"]

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Khong mo duoc camera")
    exit()

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        h, w, _ = frame.shape

        # Khung vuông giữa màn hình
        size = 250

        x1 = w // 2 - size // 2
        y1 = h // 2 - size // 2

        x2 = x1 + size
        y2 = y1 + size

        # Cắt vùng trong khung
        roi = frame[y1:y2, x1:x2]

        # BGR -> RGB
        rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        # Resize đúng kích thước model
        img = cv2.resize(rgb_roi, (100, 100))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        # Dự đoán
        pred = model.predict(img, verbose=0)

        apple_p = pred[0][0] * 100
        banana_p = pred[0][1] * 100
        orange_p = pred[0][2] * 100

        index = np.argmax(pred)
        confidence = np.max(pred) * 100

        if confidence < 80:
            text1 = "Khong xac dinh"
        else:
            text1 = f"{classes[index]} {confidence:.1f}%"

        text2 = f"A:{apple_p:.0f}% B:{banana_p:.0f}% O:{orange_p:.0f}%"

        # Vẽ khung nhận diện
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            text1,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            text2,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Fruit AI", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
