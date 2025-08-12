# Housing Price Prediction – Paris Dataset

A regression-based machine learning project to predict housing prices using the **Paris Housing Price Prediction** dataset from Kaggle. The project involves **EDA, feature importance analysis, model comparison, and deployment as a Streamlit web app**.

---

## 📌 Project Overview
This project is part of **SIG720 – Machine Learning (Task 5D)** at Deakin University.  
The objective is to **predict housing prices** based on various property features, evaluate multiple regression models, and build a user-friendly web tool for predictions.

---

## 📂 Dataset
- **Source:** https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction
- **Size:** ~10,000 rows × 16 features
- **Features include:** Square meters, number of rooms, city code, floors, hasYard, hasPool, attic, basement, garage, and more.

---

## 🔍 Workflow
1. **Data Preprocessing** – Handling data types, scaling, and preparing features.
2. **EDA** – Price distribution, suburb-wise comparison, correlation heatmap, outlier detection.
3. **Model Development** – Linear Regression, Random Forest, XGBoost with cross-validation.
4. **Performance Evaluation** – MAE, RMSE, R² metrics comparison.
5. **Feature Importance** – Model-based and SHAP value analysis.
6. **Deployment** – Streamlit web application for live predictions.

---

## 📊 Model Performance

| Model              | MAE       | RMSE      | R²       |
|--------------------|-----------|-----------|----------|
| Linear Regression  | 1480.97   | 1900.10   | 1.000000 |
| Random Forest      | 3096.67   | 3873.87   | 0.999998 |
| XGBoost            | 11816.84  | 14446.83  | 0.999975 |

---

## 🌟 Key Insights
- **Square Meters** is the most influential feature in predicting prices.
- Model-based and SHAP analyses strongly align in feature importance rankings.
- Linear Regression slightly outperformed others in terms of error metrics.

---

## 🚀 Deployment
- **Web App:** [Streamlit App Link](https://house-price-prediction-app-hppapp.streamlit.app/)
- Users can input property details to get an instant price prediction.

---

## 📚 References & Resources
- Kaggle Dataset: https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction
- Deakin University SIG720 Course Materials
- Google Machine Learning Documentation
- Scikit-learn Documentation: https://scikit-learn.org/stable/

---

## 📜 License
This project is licensed under the **MIT License** – see the LICENSE file for details.  
Dataset usage is subject to **Kaggle’s dataset terms**.
