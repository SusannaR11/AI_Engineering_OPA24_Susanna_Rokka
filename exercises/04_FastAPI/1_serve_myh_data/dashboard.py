import streamlit as st
import pandas as pd
from constants import DATA_PATH

df = pd.read_excel(DATA_PATH)


st.markdown("# Yrkeshögskolan dashboard")
st.markdown("## Resultat ansökningsomgång 2024")

st.write(df)