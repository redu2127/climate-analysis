import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Climate Analysis Dashboard")

df = pd.read_csv("notebooks/cleaned_data.csv")

country = st.selectbox("Select Country", df["Country"].unique())

filtered = df[df["Country"] == country]

st.subheader("Temperature Trend")
st.line_chart(filtered["T2M"])
st.subheader("Precipitation")
st.line_chart(filtered["PRECTOTCORR"])