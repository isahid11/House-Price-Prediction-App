
import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Housing Price Predictor")
st.markdown("Enter the property details below:")

# Input fields
squareMeters = st.number_input("Total Area (in square meters)", min_value=10, max_value=1000)
numberOfRooms = st.number_input("Number of Rooms", min_value=1, max_value=10)
hasYard = st.selectbox("Has Yard?", ["No", "Yes"])
hasPool = st.selectbox("Has Pool?", ["No", "Yes"])
floors = st.number_input("Number of Floors", min_value=1, max_value=10)
cityCode = st.number_input("City Code", min_value=1)
cityPartRange = st.number_input("City Part Range", min_value=1)
numPrevOwners = st.number_input("Number of Previous Owners", min_value=0)
isNewBuilt = st.selectbox("Is Newly Built?", ["No", "Yes"])
hasStormProtector = st.selectbox("Has Storm Protector?", ["No", "Yes"])
basement = st.selectbox("Has Basement?", ["No", "Yes"])
attic = st.selectbox("Has Attic?", ["No", "Yes"])
garage = st.selectbox("Has Garage?", ["No", "Yes"])
hasStorageRoom = st.selectbox("Has Storage Room?", ["No", "Yes"])
hasGuestRoom = st.selectbox("Has Guest Room?", ["No", "Yes"])
house_age = st.number_input("House Age (in years)", min_value=0, max_value=200)

# Convert binary
binary_map = lambda x: 1 if x == "Yes" else 0
input_data = [
    squareMeters,
    numberOfRooms,
    binary_map(hasYard),
    binary_map(hasPool),
    floors,
    cityCode,
    cityPartRange,
    numPrevOwners,
    binary_map(isNewBuilt),
    binary_map(hasStormProtector),
    binary_map(basement),
    binary_map(attic),
    binary_map(garage),
    binary_map(hasStorageRoom),
    binary_map(hasGuestRoom),
    house_age
]

# Predict
if st.button("Predict Price"):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    st.success(f"Predicted House Price: ${prediction:,.2f}")

