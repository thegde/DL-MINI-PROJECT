import os
import tensorflow as tf

PROJECT_PATH = os.getcwd()

models = {
    "Custom CNN": "results/custom_cnn_best.keras",
    "ResNet50": "results/resnet50_best.keras"
}

for name, relative_path in models.items():

    model_path = os.path.join(PROJECT_PATH, relative_path)

    print("\n" + "=" * 45)
    print(name)

    if not os.path.exists(model_path):
        print("Model file not found:", model_path)
        continue

    model = tf.keras.models.load_model(
        model_path,
        compile=False
    )

    total = model.count_params()

    trainable = sum(
        tf.keras.backend.count_params(w)
        for w in model.trainable_weights
    )

    non_trainable = total - trainable

    size_mb = os.path.getsize(model_path) / (1024 * 1024)

    print("Total parameters:", total)
    print("Trainable parameters:", trainable)
    print("Non-trainable parameters:", non_trainable)
    print("Model size:", round(size_mb, 2), "MB")
    