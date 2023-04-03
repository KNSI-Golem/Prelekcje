import tensorflow as tf
import tensorflow_addons as tfa
tf.get_logger().setLevel('ERROR')

from constants          import *
from custom_layers      import create_vit_classifier
from data_preprocessing import load_cifar100_data, create_data_augmentation_model, \
                                show_random_images, show_patched_image, noise_encoding

def run_experiment(model, x_train, y_train):
    optimizer = tfa.optimizers.AdamW(
        learning_rate=LEARNING_RATE, weight_decay=ADAMW_WEIGHT_DECAY
    )

    model.compile(
        optimizer=optimizer,
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[
            tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy"),
            tf.keras.metrics.SparseTopKCategoricalAccuracy(5, name="top-5-accuracy"),
        ],
    )

    checkpoint_filepath = "/tmp/checkpoint"
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        checkpoint_filepath,
        monitor="val_accuracy",
        save_best_only=True,
        save_weights_only=True,
    )

    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        validation_split=0.1,
        callbacks=[checkpoint_callback],
    )

    model.load_weights(checkpoint_filepath)
    _, accuracy, top_5_accuracy = model.evaluate(x_test, y_test)
    print(f"Test accuracy: {round(accuracy * 100, 2)}%")
    print(f"Test top 5 accuracy: {round(top_5_accuracy * 100, 2)}%")

    return history


if __name__ == "__main__":
    noise_encoding()
    (x_train, y_train), (x_test, y_test), input_shape, num_classes = load_cifar100_data()
    show_random_images(x_train, 4)
    show_patched_image(x_train)
    data_augmentation = create_data_augmentation_model(x_train)
    vit_classifier = create_vit_classifier(input_shape, num_classes, data_augmentation)
    vit_classifier.summary()
    history = run_experiment(vit_classifier, x_train, y_train)