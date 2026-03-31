# ❤️ Heart Disease Prediction Web Application

A Machine Learning-based web application built using Flask that predicts the risk of heart disease based on user health inputs. The model is trained on the Framingham Heart Study dataset and provides real-time predictions through a simple web interface.

---

## Features

- User-friendly web interface for input  
- Real-time heart disease risk prediction  
- Trained ML model using multiple algorithms  
- Clean and responsive UI  
- Docker support for easy deployment  

---

## Tech Stack

- Backend: Python, Flask  
- Machine Learning: scikit-learn, pandas, numpy  
- Frontend: HTML, CSS  
- Model Storage: joblib  
- Containerization: Docker  

---

## Project Structure

linux-scripting-project/

- app.py  
- heart_disease_predictor.py  
- model.pkl  
- requirements.txt  
- Dockerfile  
- README.md  

Data_set/
- framingham.csv  

static/
- style.css  

templates/
- index.html  
- result.html  

---

## Workflow

1. Train the Model  
   python heart_disease_predictor.py  

2. Run the Application  
   python app.py  

   Open: http://localhost:5000  

3. Use the Application  
   - Enter details  
   - Click Submit  
   - View result  

---

## Input Parameters

Gender, Age, Smoker, BP Medication, Previous Stroke, Hypertension, Diabetes, Cholesterol, Systolic BP, BMI, Heart Rate, Glucose  

---

## Prediction Output

- Low Risk: You are unlikely to have a risk of heart disease  
- High Risk: You may have a risk of heart disease  

---

## Docker

Build:
docker build -t heart-disease-app .

Run:
docker run -p 5000:5000 heart-disease-app

---

## Installation

pip install -r requirements.txt

---

## Note

Update dataset path if needed:
pd.read_csv("Data_set/framingham.csv")

---

## Author

Jyotiprakash Khuntia  
DevOps & Cloud Engineer  

---

## Support

If you like this project, give it a ⭐ on GitHub!