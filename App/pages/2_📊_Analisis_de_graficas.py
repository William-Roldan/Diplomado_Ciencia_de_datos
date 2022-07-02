import streamlit as st
import pandas as pd
from plotly import express as px

@st.cache
def get_data():
     url = 'https://raw.githubusercontent.com/sebmatecho/CienciaDeDatos/master/ProyectoPreciosCasas/data/kc_house_data.csv'
     return pd.read_csv(url)

data = get_data()

st.header('Graficas')
st.sidebar.header('Proximamente! :sunglasses:')

try:
        numeric_columns=list(data.select_dtypes(['float','int']).columns)
except Exception as e:
    print(e)
    st.write("No se encuentra la Base de Datos")


chart_select=st.sidebar.selectbox(
    label="select the chart type",
    options=['Scatterplots','Lineplots','Histogram','Boxplot']
)


if chart_select=='Scatterplots':
    st.sidebar.subheader("scatterplot settings")
    try:
        X_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        Y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot1=px.scatter(data_frame=data,x=X_values,y=Y_values)
        #Mostrar la grafica
        st.plotly_chart(plot1)
    except Exception as e:
        print(e)

if chart_select=='Lineplots':
    st.sidebar.subheader("Lineplot settings")
    try:
        X_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        Y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot2=px.line(data_frame=data,x=X_values,y=Y_values)
        #Mostrar la grafica
        st.plotly_chart(plot2)
    except Exception as e:
        print(e)

if chart_select=='Histogram':
    st.sidebar.subheader("Histogram settings")
    try:
        X_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        Y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot3=px.histogram(data_frame=data,x=X_values,y=Y_values)
        #Mostrar la grafica
        st.plotly_chart(plot3)
    except Exception as e:
        print(e)

if chart_select=='Boxplot':
    st.sidebar.subheader("Boxplot settings")
    try:
        X_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        Y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot4=px.box(data_frame=data,x=X_values,y=Y_values)
        #Mostrar la grafica
        st.plotly_chart(plot4)
    except Exception as e:
        print(e)