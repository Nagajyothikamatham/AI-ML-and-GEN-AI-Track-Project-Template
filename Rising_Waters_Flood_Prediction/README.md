# 🌊 Rising Waters - AI Powered Flood Prediction System

## 📌 Project Overview

The Rising Waters Flood Prediction System is a Machine Learning web application that predicts the probability of flooding based on environmental and infrastructure-related factors.

The application is built using Python, Flask, Scikit-learn, HTML, and CSS. Users can enter different flood-related parameters, and the trained Random Forest model predicts the flood probability along with the corresponding risk level.

---

## 🎯 Features

- 🌊 Predict Flood Probability
- 🤖 Machine Learning Model (Random Forest)
- 📊 Risk Classification (Low, Moderate, High)
- 📈 Flood Probability Percentage
- 💡 Safety Advice
- 📅 Current Date & Time
- 🎨 Professional User Interface
- 📱 Responsive Design
- 🔄 Reset Button

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3

---

## 📂 Project Structure

```
Rising_Waters_Flood_Prediction/

├── app.py
├── train_model.py
├── README.md
├── requirements.txt

├── dataset/
│   └── flood.csv

├── model/
│   └── flood_model.pkl

├── templates/
│   └── index.html

└── static/
    └── style.css
```

---

## 🚀 Installation

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Rising_Waters_Flood_Prediction.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Open your browser

```
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Model

Algorithm Used:

**Random Forest Regressor**

Model Accuracy (R² Score):

**72.97%**

---

## 🌊 Prediction Output

The application predicts:

- Flood Probability (%)
- Flood Risk Level
- Safety Recommendation

---

## 🔮 Future Improvements

- Live Weather API Integration
- Interactive Maps
- Location-based Flood Prediction
- Historical Flood Data Visualization
- User Login System
- Prediction History

---

## 👩‍💻 Developer

**Nagajyothi Kamatham**
## Note

The trained model file (`model/flood_model.pkl`) is not included in this repository because it exceeds GitHub's web upload size limit.

To generate the model locally, run:

```bash
python train_model.py
```

This will automatically recreate the trained model.

B.Tech - Computer Science and Engineering

Machine Learning Internship Project

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
