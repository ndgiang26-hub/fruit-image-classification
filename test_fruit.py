import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model("fruit_model.h5")

img_path = "test.png"

img = image.load_img(img_path, target_size=(100, 100))
img = image.img_to_array(img)
img = img / 255.0
img = np.expand_dims(img, axis=0)

pred = model.predict(img)

classes = ["apple", "banana", "orange"]

index = np.argmax(pred)
confidence = np.max(pred) * 100

print("Ket qua du doan:", classes[index])
print("Do tin cay: %.2f%%" % confidence)