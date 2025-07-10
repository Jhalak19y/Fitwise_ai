import streamlit as st 

# pages/2_BMI_Calculator.py

import streamlit as st

st.title("🧮 BMI & Calorie Calculator")
st.markdown("Track your health with simple inputs. Get your BMI and daily calorie needs!")

# Form
with st.form("bmi_form"):
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.slider("Age", 10, 80, 25)
    height_cm = st.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
    weight_kg = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=65)
    activity_level = st.selectbox("Activity Level", [
        "Sedentary (little to no exercise)",
        "Lightly active (1–3 days/week)",
        "Moderately active (3–5 days/week)",
        "Very active (6–7 days/week)",
        "Super active (twice daily or athlete)"
    ])
    goal = st.radio("Your Goal", ["Lose Weight", "Maintain Weight", "Gain Weight"])

    submit = st.form_submit_button("Calculate")

if submit:
    # Convert height from cm to meters
    height_m = height_cm / 100

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    # Interpret BMI
    if bmi < 18.5:
        bmi_category = "Underweight 🦴"
        color = "orange"
    elif 18.5 <= bmi < 25:
        bmi_category = "Normal weight ✅"
        color = "green"
    elif 25 <= bmi < 30:
        bmi_category = "Overweight ⚠️"
        color = "yellow"
    else:
        bmi_category = "Obese ❌"
        color = "red"

    # Show result
    st.markdown(f"<h3 style='color:{color}'>Your BMI: {bmi} ({bmi_category})</h3>", unsafe_allow_html=True)

    # Calorie calculation using Mifflin-St Jeor Formula
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Activity multiplier
    activity_multipliers = {
        "Sedentary (little to no exercise)": 1.2,
        "Lightly active (1–3 days/week)": 1.375,
        "Moderately active (3–5 days/week)": 1.55,
        "Very active (6–7 days/week)": 1.725,
        "Super active (twice daily or athlete)": 1.9
    }

    calories = bmr * activity_multipliers[activity_level]

    # Adjust based on goal
    if goal == "Lose Weight":
        calories -= 300
    elif goal == "Gain Weight":
        calories += 300

    calories = int(calories)

    st.markdown(f"### 🥗 Your Estimated Daily Calories: **{calories} kcal**")

    # Suggestion based on goal
    if goal == "Lose Weight":
        st.info("💡 Tip: Stay in a calorie deficit. Focus on protein, fiber, and hydration.")
    elif goal == "Gain Weight":
        st.info("💡 Tip: Increase your protein and calorie intake. Add healthy fats.")
    else:
        st.info("💡 Tip: Maintain balance. Keep active and consistent with your meals.")
