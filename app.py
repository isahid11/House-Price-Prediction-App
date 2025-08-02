import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title(" Paris Housing Price Predictor")
st.markdown("Enter property details to estimate its market price:")

# Inputs
squareMeters = st.number_input("Total Area (sq meters)", min_value=89, max_value=100000, value=50000)
numberOfRooms = st.number_input("Number of Rooms", min_value=1, max_value=100, value=5)
hasYard = st.selectbox("Has Yard?", ["No", "Yes"])
hasPool = st.selectbox("Has Pool?", ["No", "Yes"])
floors = st.number_input("Number of Floors", min_value=1, max_value=100, value=1)
cityCode = st.number_input("City Code", min_value=1, value=50000)
cityPartRange = st.number_input("City Part Range", min_value=1, max_value=10, value=5)
numPrevOwners = st.number_input("Number of Previous Owners", min_value=0, max_value=10, value=2)
isNewBuilt = st.selectbox("Is Newly Built?", ["No", "Yes"])
hasStormProtector = st.selectbox("Has Storm Protector?", ["No", "Yes"])
basement = st.number_input("Basement Area (sq meters)", min_value=0, max_value=10000, value=1000)
attic = st.number_input("Attic Area (sq meters)", min_value=0, max_value=10000, value=1000)
garage = st.number_input("Garage Area (sq meters)", min_value=0, max_value=1000, value=100)
hasStorageRoom = st.selectbox("Has Storage Room?", ["No", "Yes"])
hasGuestRoom = st.number_input("Number of Guest Rooms", min_value=0, max_value=10, value=1)
house_age = st.number_input("House Age (years)", min_value=0, max_value=200, value=20)

# Convert selections to numeric binary
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
    basement,
    attic,
    garage,
    binary_map(hasStorageRoom),
    hasGuestRoom,
    house_age
]

# Predict
if st.button("Predict Price"):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    st.success(f" Estimated House Price: **${prediction:,.2f}**")
