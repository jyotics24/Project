# ❤️ Heart Disease Prediction Web App

A machine learning-powered web application that predicts the risk of heart disease based on user input. Built with **Python**, **Flask**, and a clean **HTML/CSS/JS** frontend.

---

## 🧠 Project Structure

```
heart_prediction_app/
├── save_model.py               # Train & save ML model
├── model/
│   └── model.pkl               # Saved trained model
├── backend/
│   └── app.py                  # Flask API
├── frontend/
│   ├── index.html              # Frontend form
│   └── style.css               # Styling
```

---

## 🔁 Workflow

### 1. Train and Save the Model

```bash
python save_model.py
```

- Loads and cleans data from `framingham.csv`
- Trains Logistic Regression model
- Saves `model.pkl` into `/model` folder

---

### 2. Start Flask API Server

```bash
python backend/app.py
```

- Loads the model
- Runs Flask API at `http://localhost:5000`
- Defines POST endpoint `/predict`

---

### 3. Open Frontend Form

- Open `frontend/index.html` in any browser
- Fill in user data
- Click "Predict" to get the result

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install flask flask-cors scikit-learn pandas numpy
```

---

## 🔗 API Endpoint

**POST** `/predict`\
Consumes: `application/json`\
Example input:

```json
{
  "male": 1,
  "age": 55,
  "smoker": 1,
  "bpmeds": 0,
  "prevalentStroke": 0,
  "prevalentHyp": 1,
  "diabetes": 0,
  "totChol": 233,
  "sysBP": 140,
  "BMI": 27.5,
  "heartRate": 85,
  "glucose": 85
}
```

Returns:

```json
{ "prediction": 1 }
```

---

## ⚙️ Technologies Used

- **Python**, **Flask**
- **scikit-learn**, **pandas**, **numpy**
- **HTML**, **CSS**, **JavaScript**
- **pickle** (for model saving)
- **flask-cors** (to allow cross-origin requests)

---

## 📌 Author

Developed by ** JYOTIPRAKASH KHUNTIA **\
Feel free to use and modify this project for learning or production!

---
