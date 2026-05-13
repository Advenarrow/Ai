import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# Generate random data
X = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# Define Deep Model
model = Sequential([
    Dense(units=64, activation='relu', input_dim=100),
    Dense(units=64, activation='relu'),
    Dense(units=10, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Train and capture history for graphing
history = model.fit(X, one_hot_labels, epochs=15, batch_size=32, verbose=0)

# Plot accuracy over epochs
plt.plot(history.history['accuracy'])
plt.title('Deep Learning Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

# Evaluate
test_data = np.random.random((100, 100))
test_labels = np.random.randint(10, size=(100, 1))
test_one_hot_labels = keras.utils.to_categorical(test_labels, num_classes=10)
loss, acc = model.evaluate(test_data, test_one_hot_labels)
print(f"Deep Learning Model Test Accuracy: {acc*100:.2f}%")