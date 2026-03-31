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

```bash
python heart_disease_predictor.py