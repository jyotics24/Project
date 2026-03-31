# ❤️ Heart Disease Prediction Web Application

A Machine Learning-based web application built using **Flask** that predicts the risk of heart disease based on user health inputs. The model is trained on the **Framingham Heart Study** dataset and provides real-time predictions through an intuitive web interface.

---

## 📌 Features

* **User-friendly UI:** Clean, responsive web interface for data entry  
* **Real-time Prediction:** Instant risk assessment using a pre-trained ML model  
* **Multi-Algorithm Evaluation:** Model selected based on comparative performance  
* **Dockerized Deployment:** Simplified setup and scaling using containerization  

---

## 🧠 Tech Stack

* **Backend:** Python, Flask  
* **Machine Learning:** scikit-learn, Pandas, NumPy  
* **Frontend:** HTML5, CSS3  
* **Model Serialization:** Joblib  
* **Containerization:** Docker  

---

---

## 📁 Project Structure

```text
.
├── app.py                      # Flask application (Web Server)
├── heart_disease_predictor.py  # Model training & evaluation script
├── model.pkl                   # Exported trained ML model
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container instructions
├── README.md                   # Project documentation
├── Data_set/
│   └── framingham.csv          # Source dataset
├── static/
│   └── style.css               # Frontend styling
└── templates/
    ├── index.html              # User input form
    └── result.html             # Prediction display page


---

## 🔄 Workflow

### 1. Model Training & Export

To retrain the model or update parameters, run:

python heart_disease_predictor.py

- Loads data  
- Handles missing values  
- Performs model comparison  
- Exports `model.pkl`  

---

### 2. Local Development

Install dependencies and run the app:

pip install -r requirements.txt  
python app.py  

Application will be available at:  
http://localhost:5000  

---

### 3. Usage

1. Open the application in browser  
2. Enter health details  
3. Submit form  
4. View prediction result  

---

## 📊 Model Information

The project evaluates several classification algorithms:

| Algorithm            | Status     | Reason |
|---------------------|-----------|--------|
| Logistic Regression | Selected  | Best balance of accuracy and interpretability |
| Decision Tree       | Evaluated | Prone to overfitting |
| SVM / KNN           | Evaluated | Computationally heavier |

---

## 🐳 Docker Deployment

Build the image:

docker build -t heart-disease-app .

Run the container:

docker run -p 5000:5000 heart-disease-app

---

## 🧾 Input Parameters

The model uses the following inputs:  
Gender, Age, Smoker status, BP Medication, Previous Stroke, Hypertension, Diabetes, Total Cholesterol, Systolic BP, BMI, Heart Rate, Glucose level  

---

## 👨‍💻 Author

Jyotiprakash Khuntia  
DevOps & Cloud Engineer  

---

## ⭐ Support

If this project helped you, please give it a ⭐ on GitHub!