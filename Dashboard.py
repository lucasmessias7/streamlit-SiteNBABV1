import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.write('NBA Estatística')


dados_jogadores = pd.read_csv('pontos_tres.csv', delimiter=';')
dados = pd.read_csv('jogadores_atualizados-0.1.csv', delimiter=';')
st.dataframe(dados)
st.dataframe(dados_jogadores)
