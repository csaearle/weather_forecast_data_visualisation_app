import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

# Add title text_input, slider, selectbox, and subheader
st.title("Weather forecast for the Next days")
place = st.text_input("Place: ")
forecast_days = st.slider("Forecast days",
                                    min_value=1, max_value=5,
                                    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky conditions"))
st.subheader(f"{option} for the next {forecast_days} days in {place}")

# Get the temperature/"Sky conditions"
if place:
    filtered_data = get_data(place, forecast_days)

    if option == "Temperature":
    # Create a temperature plot
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

if option == "Sky conditions":
    images ={"Clear": "images/clear.png", "Clouds": "images/cloud.png",
             "Rain": "images/rain.png", 'Snow': 'images/snow.png'}
    sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
    image_paths = [images[condition] for condition in sky_conditions]

    st.image(image_paths, width=115)