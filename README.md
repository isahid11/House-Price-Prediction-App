# House-Price-Prediction-App
A simple machine learning project to predict house prices using Random Forest and deploy it using Streamlit. Includes data analysis, feature importance, model training, and an interactive web app for predictions.


# 🏡 House Price Prediction using Machine Learning

This project is part of the SIG720 Task 5D submission. The goal is to build a machine learning model that predicts house prices based on property features, and deploy the model using a simple web app built with Streamlit.

---

## 📌 Project Overview

We use the **Paris Housing dataset** (from Kaggle) to train and evaluate multiple regression models. The final model (Random Forest Regressor) is saved and deployed using Streamlit to allow users to input features and get a predicted house price.

---

## 📂 Files in This Repository

- `app.py` – Streamlit app code for prediction
- `best_model.pkl` – Trained Random Forest model
- `requirements.txt` – List of Python packages needed
- `ParisHousing.csv` – Dataset used (optional if you're not uploading the CSV)
- `EDA_and_Modeling.ipynb` – Notebook with data analysis, model training, and feature importance

---

## 🚀 How to Run This App Locally

1. Clone the repo:
  git clone https://github.com/your-username/house-price-prediction.git
  cd house-price-prediction

2. Install dependencies:
  pip install -r requirements.txt

3. Run the Streamlit app:
  streamlit run app.py


**How to Deploy on Streamlit Cloud**
*Upload this repository to your GitHub account (make it public).*

-`Go to https://streamlit.io/cloud`

-`Click on “Deploy an App”.`

-`Connect your GitHub repo and select app.py as the main file.`

-`Wait for it to deploy and share your app link!`
