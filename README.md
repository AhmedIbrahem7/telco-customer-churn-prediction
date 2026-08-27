📊 Telco Customer Churn Prediction
📌 Project Overview

Customer churn is one of the key challenges for subscription-based businesses.

This project uses Machine Learning to predict whether a customer is likely to churn based on customer characteristics, service usage, contract information, and billing behavior.

The project follows an end-to-end Machine Learning workflow, starting from data preparation and exploratory data analysis, through model development and evaluation, and ending with an interactive Streamlit deployment.

🎯 Project Objectives

The main objectives of this project are:

Analyze customer characteristics and behavior.
Identify factors associated with customer churn.
Build and compare multiple Machine Learning classification models.
Select the best-performing model.
Tune the selected model using GridSearchCV.
Develop an interactive customer churn prediction application.
Provide business insights that can support customer retention strategies.
📂 Dataset

The project uses the Telco Customer Churn dataset.

Dataset Size
Customers: 7,043
Original Features: 21
Target Variable: Churn

The dataset contains information related to:

Customer demographics
Customer tenure
Services
Internet services
Contract type
Payment method
Monthly charges
Total charges
Churn status
🔄 Machine Learning Workflow

The project follows the following workflow:

Raw Dataset → Data Cleaning → Missing Value Handling → Exploratory Data Analysis → Feature Engineering → Categorical Encoding → Feature Scaling → Train/Test Split → Model Training → Model Evaluation → Hyperparameter Tuning → Final Logistic Regression Model → Model Serialization → Streamlit Deployment

🧹 Data Preparation

Several data preparation steps were performed before model development.

Missing Values

The TotalCharges column contained missing values represented as blank strings.

These values were converted to numeric format and missing values were handled during the data cleaning process.

Target Encoding

The Churn target variable was converted from No / Yes to 0 / 1.

⚙️ Feature Engineering

Two additional features were created.

TotalServices

Represents the number of additional services used by the customer.

AverageMonthlySpend

Calculated using:

TotalCharges / Tenure

This provides an estimate of the customer's average monthly spending.

🤖 Machine Learning Models

Multiple classification algorithms were evaluated during the project.

The main models compared were:

Logistic Regression
Gradient Boosting
Random Forest

Additional classification algorithms were also explored during the modeling phase.

📊 Model Performance

The models were evaluated using Accuracy, Precision, Recall, and F1 Score.

Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	80.62%	65.83%	56.15%	60.61%
Gradient Boosting	80.13%	66.21%	51.34%	57.83%
Random Forest	77.93%	60.98%	46.79%	52.95%
🏆 Selected Model

Logistic Regression

Logistic Regression was selected as the final model because it achieved the strongest overall performance among the compared models.

Final performance:

Accuracy: 80.62%
Precision: 65.83%
Recall: 56.15%
F1 Score: 60.61%
⚙️ Hyperparameter Tuning

GridSearchCV was used to optimize the Logistic Regression model.

The best parameter identified was:

C = 1

The tuned model achieved the same test-set performance as the original Logistic Regression model.

🔮 Streamlit Prediction Application

An interactive Streamlit application was developed to allow users to enter customer information and receive a churn prediction.

The application provides:

Churn Probability
Risk Level
Likely to Churn / Likely to Stay prediction
Model Performance
Business Insights
🚀 Live Application: https://telco-customer-churn-prediction-jpxvnuvjlrpeitg7qmcegi.streamlit.app/

💡 Business Insights

The analysis highlighted several important churn patterns.

Contract Type

Month-to-month customers generally show higher churn risk compared with customers on longer-term contracts.

Customer Tenure

Customers with shorter tenure tend to have a higher likelihood of churn.

Monthly Charges

Higher monthly charges can be associated with increased churn risk, particularly when combined with short tenure or month-to-month contracts.

Payment Method

Different payment methods can be associated with different churn patterns.

🎯 Recommended Business Actions
Target customers with high predicted churn risk.
Focus on retention during the early customer lifecycle.
Encourage customers to move to longer-term contracts.
Monitor high-value customers with higher monthly charges.
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Plotly
Streamlit
Jupyter Notebook
Git
GitHub
📁 Project Structure

telco-customer-churn-prediction/

├── app.py
├── churn_model_v2.pkl
├── requirements.txt
├── README.md
│
├── data/
│ └── Telco-Customer-Churn.csv
│
└── notebooks/
└── Telecom-Churn.ipynb

▶️ Run the Project Locally

Clone the repository:

git clone https://github.com/AhmedIbrahem7/telco-customer-churn-prediction.git

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

📌 Project Outcome

This project demonstrates a complete end-to-end Machine Learning workflow for customer churn prediction, from data preparation and exploratory analysis to model development, evaluation, deployment, and business recommendations.

The final solution can support proactive customer retention by identifying customers who may be at higher risk of churn.
