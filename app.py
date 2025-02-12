import base64
from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)

# 📌 **Load and compile the model**
model = load_model("mnist_cnn_model.h5", compile=False)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if "image" not in data:
            return jsonify({"error": "Image data not received!"}), 400

        # 📌 **Decode the Base64 encoded image**
        image_data = base64.b64decode(data["image"].split(",")[1])
        image = Image.open(io.BytesIO(image_data)).convert("L")  

        # 📌 **Resize the image to 28x28 pixels**
        image = image.resize((28, 28))

        # 📌 **Convert the image to a NumPy array**
        image_array = np.array(image)

        # 📌 **Invert colors (White Background = 0, Black Drawing = 1)**
        image_array = 255 - image_array

        # 📌 **Display raw image data in terminal**
        print("\n--- RAW IMAGE DATA ---")
        print(image_array[:5, :5]) 

        # 📌 **Normalize the image (0-1 range)**
        image_array = image_array.astype("float32") / 255.0  

        # 📌 **Reshape for the model input**
        image_array = image_array.reshape(1, 28, 28, 1)

        # 📌 **Make a prediction using the model**
        prediction = model.predict(image_array)
        predicted_label = int(np.argmax(prediction))

        return jsonify({"prediction": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)