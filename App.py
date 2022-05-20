import streamlit as st
import pandas as pd
##import json
import folium
##import numpy as np
##import seaborn as sns
##import matplotlib.pyplot as plt

from plotly                   import express as px
##from folium.plugins           import MarkerCluster
##from streamlit_folium         import folium_static
##from matplotlib.pyplot        import figimage
##rom distutils.fancy_getopt   import OptionDummy

st.title('Aplicacion de prueba')

st.write('**Datos de king country, USA (20xx a 20xx)**:')
data=pd.read_csv('Data/kc_house_data.csv')
st.dataframe(data)


##no usar
##st.table(data)
##sale la tabla entera en la pagina


##primera parte // mostrar datos
st.write('**Casas en el periodo analisado:**','Disponibles {} casas'.format(data['id'].nunique()))

with st.expander("Mas barata y mas cara"):
     st.write('**Casa mas barata:**')
     st.dataframe(data[data['price']==data['price'].min()])

     st.write('**Casa mas cara:**')
     st.dataframe(data[data['price']==data['price'].max()])



##segunda parte // Filtrar datos
st.title('Filtros')
##forma de seleccionarlos los datos para el filtro
OptFiltro = st.multiselect(
     'Que quieres filtrar',
     ['Precios','Habitaciones', 'Baños', 'Metros cuadrados (Espacio habitable)','Pisos','Vista al mar','Indice de construccion','Condicion'],
     ['Habitaciones', 'Baños','Pisos'])

with st.expander("Mis Filtros",expanded=1):
     if 'Precios' in OptFiltro:
          Price = st.number_input ('Precios',step=1,min_value=0,max_value=round(data['price'].max()))

     if 'Habitaciones' in OptFiltro:
          Bedrooms = st.number_input('Habitaciones',step=1,min_value=0,max_value=round(data['bedrooms'].max()))

     if 'Baños' in OptFiltro:
          Bathrooms = st.number_input ('Baños',step=1,min_value=0,max_value=round(data['bathrooms'].max()))

     if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
          Mt2 = st.number_input('Metros cuadrados (Espacio habitable)',step=1,min_value=0,max_value=round(data['sqft_living'].max()))

     if 'Pisos' in OptFiltro:
          Floors = st.number_input('Pisos',step=1,min_value=0,max_value=round(data['floors'].max()))

     if 'Vista al mar' in OptFiltro:
          Waterfront= st.number_input('Vista al mar',step=1,min_value=0,max_value=round(data['waterfront'].max()))

     if 'Condicion' in OptFiltro:
          Cond = st.number_input('Condicion',step=1,min_value=0,max_value=round(data['condition'].max()))

     if 'Indice de construccion' in OptFiltro:
          Grade = st.number_input('Indice de construccion',step=1,min_value=0,max_value=round(data['grade'].max()))



st.title('Mis filtros')
##datos filtrados

if 'Precios' in OptFiltro:
     st.write('**Precio:**', Price)

if 'Habitaciones' in OptFiltro:
     st.write('**Numero de habitaciones:**', Bedrooms)

if 'Baños' in OptFiltro:
     st.write('**Baños:**', Bathrooms)

if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
     st.write('**Metros cuadrados (Espacio habitable):**', Mt2)

if 'Pisos' in OptFiltro:
     st.write('**Pisos:**', Floors)

if 'Vista al mar' in OptFiltro:
     if Waterfront ==1:
          st.write('**Vista al mar:**','Si')
     elif Waterfront ==0:
          st.write('**Vista al mar:**','No')

if 'Condicion' in OptFiltro:
     st.write('**Condicion:**', Cond)

if 'Indice de construccion' in OptFiltro:
     if 0<=Grade<=3:
          st.write('**Indice de construccion:**','Sin construir')
     elif 4<=Grade<=6:
          st.write('**Indice de construccion:**','Construccion y diseño pobre')
     elif 7<=Grade<=10:
          st.write('**Indice de construccion:**','Construccion y diseño promedio')
     elif 11<=Grade<=13:
          st.write('**Indice de construccion:**','Construccion y diseño de alta calidad')



##Inf datos en el filtro
st.title('Info de las casas:')

with st.expander("Resultados con valor igual al filtrado",expanded=0):
     if 'Precios' in OptFiltro:
          if Price>0:
               st.write('Hay {} casas con Valor igual a {}'.format(data[data['price']==Price].shape[0],Price))

     if 'Habitaciones' in OptFiltro:
          if Bedrooms>0:
               st.write('Hay {} casas con {} Habitacion/nes'.format(data[data['bedrooms']==Bedrooms].shape[0],Bedrooms))

     if 'Baños' in OptFiltro:
          if Bathrooms>0:
               st.write('Hay {} casas con {} baño/s'.format(data[data['bathrooms']==Bathrooms].shape[0],Bathrooms))

     if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
          if Mt2>0:
               st.write('Hay {} casas con {} metros cuadrados habitables'.format(data[data['sqft_living']==Mt2].shape[0],Mt2))

     if 'Pisos' in OptFiltro:
          if Floors>0:
               st.write('Hay {} casas con {} Piso/s construidos'.format(data[data['floors']==Floors].shape[0],Floors))

     if 'Vista al mar' in OptFiltro:
          if Waterfront ==1:
               st.write('Hay {} casas con vista al mar'.format(data[data['waterfront']==Waterfront].shape[0]))

     if 'Condicion' in OptFiltro:
          if Cond>0:
               st.write('Hay {} casas con una condicion igual a {}'.format(data[data['condition']==Cond].shape[0],Cond))

     if 'Indice de construccion' in OptFiltro:
          if Grade>0:
               st.write('Hay {} casas con un Indice de construccion igual a {}'.format(data[data['grade']==Grade].shape[0],Grade))

with st.expander("Resultados con valores mayor o igual al filtrado",expanded=0):
     if 'Precios' in OptFiltro:
          if Price>0:
               st.write('Hay {} casas con un valor igual o superior a {}'.format(data[data['price']>=Price].shape[0],Price))

     if 'Habitaciones' in OptFiltro:
          if Bedrooms>0:
               st.write('Hay {} casas con o más de {} Habitacion/nes'.format(data[data['bedrooms']>=Bedrooms].shape[0],Bedrooms))

     if 'Baños' in OptFiltro:
          if Bathrooms>0:
               st.write('Hay {} casas con o más de {} baño/s'.format(data[data['bathrooms']>=Bathrooms].shape[0],Bathrooms))

     if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
          if Mt2>0:
               st.write('Hay {} casas con o más de {} metros cuadrados habitables'.format(data[data['sqft_living']>=Mt2].shape[0],Mt2))

     if 'Pisos' in OptFiltro:
          if Floors>0:
               st.write('Hay {} casas con o más de {} Piso/s construido/s'.format(data[data['floors']>=Floors].shape[0],Floors))

     if 'Vista al mar' in OptFiltro:
          if Waterfront ==1:
               st.write('Hay {} casas con vista al mar'.format(data[data['waterfront']>=Waterfront].shape[0]))

     if 'Condicion' in OptFiltro:
          if Cond>0:
               st.write('Hay {} casas con una condicion mayor o igual a {}'.format(data[data['condition']>=Cond].shape[0],Cond))

     if 'Indice de construccion' in OptFiltro:
          if Grade>0:
               st.write('Hay {} casas con un Indice de construccion mayor o igual a {}'.format(data[data['grade']>=Grade].shape[0],Grade))

with st.expander("Cruce de datos filtrados",expanded=0):
     st.write('Proximamente! :sunglasses:')

## if 'Baños' in OptFiltro and 'Habitaciones' in OptFiltro:
##      if Bathrooms and Bedrooms>0:
##           st.write('Hay {} casas con {} habitacions y {} baños'.format(data[(data['bathrooms']>=Bathrooms) & (data['bedrooms'] >=Bedrooms )].shape[0],Bedrooms,Bathrooms))


##tercera parte // mostrar graficos
st.title('Graficas')

houses=data[['id','lat','long','price']]

Casas = px.scatter_mapbox(houses, lat="lat", lon="long", color="price",
                  color_continuous_scale=px.colors.sequential.RdBu, size_max=20, zoom=10,
                  mapbox_style="open-street-map")
st.write(Casas)

##Otrass opcion para ver el mapa  "open-street-map"   "carto-positron"

##pruebas
st.title('Pruebas')

valores={'Habitaciones':data['bedrooms'],'Pisos':data['floors'],'Baños':data['bathrooms']}
for k,v in valores.items():
     if 'Habitaciones' in OptFiltro:
          st.dataframe(data[v==v.max()])
          st.write(data[v==v.max()].shape[0])
          st.write(v.mean())
          st.write(v.mode())
          st.write(v.median())
          st.write(v.min())
          st.write(v.max())


    


