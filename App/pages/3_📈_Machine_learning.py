import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

@st.cache
def get_data():
     url = 'https://raw.githubusercontent.com/sebmatecho/CienciaDeDatos/master/ProyectoPreciosCasas/data/kc_house_data.csv'
     return pd.read_csv(url)

data = get_data()

st.write('Proximamente! :sunglasses:')
st.sidebar.header('Proximamente! :sunglasses:')


##pruebas
st.title('Pruebas')

# valores={'Habitaciones':data['bedrooms'],'Pisos':data['floors'],'Baños':data['bathrooms']}
# #for k,v in valores.items():
# def resumen(var1):
#      return st.write(data[data[var1]==data[var1].max()])

#if 'Habitaciones' in OptFiltro:
#     resumen('bedrooms')
#      st.write(data[data['bedrooms']==data['bedrooms'].max()])
#      st.write(data[data['bedrooms']==data['bedrooms'].max()].shape[0])
#      st.write(data['bedrooms'].mean())
#      st.write(data['bedrooms'].mode())
#      st.write(data['bedrooms'].median())
#      st.write(data['bedrooms'].min())
#      st.write(data['bedrooms'].max())

# def resumen(var1):
#      return st.write(data[data[var1]==data[var1].max()])
     
     #return st.write(data[data[var1]==data[var1].max()].shape[0])
     # st.write(data['bedrooms'].mean())
     # st.write(data['bedrooms'].mode())
     # st.write(data['bedrooms'].median())
     # st.write(data['bedrooms'].min())
     # st.write(data['bedrooms'].max())




# fig=plt.boxplot(data['price'])
# st.write(fig)



st.write(plt.boxplot(data['price']))
