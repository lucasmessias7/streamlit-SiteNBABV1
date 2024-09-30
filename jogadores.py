import pandas as pd
import streamlit as st
import plotly

dados_jogadores = pd.read_csv('dados/dados_jogadores_23-24.csv', delimiter=';')
st.title('Dados jogadores')



pontos = dados_jogadores[[
     'Jogador',
    'Equipe',
    'Minutos jogados',
    'Taxa de acerto total',
    'Pontos de 3 convertidos',
    'Pontos de 3 tentados',
    'Taxa de acerto de 3 pontos',
    'Pontos por jogo'
]]
rebotes = dados_jogadores[[
    'Jogador',
    'Equipe',
    'Minutos jogados',
    'Rebotes'
]]
assistencias = dados_jogadores[[
    'Jogador',
    'Equipe',
    'Minutos jogados',
    'Assistencias'
]]


paginas = ['all', 'Pontos', 'Rebotes', 'Assistencias']
st.sidebar.title('Filtro')
dados = st.sidebar.selectbox('Selecione o filtro:', paginas)

if dados == 'all':
    dados = dados_jogadores


    


aba1, aba2, aba3 = st.tabs(['Pontos', 'Rebotes', 'Assistencias'])



with aba1:
    pontos

with aba2:
    rebotes

with aba3:
    assistencias