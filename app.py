import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.title("Análisis de Datos de Vehículos")

if st.checkbox("Mostrar datos"): 
    st.write(df.head())

st.subheader("Distribución de precios")
fig, ax = plt.subplots()
df['price'].hist(bins=30, ax=ax)
st.pyplot(fig)

def update():
    st.rerun()

st.button("Actualizar", on_click=update)

if st.button("Mostrar gráfico de dispersión"):
    st.subheader("Relación entre precio y año del vehículo")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='model_year', y='price', alpha=0.5, ax=ax)
    st.pyplot(fig)