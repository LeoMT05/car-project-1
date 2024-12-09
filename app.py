import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file automatically (no upload needed)
data = pd.read_csv("vehicles_us.csv")  # Adjust the filename if necessary

# Display the first few rows of the dataset
st.write("Dataset Preview")
st.write(data.head())

# Summary Statistics
st.write("Summary Statistics:")
st.write(data.describe())

# Histogram of Prices
st.write("Histogram of Prices:")
plt.figure(figsize=(10,6))
plt.hist(data["price"], bins=30, color="blue", edgecolor="black")
plt.title("Histogram of Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
st.pyplot()  # Render the plot in Streamlit

# Scatter Plot: Price vs. Mileage
st.write("Price vs. Mileage (Scatter Plot):")
plt.figure(figsize=(10,6))
plt.scatter(data["mileage"], data["price"], alpha=0.5)
plt.title("Price vs. Mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")
st.pyplot()  # Render the plot in Streamlit

# Correlation Matrix
st.write("Correlation Matrix:")
plt.figure(figsize=(10,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
st.pyplot()  # Render the plot in Streamlit
data = pd.read_csv("vehicles_us.csv")
data = pd.read_csv("data/vehicles_us.csv")
