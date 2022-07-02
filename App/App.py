import streamlit as st
import pandas as pd


st.set_page_config(page_title="Inicio",page_icon="sunglasses",)

data = pd.read_csv('Data/kc_house_data.csv')

st.title('VENTA DE CASAS EN KING COUNT, WA (USA)')
st.header('PROPUESTO POR: [William Roldan](https://github.com/William-Roldan)')


st.write('Se hizo uso de la base de datos de [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction), los datos incluyen viviendas vendidas entre mayo de 2014 y mayo de 2015.')
st.write('La base de datos nos da información de 18 características distribuidas en columna de la base de datos:')

with st.expander("Detalles de las Columnas",expanded=0):
    st.write("""
    - id: Identificación única para cada casa vendida
    - date: Fecha de la venta de la casa
    - price: Precio de cada vivienda vendida
    - bedrooms: Número de dormitorios
    - bathrooms: Número de baños, donde .5 representa una habitación con inodoro pero sin ducha
    - sqft_living: Pies cuadrados del espacio habitable interior de los apartamentos
    - sqft_lot: Pies cuadrados del espacio del terreno
    - floors: Número de pisos
    - waterfront: una variable ficticia para determinar si el apartamento tenía vistas al paseo marítimo o no.
    - view: un índice de 0 a 4 de qué tan buena fue la vista de la propiedad
    - condition: Un índice de 1 a 5 sobre la condición del apartamento
    - grade: un índice de 1 a 13, donde 1-3 no alcanza la construcción y el diseño de edificios, 7 tiene un nivel promedio de construcción y diseño, y 11-13 tiene un nivel de construcción y diseño de alta calidad.
    - sqft_above: los pies cuadrados del espacio interior de la vivienda que está sobre el nivel del suelo
    - sqft_basement: los pies cuadrados del espacio interior de la vivienda que está por debajo del nivel del suelo
    - yr_built: el año en que se construyó inicialmente la casa
    - yr_renovated: El año de la última renovación de la casa
    - zipcode: en qué área de código postal se encuentra la casa
    - lat: latitud
    - long: Longitud
    - sqft_living15: Los pies cuadrados de espacio habitable de vivienda interior para los 15 vecinos más cercanos
    - sqft_lot15: Los pies cuadrados de los lotes de terreno de los 15 vecinos más cercanos
        """)


with st.expander("Tabla",expanded=0):
    st.write('**Base de Datos House Sales in King County**')
    st.write(data)
