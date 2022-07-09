import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

@st.cache
def get_data():
     url = 'https://raw.githubusercontent.com/William-Roldan/Diplomado_Ciencia_de_datos/master/App/Data/kc_house_data.csv'
     return pd.read_csv(url)

data = get_data()

st.write('Proximamente! :🔧')
st.sidebar.header('Proximamente! :🔧')
