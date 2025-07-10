# pages/5_Suggestions.py

import streamlit as st

st.title("🧠 Personalized Health Suggestions")
st.markdown("Smart tips and motivation based on your BMI and health goal.")

# Input form
with st.form("suggestion_form"):
    bmi = st.number_input("Enter your latest BMI", min_value=10.0, max_value=50.0, step=0.1)
    goal = st.radio("Your Current Goal", ["Lose Weight", "Maintain Weight", "Gain Weight"])
    submit = st.form_submit_button("Get Suggestions")

# Logic after submit
if submit:
    st.markdown("---")

    # BMI category logic
    if bmi < 18.5:
        category = "Underweight"
        st.warning("⚠️ Your BMI suggests you're underweight.")
        tip = "Try increasing your calorie intake with nutrient-dense foods. Include healthy fats like nuts and avocados. 🥑"
    elif 18.5 <= bmi < 25:
        category = "Healthy"
        st.success("✅ Great! You're in the healthy BMI range.")
        tip = "Maintain a balanced diet, stay active, and focus on consistency. 🥗"
    elif 25 <= bmi < 30:
        category = "Overweight"
        st.warning("⚠️ You're slightly above the ideal range.")
        tip = "Stay in a calorie deficit. Incorporate cardio, avoid sugary drinks, and track your meals. 🏃‍♀️"
    else:
        category = "Obese"
        st.error("❌ Your BMI indicates obesity.")
        tip = "Prioritize daily movement, reduce ultra-processed foods, and seek guidance if needed. 💡"

    st.markdown(f"### 📊 Category: **{category}**")
    st.markdown(f"### 💡 Suggestion: {tip}")

    # Goal-based encouragement
    st.markdown("---")
    if goal == "Lose Weight":
        st.info("🎯 Keep going! Weight loss is a journey, not a race. Small steps lead to big change.")
    elif goal == "Gain Weight":
        st.info("🎯 Fuel your body with good calories. Train consistently and be patient.")
    else:
        st.info("🎯 Balance is key. Stay active, eat mindfully, and check in with your body regularly.")

    # Motivational quote
    st.markdown("---")
    st.markdown("🧘‍♀️ **Motivation of the Day:**")
    st.markdown("> _“It does not matter how slowly you go as long as you do not stop.”_ – Confucius")

