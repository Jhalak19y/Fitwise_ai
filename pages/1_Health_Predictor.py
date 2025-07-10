# pages/1_Health_Predictor.py

import streamlit as st
import pandas as pd
import joblib

st.title("🩺 Heart Disease Predictor")
st.markdown("Predict your risk based on health inputs using a trained ML model.")

# Load model
try:
    model = joblib.load("models/heart_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found. Please run train_model.py first.")
    st.stop()

# Form inputs
with st.form("predict_form"):
    st.subheader("📋 Enter Your Health Info")

    age = st.number_input("Age", min_value=1, max_value=120, value=30)

    # 🔁 Replace numeric sex input with labels
    sex_label = st.radio("Sex", ["Female", "Male"])
    sex = 0 if sex_label == "Female" else 1

    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", value=120)
    chol = st.number_input("Cholesterol Level", value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", value=150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Oldpeak (ST depression)", value=1.0)
    slope = st.selectbox("Slope of the ST segment", [0, 1, 2])
    ca = st.selectbox("Number of major vessels (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    submit = st.form_submit_button("🔍 Predict")

# On form submit
if submit:
    input_data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak, slope, ca, thal
    ]], columns=[
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ])

    # Make prediction
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease.\n\n**Probability: {prob:.2%}**")
    else:
        st.success(f"✅ Low risk of heart disease.\n\n**Probability: {prob:.2%}**")
