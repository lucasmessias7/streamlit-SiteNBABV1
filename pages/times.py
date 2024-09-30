import pandas as pd
import streamlit as st
import plotly

st.title('Dados dos Times na temporada 23-24')

dados_times = pd.read_csv('dados/dados_times_23-24.csv', delimiter=';')

st.dataframe(dados_times)