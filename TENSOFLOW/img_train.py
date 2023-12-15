# pip install tensorflow

import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt


# Load data
dataset_name = 'cifar10'
(train_dataset, test_dataset), dataset_info = tfds.load(name=dataset_name,
													split=['train', 'test'],
													shuffle_files=True,
													with_info=True,
													as_supervised=True)


image, label = next(iter(train_dataset.take(1)))

plt.imshow(image)
plt.title(label.numpy())
plt.axis('off')
plt.show()


# Get the number of classes in the dataset
num_classes = dataset_info.features['label'].num_classes
num_classes


# Preprocess the data
def preprocess_data(image, label):
	# Convert image to float32 and normalize between 0 and 1
	image = tf.cast(image, tf.float32) / 255.0
	return image, label


# Apply preprocessing to the datasets
train_dataset = train_dataset.map(preprocess_data)
test_dataset = test_dataset.map(preprocess_data)


# Step 3: Build the model
input_dim = (32, 32, 3)

model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_dim),
	tf.keras.layers.MaxPooling2D((2, 2)),
	tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
	tf.keras.layers.MaxPooling2D((2, 2)),
	tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(64, activation='relu'),
	tf.keras.layers.Dense(num_classes, activation='softmax')
])
# Print the model summary
model.summary()


#sudo apt install graphviz  # For Ubuntu
#pip install pydot
