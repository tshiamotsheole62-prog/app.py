import streamlit as st
import random
import time

st.set_page_config(page_title="Flight Predictor", page_icon="✈️")

st.title("✈️ Flight Duration Predictor (Demo)")
st.write("This app simulates flight duration outcomes.")

st.warning("⚠️ This is a simulation for educational purposes only.")

if st.button("Start Flight"):
    with st.spinner("Plane is flying..."):
        time.sleep(2)

    duration = round(random.uniform(1.0, 10.0), 2)

    st.success(f"✈️ Flight lasted **{duration} seconds**")
