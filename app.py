import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Introduction
st.title("Car Price Prediction App")
st.write("""
Welcome to the Car Price Prediction App! This app allows you to:
- View statistics and correlations among features.
- Visualize data trends to understand the dataset better.
""")

# Load dataset
try:
    data = pd.read_csv("vehicles_us.csv")
    st.write("Dataset successfully loaded!")
    st.write(data.head())
except FileNotFoundError:
    st.error("Default dataset 'vehicles_us.csv' not found. Please ensure the file is in the working directory.")
    st.stop()

# Select numeric columns
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
if numeric_columns.empty:
    st.warning("No numeric columns found in the dataset!")
else:
    st.write("Numeric columns detected:")
    st.write(list(numeric_columns))

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())

    # Correlation Matrix
    st.subheader("Correlation Matrix")
    corr = data[numeric_columns].corr()
    st.write(corr)

    # Heatmap
    st.subheader("Heatmap of Correlations")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Visualizations
    st.subheader("Visualizations")
    feature = st.selectbox("Select a feature for distribution plot", numeric_columns)
    if feature:
        fig, ax = plt.subplots()
        sns.histplot(data[feature], kde=True, ax=ax)
        ax.set_title(f"Distribution of {feature}")
        st.pyplot(fig)

# Footer
st.write("Developed by leoMT05")
