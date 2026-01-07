
import streamlit as st

st.title("✈️ Aviator Predictor App")
st.write("Welcome! This app will predict the flight duration and analyze patterns.")

# Example input and output
minutes = st.slider("Select number of minutes:", 1, 100)
st.write(f"The plane might fly for about {minutes} minutes 🚀")

# Placeholder for your model logic
st.info("AI prediction model coming soon...")
