
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('best_model.pkl')

# Streamlit app UI
st.title("Housing Price Predictor")

st.markdown("Enter the property details below:")

# Create input fields for each feature
squareMeters = st.number_input("Total Area (in square meters)", min_value=10)
numberOfRooms = st.number_input("Number of Rooms", min_value=1)
hasYard = st.selectbox("Has Yard?", [0, 1])
hasPool = st.selectbox("Has Pool?", [0, 1])
floors = st.number_input("Number of Floors", min_value=1)
cityCode = st.number_input("City Code", min_value=1)
cityPartRange = st.number_input("City Part Range", min_value=1)
numPrevOwners = st.number_input("Number of Previous Owners", min_value=0)
isNewBuilt = st.selectbox("Is Newly Built?", [0, 1])
hasStormProtector = st.selectbox("Has Storm Protector?", [0, 1])
basement = st.selectbox("Has Basement?", [0, 1])
attic = st.selectbox("Has Attic?", [0, 1])
garage = st.selectbox("Has Garage?", [0, 1])
hasStorageRoom = st.selectbox("Has Storage Room?", [0, 1])
hasGuestRoom = st.selectbox("Has Guest Room?", [0, 1])
house_age = st.number_input("House Age (in years)", min_value=0)

# Predict button
if st.button("Predict Price"):
    features = np.array([[squareMeters, numberOfRooms, hasYard, hasPool, floors,
                          cityCode, cityPartRange, numPrevOwners, isNewBuilt,
                          hasStormProtector, basement, attic, garage,
                          hasStorageRoom, hasGuestRoom, house_age]])
    
    prediction = model.predict(features)[0]
    st.success(f"Predicted House Price: ${prediction:,.2f}")
