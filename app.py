import streamlit as st
import pandas as pd 
import plotly_express as px
 
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Exploración de Datos de Vehículos Usados')

st.write("Este conjunto de datos tiene ", car_data.shape[0], " filas y ", car_data.shape[1], " columnas.")

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma del Odómetro')

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión Precio vs. Odómetro')

# Crear un botón que construya un histograma
if st.button('Mostrar Histograma del Odómetro'):
    fig = px.histogram(car_data, x="odometer", title='Histograma del Odómetro')
    st.plotly_chart(fig)

# Crear un botón que construya un gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión del Precio vs. Odómetro'):
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
        title='Gráfico de Dispersión: Precio vs. Odómetro',
        labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)'})
    st.plotly_chart(fig_scatter)