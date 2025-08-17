import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') #lendo os dados
hist_button = st.button("Criar histograma") #criar botao

if hist_button: #se o botao for clicado
    st.write("Criando um histograma para o conjunto de dados de anuncios de venda de carros")
#criar um histograma    
    fig = px.histogram(car_data, x="odometer")

#ixibir grafico plotly interativo
    st.plotly_chart(fig, use_container_width=True)

#grafico de dispersao
scatter_button = st.button("Criar grafico de dispersao")

if scatter_button: #se o  segundo botao for clicado
    st.write("Criando um grafico de dispersao para o conjunto de dados de anuncios de vendas de carros")

    #criar um grafico de dispersao
    fig = px.scatter(car_data, x="odometer", y="price")

    #ixibir o grafico
    st.plotly_chart(fig, use_container_width=True)