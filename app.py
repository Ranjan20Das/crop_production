import streamlit as st
import requests
import json

# 🔑 IBM Cloud credentials
API_KEY = "cpd-apikey-IBMid-6950012C8R-2025-08-22T14:23:48Z"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/crop123/predictions?version=2021-05-01"

# Function to get IAM token
def get_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

# Streamlit UI
st.title("🌱 Crop Production Prediction")
st.write("Enter soil and weather parameters to predict the suitable crop")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0.0, value=30.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, value=79.0)
K = st.number_input("Potassium (K)", min_value=0.0, value=75.0)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=100.0)

if st.button("Predict Crop"):
    # Prepare payload
    payload = {
        "input_data": [
            {
                "fields": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
                "values": [[N, P, K, temperature, humidity, ph, rainfall]]
            }
        ]
    }

    try:
        # Get IAM token
        token = get_token(API_KEY)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        # Send request to Watson ML deployment
        response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result["predictions"][0]["values"][0][0]
            st.success(f"✅ Predicted Crop: **{prediction}**")
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"⚠️ Exception: {str(e)}")
