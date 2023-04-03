import tensorflow as tf
from keras import layers

from constants import *

class MultiLayerPerceptron(layers.Layer):
    def __init__(self, neurons, dropout_rate):
        super().__init__()
        self.dense_1 = layers.Dense(neurons, activation = tf.nn.gelu)
        self.dropout_1 = layers.Dropout(dropout_rate)
        self.dense_2 = layers.Dense(neurons, activation = tf.nn.gelu)
        self.dropout_2 = layers.Dropout(dropout_rate)

    def call(self, x):
        x = self.dense_1(x)
        x = self.dropout_1(x)
        x = self.dense_2(x)
        x = self.dropout_2(x)
        return x

class CutIntoPatches(layers.Layer):
    def __init__(self):
        super().__init__()

    def call(self, images):
        batch_size = tf.shape(images)[0]
        patches = tf.image.extract_patches(
            images=images,
            sizes=[1, PATCH_SIZE, PATCH_SIZE, 1],
            strides=[1, PATCH_SIZE, PATCH_SIZE, 1],
            rates=[1, 1, 1, 1],
            padding="VALID",
        )
        patch_dims = patches.shape[-1]
        patches = tf.reshape(patches, [batch_size, -1, patch_dims])
        return patches

class EncodePatchesIntoProjections(layers.Layer):
    def __init__(self):
        super().__init__()
        self.projection = layers.Dense(PROJECTION_DIMENSIONS)
        self.positional_embedding = layers.Embedding(
            input_dim=PATCHES_COUNT, output_dim=PROJECTION_DIMENSIONS #dim - max idx, not dimension size
        )

    def call(self, patch):
        positions = tf.range(start=0, limit=PATCHES_COUNT, delta=1)
        encoded = self.projection(patch) + self.positional_embedding(positions)
        return encoded


def  create_vit_classifier(input_shape, num_classes, data_augmentation):
    inputs = layers.Input(shape=input_shape)
    # Augment data.
    augmented = data_augmentation(inputs)
    # Create patches.
    patches = CutIntoPatches()(augmented)
    # Encode patches.
    encoded_patches = EncodePatchesIntoProjections()(patches)

    # Create multiple layers of the Transformer block.
    for _ in range(TRANSFORMER_LAYERS):
        # Layer normalization 1.
        x1 = layers.LayerNormalization(epsilon=1e-6)(encoded_patches)
        # Create a multi-head attention layer.
        attention_output =  layers.MultiHeadAttention(num_heads=HEADS_NUMBER, key_dim=PROJECTION_DIMENSIONS, dropout=DROPOUT_RATE)(x1, x1) # queries, (key-values)
        # Skip connection 1 -> Connect attention output to encoded patches.
        x2 = layers.Add()([attention_output, encoded_patches])

        # Layer normalization 2.
        x3 = layers.LayerNormalization(epsilon=1e-6)(x2)
        # Multi Layer Perceptron (Two Dense Layers with dropouts).
        x3 = MultiLayerPerceptron(TRANSFORMER_NEURONS_COUNT, DROPOUT_RATE)(x3)
        # Skip connection 2 -> Connect learned values to attention - updated encoded patches
        encoded_patches = layers.Add()([x3, x2])

    # Create a [batch_size, projection_dim] tensor.
    representation = layers.LayerNormalization(epsilon=1e-6)(encoded_patches)
    representation = layers.Flatten()(representation)
    representation = layers.Dropout(0.5)(representation)
    # Add MLP.
    features = MultiLayerPerceptron(CLASSIFIER_NEURONS_COUNT, 0.5)(representation)
    # Classify outputs.
    logits = layers.Dense(num_classes)(features)
    # Create the Keras model.
    model = tf.keras.Model(inputs=inputs, outputs=logits)
    return model