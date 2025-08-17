import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anuncios de venda de carros")
    
    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)