# MNIST Handwritten Digit Recognition with Flask

## 📌 Project Overview
This project is a **handwritten digit recognition** web application built using **Flask** and a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. The user can draw a digit on a web-based canvas, and the trained model will predict the digit in real time.

## 🚀 Technologies Used
- **Python** (Flask for web backend)
- **TensorFlow & Keras** (for model training and inference)
- **NumPy** (for image processing)
- **Pillow (PIL)** (for image conversion)
- **HTML, CSS, JavaScript** (for front-end UI and canvas drawing)

## 📂 Project Structure
```
mnist_flask_app/
│── static/              # Static files (CSS, JS, images)
│── templates/           # HTML templates (index.html)
│── mnist_cnn_model.h5   # Pre-trained MNIST CNN model
│── app.py               # Flask backend
│── README.md            # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bektas-sari/mnist_flask_app.git
cd mnist_flask_app
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Application
```bash
python app.py
```

### 4️⃣ Open the Web Application
Go to **http://127.0.0.1:5000/** in your browser to start drawing digits and get predictions!

## 🎯 How It Works
1. **User draws a digit** on the canvas using the mouse.
2. **Canvas sends the image** to the Flask backend as a Base64-encoded PNG.
3. **Flask preprocesses the image** (grayscale, resizing, normalization).
4. **The trained CNN model predicts the digit**.
5. **The predicted number is displayed** on the webpage.


## 🤝 Contributing
Feel free to contribute by improving the model, enhancing UI, or optimizing the Flask backend! Open an issue or submit a PR.

## 📜 License
This project is open-source under the **MIT License**.

## Contact
Mail: bektas.sari@gmail.com
GitHub: bektas-sari



