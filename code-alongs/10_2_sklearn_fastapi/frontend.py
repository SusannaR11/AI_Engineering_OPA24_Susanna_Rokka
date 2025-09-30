import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd


iris_data = read_api_endpoint("/api")
df = pd.DataFrame(iris_data.json())


def layout():
    st.markdown("# Classify your iris flower")

    with st.form("iris_data"):
        sepal_length = st.number_input(
            "Sepal length (cm)", min_value=4.01, max_value=8.49, value=6.0
        )
        sepal_width = st.number_input(
            "Sepal length (cm)", min_value=1.81, max_value=4.99, value=0.1
        )
        petal_length = st.number_input(
            "Sepal length (cm)", min_value=0.81, max_value=7.49, value=0.1
        )
        petal_width = st.number_input(
            "Sepal length (cm)", min_value=0.01, max_value=2.99, value=0.1
            )
        submitted = st.form_submit_button("PREDICT FLOWER")

    if submitted:
        payload = {
            "SepalLengthCm": 6,
            "SepalWidthCm": 3,
            "PetalLengthCm": 3.8,
            "PetalWidthCm": 1.2,
        }

        response = post_api_endpoint(payload, endpoint="/api/predict")
        predicted_flower = response.json().get("predicted_flower")

        st.markdown(f"Predicted flower: {predicted_flower}")
        st.image(f"{ASSETS_PATH / predicted_flower}.jpg")

    print(f"{sepal_length = }")
    print(f"{submitted = }")

    st.markdown("## Raw data")
    st.dataframe(df)


if __name__ == "__main__":
    layout()