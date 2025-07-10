# pages/3_Data_Visualizer.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("📁 Health Data Visualizer")
st.markdown("Upload your health-related CSV file and visualize the insights!")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Preview data
    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Basic info
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # Column selector for histogram
    st.subheader("📈 Histogram")
    column = st.selectbox("Select column to plot histogram", df.columns)
    
    if df[column].dtype != "object":
        plt.figure(figsize=(8, 4))
        sns.histplot(df[column], bins=20, kde=True, color='skyblue')
        plt.xlabel(column)
        st.pyplot()
    else:
        st.warning("⚠️ Please select a numerical column.")

    # Pie chart for a categorical column (optional)
    st.subheader("🥧 Pie Chart (Categorical Columns Only)")
    cat_columns = df.select_dtypes(include="object").columns.tolist()
    
    if cat_columns:
        pie_col = st.selectbox("Select categorical column", cat_columns)
        pie_data = df[pie_col].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
        plt.title(f"{pie_col} Distribution")
        st.pyplot()
    else:
        st.info("ℹ️ No categorical columns available for pie chart.")

    # Correlation heatmap
    st.subheader("🔍 Correlation Heatmap")
    numeric_df = df.select_dtypes(include="number")
    corr = numeric_df.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot()
else:
    st.info("📌 Please upload a CSV file to proceed.")
