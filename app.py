import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

# App Title
st.title("Student Performance Prediction")

# User Inputs
g1 = st.number_input(
    "G1 (First Period Grade)",
    min_value=0,
    max_value=20,
    value=10
)

g2 = st.number_input(
    "G2 (Second Period Grade)",
    min_value=0,
    max_value=20,
    value=10
)

failures = st.number_input(
    "Failures",
    min_value=0,
    max_value=10,
    value=0
)

studytime = st.number_input(
    "Study Time",
    min_value=1,
    max_value=4,
    value=2
)

medu = st.number_input(
    "Mother Education",
    min_value=0,
    max_value=4,
    value=2
)

fedu = st.number_input(
    "Father Education",
    min_value=0,
    max_value=4,
    value=2
)

# Prediction Button
if st.button("Predict Final Grade"):

    data = pd.DataFrame(
        [[g1, g2, failures, studytime, medu, fedu]],
        columns=[
            "G1",
            "G2",
            "failures",
            "studytime",
            "Medu",
            "Fedu"
        ]
    )

    prediction = model.predict(data)[0]

    # Performance Category
    if prediction < 8:
        category = "Poor"
    elif prediction < 12:
        category = "Average"
    elif prediction < 16:
        category = "Good"
    else:
        category = "Excellent"

    st.success(
        f"Predicted Final Grade (G3): {prediction:.2f}"
    )

    st.info(
        f"Performance Category: {category}"
    )