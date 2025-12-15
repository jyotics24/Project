# # Import necessary libraries
# from flask import Flask, request, jsonify, render_template  # Flask core components

# import joblib  # For loading the trained ML model

# # Initialize the Flask application
# app = Flask(__name__)

# # Load the trained model from the 'model.pkl' file
# model = joblib.load('model.pkl')

# # Define the route for the home page
# @app.route('/')
# def home():
#     return render_template('index.html')  # Render the HTML form (index.html)

# # Define the route for prediction, accepts only POST requests
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Mapping for categorical form input to numerical values
#         gender_map = {'Male': 1.0, 'Female': 0.0}
#         yes_no_map = {'Yes': 1.0, 'No': 0.0}

#         # Retrieve and convert form values to appropriate types
#         gender = gender_map[request.form['Gender']]  # Convert gender
#         age = float(request.form['Age'])  # Convert age input to float

#         smoker = yes_no_map[request.form['Smoker']]  # Smoker: Yes/No -> 1/0
#         bp_med = yes_no_map[request.form['BP_Med']]  # BP medication: Yes/No -> 1/0
#         p_stroke = yes_no_map[request.form['P_Stroke']]  # Previous stroke: Yes/No -> 1/0
#         hypertension = yes_no_map[request.form['Hypertension']]  # Hypertension: Yes/No -> 1/0
#         diabetes = yes_no_map[request.form['Diabetes']]  # Diabetes: Yes/No -> 1/0

#         # Retrieve numeric inputs and convert them to float
#         cholesterol = float(request.form['Cholesterol'])
#         systolic_bp = float(request.form['Systolic_Bp'])
#         bmi = float(request.form['BMI'])
#         heart_rate = float(request.form['Heart_rate'])
#         glucose = float(request.form['Glucose'])

#         # Create a list of inputs to feed into the model
#         data = [
#             gender, age, smoker, bp_med, p_stroke, hypertension,
#             diabetes, cholesterol, systolic_bp, bmi, heart_rate, glucose
#         ]

#         # Predict using the loaded model
#         prediction = model.predict([data])[0]  # Get the first (and only) prediction

#         # Interpret the result
#         if prediction == 1:
#             result = "You may have a risk of heart disease."
#         else:
#             result = "You are unlikely to have a risk of heart disease."

#         # Render the result on the result.html template
#         return render_template('result.html', prediction_text=result)

#     except Exception as e:
#         # If there is an error during prediction, return it as JSON
#         return jsonify({'error': str(e)})

# # Run the Flask app in debug mode (helpful during development)
# #if __name__ == '__main__':
# #    app.run(debug=True)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=80)
# Import necessary libraries
from flask import Flask, request, jsonify, render_template  # Flask core components
import joblib  # For loading the trained ML model

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model from the 'model.pkl' file
model = joblib.load('model.pkl')

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form (index.html)

# Define the route for prediction, accepts only POST requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Mapping for categorical form input to numerical values
        gender_map = {'Male': 1.0, 'Female': 0.0}
        yes_no_map = {'Yes': 1.0, 'No': 0.0}

        # Retrieve and convert form values to appropriate types
        gender = gender_map[request.form['Gender']]
        age = float(request.form['Age'])
        smoker = yes_no_map[request.form['Smoker']]
        bp_med = yes_no_map[request.form['BP_Med']]
        p_stroke = yes_no_map[request.form['P_Stroke']]
        hypertension = yes_no_map[request.form['Hypertension']]
        diabetes = yes_no_map[request.form['Diabetes']]
        cholesterol = float(request.form['Cholesterol'])
        systolic_bp = float(request.form['Systolic_Bp'])
        bmi = float(request.form['BMI'])
        heart_rate = float(request.form['Heart_rate'])
        glucose = float(request.form['Glucose'])

        # Create a list of inputs to feed into the model
        data = [
            gender, age, smoker, bp_med, p_stroke, hypertension,
            diabetes, cholesterol, systolic_bp, bmi, heart_rate, glucose
        ]

        # Predict using the loaded model
        prediction = model.predict([data])[0]

        # Interpret the result
        if prediction == 1:
            result = "You may have a risk of heart disease."
        else:
            result = "You are unlikely to have a risk of heart disease."

        # Render the result on the result.html template
        return render_template('result.html', prediction_text=result)

    except Exception as e:
        # If there is an error during prediction, return it as JSON
        return jsonify({'error': str(e)})

# Run the Flask app on port 5000 (non-privileged port)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
