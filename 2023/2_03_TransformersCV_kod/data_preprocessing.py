import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt

from constants import *
from custom_layers import CutIntoPatches

def load_cifar100_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()

    print(f"x_train shape: {x_train.shape} - y_train shape: {y_train.shape}")
    print(f"x_test shape: {x_test.shape} - y_test shape: {y_test.shape}")

    num_classes = 100
    input_shape = (32, 32, 3)

    return (x_train, y_train), (x_test, y_test), input_shape, num_classes

def create_data_augmentation_model(x_train):
    data_augmentation = tf.keras.Sequential(
    [
        layers.Normalization(),
        layers.Resizing(TARGET_IMAGE_SIZE, TARGET_IMAGE_SIZE),
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(factor=0.02),
        layers.RandomZoom(
            height_factor=0.2, width_factor=0.2
        ),
    ],
    name="data_augmentation",
    )
    # Compute the mean and the variance of the training data for normalization
    data_augmentation.layers[0].adapt(x_train)

    return data_augmentation

def show_random_images(x_train, amount):
    plt.figure(figsize=(4, 4))
    n = int(np.sqrt(amount))

    for i in range(amount):
        image = x_train[np.random.choice(range(x_train.shape[0]))]
        ax = plt.subplot(n, n, i+1)
        plt.imshow(image)
        plt.axis("off")

    plt.show(block = True)

def show_patched_image(x_train):
    image = x_train[np.random.choice(range(x_train.shape[0]))]
    resized_image = tf.image.resize(
        tf.convert_to_tensor([image]), size=(TARGET_IMAGE_SIZE, TARGET_IMAGE_SIZE)
    )
    patches = CutIntoPatches()(resized_image)
    print(f"Image size: {TARGET_IMAGE_SIZE} X {TARGET_IMAGE_SIZE}")
    print(f"Patch size: {PATCH_SIZE} X {PATCH_SIZE}")
    print(f"Patches per image: {patches.shape[1]}")
    print(f"Elements per patch: {patches.shape[-1]}")

    n = int(np.sqrt(patches.shape[1]))
    plt.figure(figsize=(4, 4))
    for i, patch in enumerate(patches[0]):
        ax = plt.subplot(n, n, i + 1)
        patch_img = tf.reshape(patch, (PATCH_SIZE, PATCH_SIZE, 3))
        plt.imshow(patch_img.numpy().astype("uint8"))
        plt.axis("off")

    plt.show(block = True)

def noise_encoding():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(1000, 3, input_length=100))
    model.compile('rmsprop', 'mse')

    input_array = np.random.randint(1000, size=(1, 100))
    output_array = model.predict(input_array)[0, :, :]
    
    x = output_array[:, 0]
    y = output_array[:, 1]
    z = output_array[:, 2]

    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, zdir='z', c= 'red')
    plt.show(block = True)
