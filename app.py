from flask import Flask, request, jsonify, send_from_directory
import os
import joblib

app = Flask(__name__)

model = joblib.load('random_forest_model.pkl')

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        sex = data['Sex']
        age = int(data['Age'])
        weight = float(data['Weight'])
        height = float(data['Height'])
        neck = float(data['Neck'])
        chest = float(data['Chest'])
        abdomen = float(data['Abdomen'])
        hip = float(data['Hip'])
        knee = float(data['Knee'])
        wrist = float(data['Wrist'])
    except ValueError:
        return jsonify({"error": "Invalid input, please enter valid numbers."}), 400

    sex_value = 1 if sex == 'Male' else 0

    bmi = weight / (height ** 2)  

    if bmi < 18.5:
        bmi_class = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_class = "Normal weight"
    elif 25 <= bmi < 29.9:
        bmi_class = "Overweight"
    else:
        bmi_class = "Obese"

    input_features = [sex_value, age, weight, height, neck, chest, abdomen, hip, knee, wrist]

    prediction = model.predict([input_features])
    body_fat = prediction[0]

    if sex == 'Male':
        if body_fat < 6:
            body_fat_class = "Essential fat"
        elif 6 <= body_fat < 14:
            body_fat_class = "Athletes"
        elif 14 <= body_fat < 18:
            body_fat_class = "Fitness"
        elif 18 <= body_fat < 25:
            body_fat_class = "Acceptable"
        else:
            body_fat_class = "Obese"
    else:  
        if body_fat < 14:
            body_fat_class = "Essential fat"
        elif 14 <= body_fat < 21:
            body_fat_class = "Athletes"
        elif 21 <= body_fat < 25:
            body_fat_class = "Fitness"
        elif 25 <= body_fat < 32:
            body_fat_class = "Acceptable"
        else:
            body_fat_class = "Obese"

    return jsonify({
        'bmi': round(bmi, 2),
        'bmi_class': bmi_class,
        'body_fat': round(body_fat, 2),
        'body_fat_class': body_fat_class
    })

@app.route('/<filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(debug=True)
