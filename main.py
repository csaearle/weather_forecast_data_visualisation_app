import streamlit as st
import pandas as pd

st.title("Weather forecast for the Next days")
place = st.text_input("Place: ")
forecast_days = st.slider("Forecast days",
                                    min_value=1, max_value=5,
                                    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky conditions"))
st.subheader(f"{option} for the next {forecast_days} days in {place}")