import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = tf.keras.models.load_model("fruit_model.h5")

test_path = "test_dataset"

test_datagen = ImageDataGenerator(rescale=1./255)

test_data = test_datagen.flow_from_directory(
    test_path,
    target_size=(100, 100),
    batch_size=16,
    class_mode='categorical',
    shuffle=False
)

loss, accuracy = model.evaluate(test_data)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy)
print("Test Accuracy (%):", accuracy * 100)