import streamlit as st

st.title("✈️ Flight Time Predictor")

st.write("This app estimates how long a plane will fly.")

distance = st.number_input("Enter distance (km)", min_value=1.0)
speed = st.number_input("Enter speed (km/h)", min_value=1.0)

if st.button("Predict Flight Time"):
    time_hours = distance / speed
    st.success(f"Estimated flight time: {time_hours:.2f} hours")
