
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('best_model.pkl')

st.title("Housing Price Predictor")
st.markdown("Enter the property details below:")

# Numeric Features
numeric_features = {
    "Total Area (in square meters)": 10,
    "Number of Rooms": 1,
    "Number of Floors": 1,
    "City Code": 1,
    "City Part Range": 1,
    "Number of Previous Owners": 0,
    "House Age (in years)": 0
}

numeric_inputs = []
for label, min_val in numeric_features.items():
    val = st.number_input(label, min_value=min_val)
    numeric_inputs.append(val)

# Binary Features
binary_labels = [
    "Has Yard?", "Has Pool?", "Is Newly Built?", "Has Storm Protector?",
    "Has Basement?", "Has Attic?", "Has Garage?", 
    "Has Storage Room?", "Has Guest Room?"
]

binary_inputs = []
for label in binary_labels:
    val = st.selectbox(label, ["No", "Yes"])
    binary_inputs.append(1 if val == "Yes" else 0)

# Predict
if st.button("Predict Price"):
    input_array = np.array([numeric_inputs[:2] + binary_inputs[:2] + numeric_inputs[2:] + binary_inputs[2:]])
    prediction = model.predict(input_array)[0]
    st.success(f"Predicted House Price: ${prediction:,.2f}")
