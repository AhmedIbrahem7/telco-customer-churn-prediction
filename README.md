# 📊 Telco Customer Churn Prediction

## 📌 Project Overview

Customer churn is one of the key challenges for subscription-based businesses.

This project uses Machine Learning to predict whether a customer is likely to churn based on customer characteristics, service usage, contract information, and billing behavior.

The project follows an end-to-end Machine Learning workflow, starting from data preparation and exploratory data analysis, through model development and evaluation, and ending with an interactive Streamlit deployment.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze customer characteristics and behavior.
- Identify factors associated with customer churn.
- Build and compare multiple Machine Learning classification models.
- Select the best-performing model.
- Tune the selected model using GridSearchCV.
- Develop an interactive customer churn prediction application.
- Provide business insights that can support customer retention strategies.

---

## 📂 Dataset

The project uses the Telco Customer Churn dataset.

### Dataset Size

- Customers: **7,043**
- Original Features: **21**
- Target Variable: **Churn**

The dataset contains information related to:

- Customer demographics
- Customer tenure
- Services
- Internet services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Churn status

---

## 🔄 Machine Learning Workflow

The project follows the following workflow:

```text
Raw Dataset
      ↓
Data Cleaning
      ↓
Missing Value Handling
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Categorical Encoding
      ↓
Feature Scaling
      ↓
Train / Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Final Logistic Regression Model
      ↓
Model Serialization
      ↓
Streamlit Deployment