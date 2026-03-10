import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load trained model
model = pickle.load(open(  r'C:\Users\DELL\Downloads\accident_severity_model (2).pkl', 'rb'))

st.set_page_config(page_title="Road Accident Severity Predictor", layout="centered")

st.title("🚗 Road Accident Severity Prediction")
st.write("Predict whether an accident will be Severe or Not Severe")

st.markdown("---")

# ===============================
# User Input Fields
# ===============================

state = st.number_input("State (Encoded Value)", min_value=0)
city = st.number_input("City (Encoded Value)", min_value=0)
vehicle_type = st.number_input("Vehicle Type (Encoded Value)", min_value=0)
cause = st.number_input("Cause (Encoded Value)", min_value=0)
injuries = st.number_input("Number of Injuries", min_value=0)
weather = st.number_input("Weather (Encoded Value)", min_value=0)
road_type = st.number_input("Road Type (Encoded Value)", min_value=0)
month = st.slider("Month", 1, 12)
hour = st.slider("Hour of Accident", 0, 23)

# ===============================
# Prediction
# ===============================

if st.button("Predict Severity"):

    input_data = np.array([[state, city, vehicle_type, cause,
                            injuries, weather, road_type,
                            month, hour]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Severe Accident Predicted")
    else:
        st.success("✅ Not Severe Accident")
