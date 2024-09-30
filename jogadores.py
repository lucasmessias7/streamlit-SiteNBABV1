import pandas as pd
import streamlit as st
import plotly


dados_jogadores = pd.read_csv('dados/dados_jogadores_23-24.csv', delimiter=';')


def pesquisa():
    st.text_input('Digite sua pesquisa: ')

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


filtro = ['Tudo','Pontos','Rebotes', 'Assistencias']

filtrado = st.sidebar.selectbox('NBA', filtro)

if filtrado == 'Tudo':
    st.title('Todos os dados dos jogadores')
    dados_jogadores

if filtrado == 'Pontos':
    st.title('Pontos por Jogador')
    pontos


if filtrado == 'Rebotes':
    st.title('Rebotes por jogador')
    rebotes

if filtrado == 'Assistencias':
    st.title('Assistência por jogador')
    assistencias
# aba1, aba2, aba3 = st.tabs(['Pontos', 'Rebotes', 'Assistencias'])



# with aba1:
#     pontos

# with aba2:
#     rebotes

# with aba3:
#     assistencias