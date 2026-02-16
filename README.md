# Rising-Waters-Flood-Prediction-Using-Machine-Learning-output
Flood Prediction Using Machine Learning is a web-based system that analyzes weather and rainfall data to predict flood risk. A Random Forest model is integrated with a Flask app to allow users to enter values and instantly view whether flood danger exists or not.
# 🌊 Flood Prediction Using Machine Learning (Flask Web App)

## 📌 Project Overview

This project is a Machine Learning based Flood Prediction System that predicts whether flood risk exists based on environmental and rainfall-related parameters.
The system uses a trained Random Forest model and a Flask web application to provide instant predictions through a user-friendly interface.

## 🚀 Features

* Predicts flood risk using Machine Learning
* Simple web interface for entering weather values
* Displays **High Flood Risk** or **No Flood Risk** result
* Trained using historical environmental dataset
* Flask-based backend with HTML/CSS frontend

## 🧠 Machine Learning Model

* Algorithm Used: Random Forest Classifier
* Dataset includes:

  * Temperature
  * Humidity
  * Cloud Cover
  * Annual Rainfall
  * Seasonal Rainfall Distribution

The trained model is saved as:

model.pkl

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* HTML
* CSS
* VS Code

## 📂 Project Structure

Flood-Prediction
│
├── app.py
├── train.py
├── model.pkl
├── dataset.xlsx
│
└── templates
    ├── home.html
    ├── index.html
    ├── chance.html
    └── nochance.html
    
## ▶️ How to Run the Project

### 1️⃣ Install dependencies

pip install flask pandas numpy scikit-learn

### 2️⃣ Train the model (if needed)

python train.py

### 3️⃣ Run Flask app

python app.py

### 4️⃣ Open browser

http://127.0.0.1:5000

## 📸 Output Screens

* Home Page
* Prediction Input Page
* High Flood Risk Page
* No Flood Risk Page

## 🎯 Project Purpose

This system demonstrates how Machine Learning can be applied to disaster management problems like flood prediction. It helps in early warning and supports decision-making for safety planning.

## 👨‍🎓 Developed For

SmartBridge Internship Project
Machine Learning Domain

## Developed by

M.Guruchaithanya kumari
