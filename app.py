import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow import keras


# -----------------------------------
# LOAD MODEL AND SCALER
# -----------------------------------

model = keras.models.load_model("breast_cancer_ann.keras")
scaler = joblib.load("scaler.pkl")


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🩺 Breast Cancer Prediction")
st.write("Enter the 30 tumor measurement values below.")


# -----------------------------------
# EXACT FEATURE NAMES
# -----------------------------------

features = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean",
    "concave_points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",

    "radius_se",
    "texture_se",
    "perimeter_se",
    "area_se",
    "smoothness_se",
    "compactness_se",
    "concavity_se",
    "concave_points_se",
    "symmetry_se",
    "fractal_dimension_se",

    "radius_worst",
    "texture_worst",
    "perimeter_worst",
    "area_worst",
    "smoothness_worst",
    "compactness_worst",
    "concavity_worst",
    "concave_points_worst",
    "symmetry_worst",
    "fractal_dimension_worst"
]


# -----------------------------------
# FORM
# -----------------------------------

with st.form("prediction_form"):

    st.subheader("Enter Patient Measurements")

    user_input = []

    col1, col2, col3 = st.columns(3)

    for i, feature in enumerate(features):

        if i % 3 == 0:
            with col1:
                value = st.number_input(
                    feature,
                    value=0.0,
                    format="%.6f"
                )

        elif i % 3 == 1:
            with col2:
                value = st.number_input(
                    feature,
                    value=0.0,
                    format="%.6f"
                )

        else:
            with col3:
                value = st.number_input(
                    feature,
                    value=0.0,
                    format="%.6f"
                )

        user_input.append(value)

    predict_button = st.form_submit_button(
        "🔍 Predict",
        use_container_width=True
    )


# -----------------------------------
# PREDICTION
# -----------------------------------

if predict_button:

    user_data = pd.DataFrame(
        [user_input],
        columns=features
    )

    user_input_scaled = scaler.transform(user_data)

    prediction = model.predict(
        user_input_scaled,
        verbose=0
    )

    probability = prediction[0][0]


    # -----------------------------------
    # RESULT
    # -----------------------------------

    st.subheader("Prediction Result")

    if probability >= 0.5:

        st.error("⚠️ Malignant - Cancer Detected")

        st.write(
            f"Prediction Probability: **{probability * 100:.2f}%**"
        )

    else:

        st.success("✅ Benign - No Cancer Detected")

        st.write(
            f"Prediction Probability: **{(1 - probability) * 100:.2f}%**"
        )