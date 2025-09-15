import streamlit as st
import httpx
from constants import DATA_PATH, ASSETS_PATH

url = "http://127.0.0.1:8000/api/iris/v1/predict"

def predict_flower(payload):
    with httpx.Client(timeout=10) as client:
        response = client.post(url = url, json = payload)
        response.raise_for_status()
        return response

# main page header
st.markdown("# Predict Iris Flower")

with st.form("iris_data"):

    sepal_length = st.number_input("Sepal length (cm)", min_value=4.01, max_value=8.49, value=6.0)
    st.markdown(sepal_length)

    sepal_width = st.number_input("Sepal width (cm)", min_value=1.81, max_value=4.99, value=2.5)
    st.markdown(sepal_width)

    petal_length = st.number_input("Petal length (cm)", min_value=0.81, max_value=7.49, value=4.5)
    st.markdown(petal_length)

    petal_width = st.number_input("Petal width (cm)", min_value=0.01, max_value=2.99, value=1.2)
    st.markdown(petal_width)

    submitted = st.form_submit_button("PREDICT")

#st.markdown(submitted)

#st.markdown(type(petal_width)) #check what datatype output is

if submitted:
    payload= {
            "sepal_length": (sepal_length), 
            "sepal_width": (sepal_width), 
            "petal_length": (petal_length), 
            "petal_width": (petal_width)
    }
    
    response = predict_flower(payload=payload).json()
    flower = response.get("predicted_flower").casefold() #casefold for lower case
    st.markdown(f"Predicted flower is {flower}")



# activate streamlit frontend:
#  streamlit run frontend.py

# comment out Cmd + K + C
# comment in Cmd + K + U