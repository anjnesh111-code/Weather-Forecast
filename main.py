from tkinter import Place
from backend import get_data
import streamlit as st
import plotly.express as px
st.title("Weather Forecast for the Next Days")

place=st.text_input('Place:')
days=st.slider("Forecast days:",min_value=1,max_value=5,help="Number of days to see forecast")
option=st.selectbox("Select data to view: ",("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")
if place:
    try:
        filtered_data=get_data(place,days)
        if option=="Temperature":
            temp = [dict["main"]["temp"] for dict in filtered_data]
            dates=[dict["dt_txt"] for dict in filtered_data]
            figure=px.line(x=dates,y=temp,labels={"x":"Dates","y":"Temperature(c)"})
            st.plotly_chart(figure)
        if option=="Sky":
            images={"Clear":'images/clear.png',"Clouds":'images/cloud.png',"Rain":'images/rain.png',"Snow":'images/snow.png'}
            Sky_conditions = [
                dict["weather"][0]["main"] for dict in filtered_data ]
            image_paths=[images[conditions] for conditions in Sky_conditions]
            st.image(image_paths,width=115)
    except KeyError:
        st.write("That place doesn't exist!")
    except TypeError:
        st.write("That place doesn't exist!!")