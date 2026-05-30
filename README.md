# 🎓 Student Performance Prediction System

An AI-powered Machine Learning project that predicts a student's final academic performance based on factors such as previous grades, study time, failures, and parental education.

## 🚀 Project Overview

This project uses the UCI Student Performance Dataset and Machine Learning algorithms to predict a student's final grade (G3). The application provides real-time predictions through an interactive Streamlit web interface.

## 📊 Features

* Data Analysis and Visualization
* Correlation Analysis
* Feature Selection
* Linear Regression Model
* Random Forest Model
* Feature Importance Analysis
* Real-Time Grade Prediction
* Performance Classification
* Interactive Streamlit Dashboard

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit

## 📂 Dataset

Dataset Source:

UCI Machine Learning Repository - Student Performance Dataset

Features Used:

* G1 (First Period Grade)
* G2 (Second Period Grade)
* Failures
* Study Time
* Mother Education (Medu)
* Father Education (Fedu)

Target:

* G3 (Final Grade)

## 🤖 Machine Learning Models

### Linear Regression

* R² Score: 0.78
* MAE: 1.28

### Random Forest Regressor

* R² Score: 0.80
* MAE: 1.33

Random Forest was selected as the final model because it achieved the highest prediction accuracy.

## 📈 Key Findings

* G2 (Second Period Grade) was the most important feature.
* Previous academic performance strongly influences final grades.
* Students with fewer failures tend to achieve better final results.
* Study time has a positive impact on academic performance.

## 🖥️ Streamlit Application

The application allows users to:

1. Enter student details
2. Predict final grade (G3)
3. View performance category

Performance Categories:

* Poor
* Average
* Good
* Excellent

## 📁 Project Structure

```text
student-performance-prediction/
│
├── dataset/
│   └── student-mat.csv
│
├── models/
│   └── model.pkl
│
├── app.py
├── eda.py
└── README.md
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

Run the application:

```bash
python -m streamlit run app.py
```

## 👨‍💻 Author

Divyanshu Jangir

Computer Science Engineering (AI & ML)

MBM University, Jodhpur

LinkedIn:
[www.linkedin.com/in/divyanshu-jangir-26ya24](http://www.linkedin.com/in/divyanshu-jangir-26ya24)

## ⭐ Future Improvements

* XGBoost Integration
* Model Hyperparameter Tuning
* Advanced Dashboard Analytics
* Cloud Deployment
* Student Performance Reports
