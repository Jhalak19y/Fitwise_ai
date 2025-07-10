import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.title("📈 Health Progress Tracker")
st.markdown("Track your BMI, weight and health progress over time.")

# Initialize session state to store entries
if "history" not in st.session_state:
    st.session_state.history = []

# Input form
with st.form("track_form"):
    st.subheader("📝 Log Your Current Stats")
    date = st.date_input("Date", value=datetime.today())
    weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=60)
    height = st.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
    submit = st.form_submit_button("Add Entry")

# On form submission
if submit:
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    entry = {
        "Date": date.strftime("%Y-%m-%d"),
        "Weight (kg)": weight,
        "Height (cm)": height,
        "BMI": bmi
    }

    st.session_state.history.append(entry)
    st.success("✅ Entry added successfully!")

# If history exists, show table and plots
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    st.subheader("📋 Your Progress History")
    st.dataframe(df)

    # Download as CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="progress_tracker.csv",
        mime="text/csv"
    )

    # Sort by date for plotting
    df_sorted = df.sort_values(by="Date")

    # BMI Trend Plot
    st.subheader("📊 BMI Over Time")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(df_sorted["Date"], df_sorted["BMI"], marker='o', color="green", label="BMI")
    ax1.set_ylabel("BMI")
    ax1.set_title("BMI Trend")
    ax1.set_xticklabels(df_sorted["Date"], rotation=45)
    ax1.grid(True)
    st.pyplot(fig1)

    # Weight Trend Plot
    st.subheader("⚖️ Weight Over Time")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(df_sorted["Date"], df_sorted["Weight (kg)"], marker='s', color="blue", label="Weight")
    ax2.set_ylabel("Weight (kg)")
    ax2.set_title("Weight Trend")
    ax2.set_xticklabels(df_sorted["Date"], rotation=45)
    ax2.grid(True)
    st.pyplot(fig2)
else:
    st.info("📌 No data yet. Add your first entry above to begin tracking!")
