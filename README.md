# ❤️ Heart Disease Prediction Web Application

A Machine Learning-based web application built using Flask that predicts the risk of heart disease based on user health inputs. The model is trained on the Framingham Heart Study dataset and provides real-time predictions through a simple web interface.

---

## 📌 Features

- User-friendly web interface for input  
- Real-time heart disease risk prediction  
- Trained ML model using multiple algorithms  
- Clean and responsive UI  
- Docker support for easy deployment  

---

## 🧠 Tech Stack

- Backend: Python, Flask  
- Machine Learning: scikit-learn, pandas, numpy  
- Frontend: HTML, CSS  
- Model Storage: joblib  
- Containerization: Docker  

---

## 📁 Project Structure

linux-scripting-project/
│
├── app.py                         # Flask application  
├── heart_disease_predictor.py     # Model training script  
├── model.pkl                      # Trained ML model  
├── requirements.txt               # Dependencies  
├── Dockerfile                     # Docker configuration  
├── README.md                      # Documentation  
│
├── Data_set/
│   └── framingham.csv             # Dataset  
│
├── static/
│   └── style.css                  # CSS styling  
│
├── templates/
│   ├── index.html                 # Input form  
│   └── result.html                # Result page  

---

## 🔄 Workflow

### 1. Train the Model

python heart_disease_predictor.py

- Loads dataset  
- Cleans missing values  
- Trains multiple models  
- Selects best model (Logistic Regression)  
- Saves model as model.pkl  

---

### 2. Run the Application

python app.py

Application will start at:

http://localhost:5000

---

### 3. Use the Application

- Open browser → http://localhost:5000  
- Fill in the required health details  
- Click Submit  
- View prediction result  

---

## 🧾 Input Parameters

- Gender  
- Age  
- Smoker  
- BP Medication  
- Previous Stroke  
- Hypertension  
- Diabetes  
- Cholesterol  
- Systolic BP  
- BMI  
- Heart Rate  
- Glucose  

---

## 🔮 Prediction Output

- Low Risk: You are unlikely to have a risk of heart disease  
- High Risk: You may have a risk of heart disease  

---

## 🐳 Docker Setup

### Build Docker Image

docker build -t heart-disease-app .

### Run Docker Container

docker run -p 5000:5000 heart-disease-app

Access the app at:

http://localhost:5000

---

## 📦 Installation

pip install -r requirements.txt

---

## ⚠️ Important Note

Update dataset path in heart_disease_predictor.py if needed:

pd.read_csv("Data_set/framingham.csv")

---

## 📊 Model Information

Models evaluated:
- Logistic Regression (Selected)  
- Decision Tree  
- Naive Bayes  
- KNN  
- SVM  

Evaluation Metric:
- Accuracy Score  

---

## 👨‍💻 Author

Jyotiprakash Khuntia  
DevOps & Cloud Engineer  

---

## ⭐ Support

If you found this project helpful, give it a ⭐ on GitHub!