import streamlit as st
import pandas as pd
import pickle
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD MODEL
# ============================================================

with open("churn_model_v2.pkl", "rb") as file:
    model = pickle.load(file)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Churn Analytics")

st.sidebar.caption(
    "Customer Churn Prediction"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Overview",
        "🔮 Churn Prediction",
        "📈 Model Performance",
        "💡 Business Insights"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Final Model\n\n"
    "Logistic Regression"
)


# ============================================================
# PAGE 1 — OVERVIEW
# ============================================================

if page == "🏠 Overview":

    st.title("📊 Customer Churn Analytics")

    st.write(
        "Machine Learning powered customer churn prediction "
        "and retention analysis."
    )

    st.divider()

    # --------------------------------------------------------
    # KPI SECTION
    # --------------------------------------------------------

    st.header("📌 Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Customers",
            "7,043"
        )

    with col2:
        st.metric(
            "Original Features",
            "21"
        )

    with col3:
        st.metric(
            "Features Used",
            "23"
        )

    with col4:
        st.metric(
            "Final Model",
            "Logistic Regression"
        )

    st.divider()

    # --------------------------------------------------------
    # PROJECT DESCRIPTION
    # --------------------------------------------------------

    st.header("🎯 Project Overview")

    st.write(
        """
        Customer churn is one of the key challenges for
        subscription-based businesses.

        This project uses **Machine Learning** to predict whether
        a customer is likely to churn based on customer characteristics,
        service usage, contract information, and billing behavior.

        The objective is to identify customers at risk and provide
        insights that can support proactive customer retention strategies.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # PROJECT OBJECTIVES
    # --------------------------------------------------------

    st.header("🎯 Project Objectives")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔍 Analyze")

        st.write(
            "Explore customer behavior and identify factors "
            "associated with customer churn."
        )

    with col2:
        st.subheader("🤖 Predict")

        st.write(
            "Build a machine learning model capable of predicting "
            "customer churn."
        )

    with col3:
        st.subheader("💡 Improve")

        st.write(
            "Provide insights that can support customer retention "
            "strategies."
        )

    st.divider()

    # --------------------------------------------------------
    # METHODOLOGY
    # --------------------------------------------------------

    st.header("🔬 Machine Learning Workflow")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("1️⃣ Data Preparation")

        st.write(
            "Data cleaning, missing value handling, data type "
            "correction, and removal of unnecessary columns."
        )

        st.subheader("2️⃣ Exploratory Data Analysis")

        st.write(
            "Customer characteristics and their relationship with "
            "churn were investigated using statistical analysis "
            "and visualizations."
        )

        st.subheader("3️⃣ Feature Engineering")

        st.write(
            "Additional features such as TotalServices and "
            "AverageMonthlySpend were created."
        )

    with col2:

        st.subheader("4️⃣ Model Development")

        st.write(
            "Multiple classification algorithms were tested "
            "and compared."
        )

        st.subheader("5️⃣ Hyperparameter Tuning")

        st.write(
            "GridSearchCV was used to identify the best "
            "Logistic Regression hyperparameter."
        )

        st.subheader("6️⃣ Model Evaluation")

        st.write(
            "Accuracy, Precision, Recall, F1 Score, and "
            "Confusion Matrix were used to evaluate the model."
        )


# ============================================================
# PAGE 2 — CHURN PREDICTION
# ============================================================

elif page == "🔮 Churn Prediction":

    st.title("🔮 Customer Churn Prediction")

    st.write(
        "Enter customer information below to estimate the "
        "customer's churn risk."
    )

    st.divider()

    # --------------------------------------------------------
    # CUSTOMER INFORMATION
    # --------------------------------------------------------

    st.header("👤 Customer Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

    with col2:

        senior_citizen = st.selectbox(
            "Senior Citizen",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

    with col3:

        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0,
            max_value=100,
            value=12
        )

    col1, col2 = st.columns(2)

    with col1:

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

    with col2:

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

    st.divider()

    # --------------------------------------------------------
    # SERVICE & CONTRACT
    # --------------------------------------------------------

    st.header("📡 Service & Contract Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

    with col2:

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

    with col3:

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.divider()

    # --------------------------------------------------------
    # BILLING INFORMATION
    # --------------------------------------------------------

    st.header("💰 Billing Information")

    col1, col2 = st.columns(2)

    with col1:

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=50.0,
            step=1.0
        )

    with col2:

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=500.0,
            step=10.0
        )

    # --------------------------------------------------------
    # DEFAULT FEATURES
    # --------------------------------------------------------

    phone_service = "Yes"

    multiple_lines = "No"

    paperless_billing = "Yes"

    online_security = "No"

    online_backup = "No"

    device_protection = "No"

    tech_support = "No"

    streaming_tv = "No"

    streaming_movies = "No"

    # --------------------------------------------------------
    # FEATURE ENGINEERING
    # --------------------------------------------------------

    total_services = 0

    if online_security == "Yes":
        total_services += 1

    if online_backup == "Yes":
        total_services += 1

    if device_protection == "Yes":
        total_services += 1

    if tech_support == "Yes":
        total_services += 1

    if streaming_tv == "Yes":
        total_services += 1

    if streaming_movies == "Yes":
        total_services += 1

    if tenure > 0:

        average_monthly_spend = total_charges / tenure

    else:

        average_monthly_spend = monthly_charges

    st.divider()

    # --------------------------------------------------------
    # PREDICTION BUTTON
    # --------------------------------------------------------

    predict_button = st.button(
        "🔮 Predict Churn Risk",
        use_container_width=True
    )

    if predict_button:

        # ----------------------------------------------------
        # INPUT DATA
        # ----------------------------------------------------

        input_data = pd.DataFrame({
            "gender": [gender],
            "SeniorCitizen": [senior_citizen],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone_service],
            "MultipleLines": [multiple_lines],
            "InternetService": [internet_service],
            "OnlineSecurity": [online_security],
            "OnlineBackup": [online_backup],
            "DeviceProtection": [device_protection],
            "TechSupport": [tech_support],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
            "Contract": [contract],
            "PaperlessBilling": [paperless_billing],
            "PaymentMethod": [payment_method],
            "MonthlyCharges": [monthly_charges],
            "TotalCharges": [total_charges],
            "TotalServices": [total_services],
            "AverageMonthlySpend": [average_monthly_spend]
        })

        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        # ----------------------------------------------------
        # RISK LEVEL
        # ----------------------------------------------------

        if probability < 0.30:

            risk_level = "Low Risk"

        elif probability < 0.60:

            risk_level = "Medium Risk"

        else:

            risk_level = "High Risk"

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.header("📊 Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Churn Probability",
                f"{probability:.1%}"
            )

        with col2:

            st.metric(
                "Risk Level",
                risk_level
            )

        with col3:

            if prediction == 1:

                st.metric(
                    "Prediction",
                    "Likely to Churn"
                )

            else:

                st.metric(
                    "Prediction",
                    "Likely to Stay"
                )

        # ----------------------------------------------------
        # RISK BAR
        # ----------------------------------------------------

        st.write("### Churn Risk Score")

        st.progress(
            probability,
            text=f"Churn Probability: {probability:.1%}"
        )

        # ----------------------------------------------------
        # RESULT MESSAGE
        # ----------------------------------------------------

        if prediction == 1:

            st.error(
                "⚠️ The model predicts that this customer "
                "is likely to churn."
            )

        else:

            st.success(
                "✅ The model predicts that this customer "
                "is likely to stay."
            )


# ============================================================
# PAGE 3 — MODEL PERFORMANCE
# ============================================================

elif page == "📈 Model Performance":

    st.title("📈 Model Performance")

    st.write(
        "Evaluation and comparison of the machine learning "
        "models tested during the project."
    )

    st.divider()

    # --------------------------------------------------------
    # MODEL RESULTS
    # --------------------------------------------------------

    model_results = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Gradient Boosting",
            "Random Forest"
        ],
        "Accuracy": [
            0.806246,
            0.801278,
            0.779276
        ],
        "Precision": [
            0.658307,
            0.662069,
            0.609756
        ],
        "Recall": [
            0.561497,
            0.513369,
            0.467914
        ],
        "F1 Score": [
            0.606061,
            0.578313,
            0.529501
        ]
    })

    # --------------------------------------------------------
    # SELECTED MODEL
    # --------------------------------------------------------

    st.header("🏆 Selected Model")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "Logistic Regression"
        )

        st.write(
            "Logistic Regression was selected as the final model "
            "because it achieved the strongest overall performance "
            "among the tested models."
        )

    with col2:

        st.info(
            "Best Hyperparameter: C = 1"
        )

        st.write(
            "GridSearchCV identified C = 1 as the best "
            "Logistic Regression hyperparameter."
        )

    st.divider()

    # --------------------------------------------------------
    # PERFORMANCE METRICS
    # --------------------------------------------------------

    st.header("📊 Performance Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Accuracy",
            "80.62%"
        )

    with col2:

        st.metric(
            "Precision",
            "65.83%"
        )

    with col3:

        st.metric(
            "Recall",
            "56.15%"
        )

    with col4:

        st.metric(
            "F1 Score",
            "60.61%"
        )

    st.divider()

    # --------------------------------------------------------
    # MODEL COMPARISON TABLE
    # --------------------------------------------------------

    st.header("📋 Model Comparison")

    display_results = model_results.copy()

    display_results["Accuracy"] = (
        display_results["Accuracy"] * 100
    ).round(2).astype(str) + "%"

    display_results["Precision"] = (
        display_results["Precision"] * 100
    ).round(2).astype(str) + "%"

    display_results["Recall"] = (
        display_results["Recall"] * 100
    ).round(2).astype(str) + "%"

    display_results["F1 Score"] = (
        display_results["F1 Score"] * 100
    ).round(2).astype(str) + "%"

    st.dataframe(
        display_results,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------------
    # MODEL COMPARISON CHART
    # --------------------------------------------------------

    st.header("📈 Model Comparison")

    chart_data = model_results.melt(
        id_vars="Model",
        var_name="Metric",
        value_name="Score"
    )

    fig = px.bar(
        chart_data,
        x="Model",
        y="Score",
        color="Metric",
        barmode="group",
        text_auto=".1%",
        title="Machine Learning Model Comparison"
    )

    fig.update_yaxes(
        tickformat=".0%",
        range=[0, 1]
    )

    fig.update_layout(
        height=500,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # HYPERPARAMETER TUNING
    # --------------------------------------------------------

    st.header("⚙️ Hyperparameter Tuning")

    st.write(
        "GridSearchCV identified C = 1 as the best "
        "Logistic Regression hyperparameter."
    )

    st.write(
        "The tuned model achieved the same test-set performance "
        "as the original Logistic Regression model."
    )


# ============================================================
# PAGE 4 — BUSINESS INSIGHTS
# ============================================================

elif page == "💡 Business Insights":

    st.title("💡 Business Insights")

    st.write(
        "Key observations from the exploratory data analysis "
        "and customer churn analysis."
    )

    st.divider()

    # --------------------------------------------------------
    # CONTRACT TYPE
    # --------------------------------------------------------

    st.header("📄 Contract Type")

    st.write(
        """
        Customers with **Month-to-month contracts** generally
        represent a higher churn risk compared with customers
        on longer-term contracts.

        Contract duration can therefore be an important factor
        when designing customer retention strategies.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # TENURE
    # --------------------------------------------------------

    st.header("⏳ Customer Tenure")

    st.write(
        """
        Customers with shorter tenure tend to have a higher
        likelihood of churn compared with customers who have
        stayed with the company for a longer period.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # MONTHLY CHARGES
    # --------------------------------------------------------

    st.header("💰 Monthly Charges")

    st.write(
        """
        Higher monthly charges can be associated with increased
        churn risk, particularly when combined with short tenure
        or month-to-month contracts.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # PAYMENT METHOD
    # --------------------------------------------------------

    st.header("💳 Payment Method")

    st.write(
        """
        Payment method can also be associated with different
        churn patterns.

        Understanding these differences can help identify
        customers who may benefit from targeted retention actions.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # BUSINESS ACTIONS
    # --------------------------------------------------------

    st.header("🎯 Recommended Business Actions")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("1️⃣ Target High-Risk Customers")

        st.write(
            "Use the churn probability score to prioritize "
            "customers with the highest predicted churn risk."
        )

        st.subheader("2️⃣ Focus on New Customers")

        st.write(
            "Create onboarding and early-life-cycle retention "
            "campaigns for customers with short tenure."
        )

    with col2:

        st.subheader("3️⃣ Encourage Longer Contracts")

        st.write(
            "Offer incentives to month-to-month customers "
            "to move toward longer-term contracts."
        )

        st.subheader("4️⃣ Monitor High-Value Customers")

        st.write(
            "Customers with high monthly charges should be "
            "monitored for potential dissatisfaction and churn risk."
        )

    st.divider()

    st.info(
        "💡 The churn prediction model can be integrated into "
        "a retention workflow to prioritize proactive customer actions."
    )