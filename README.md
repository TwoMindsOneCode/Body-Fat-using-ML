# **Body Fat and BMI Predictor**  

## **Overview**  
The **Body Fat Predictor** is a machine learning model built using the **Random Forest algorithm** to estimate body fat percentage based on various physical attributes such as weight, height, age, and other body measurements. This tool provides accurate predictions and classifies individuals into different body fat categories, including **Essential Fat, Athletes, Fitness, Average, and Obese**.  

## **Features**  
✅ Calculates **Body Mass Index (BMI)**  
✅ Predicts **Body Fat Percentage**  
✅ Categorizes individuals based on their **Body Fat Classification**  
✅ Uses **Random Forest** for reliable and accurate predictions  
✅ Supports multiple physical features for enhanced prediction accuracy  

## **Approach**  
1. **Dataset Preparation**  
   - The dataset includes **age, weight, height, and multiple body circumference measurements** (e.g., neck, chest, abdomen).  
2. **Preprocessing & Feature Engineering**  
   - Cleaning missing values  
   - Converting categorical variables like **sex** into numerical representations (0 for female, 1 for male)  
3. **Model Development**  
   - Trained using the **Random Forest algorithm** for robust performance on complex data  
   - Data augmentation techniques applied to improve accuracy  
4. **Performance Evaluation**  
   - Assessed using **Precision, Recall, and F1-Score**  
   - Successfully classifies individuals into different body fat categories  

## **How It Works**  
1. Enter the required body measurements into the input fields  
2. Click the **Predict** button  
3. View **BMI and Body Fat Percentage results** along with their classifications  

## **BMI Calculation**  
The **Body Mass Index (BMI)** is calculated using the formula:  

\[ BMI = \frac{Weight (kg)}{Height (m)^2} \]  

### **BMI Categories**  
- **Underweight**: BMI < 18.5  
- **Normal weight**: 18.5 ≤ BMI < 24.9  
- **Overweight**: 25 ≤ BMI < 29.9  
- **Obese**: BMI ≥ 30  

## **Demo Video**  
![Watch the Video](video.gif)

## **Installation**  
1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/body-fat-predictor.git
   cd body-fat-predictor
   ```  
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the application  
   ```bash
   python app.py
   ```  

## **Technologies Used**  
- **Python**  
- **Scikit-Learn** (Random Forest Algorithm)  
- **Flask/Streamlit** (for the UI)  
- **NumPy & Pandas** (for data processing)

## **Team**  
<img src="logo.png" width="40%"/>

## **License**  
📜 MIT License   
