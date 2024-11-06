import json
import pandas as pd
import streamlit as st
import numpy as np
from buscador import faz_busca

with open('dados/dados_tabela.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)
df = pd.DataFrame(dados_json)
df = df.rename(columns= {
                        0 : 'Jogador',
                        1 : 'idade',
                        2 : 'Equipe',
                        3 : 'Posição',
                        4 : 'Jogos',
                        5 : 'Jogos Iniciados',
                        6 : 'Minutos Jogados',
                        7 : 'Cestas totais',
                        8 : 'Cestas tentadas totais',
                        9 : 'Porcentagem de cestas',
                        10 : 'Cestas de 3 pontos',
                        11 : 'Tentativas de cestas de 3',
                        12 : 'Porcentagem de cestas de 3 pontos',
                        13 : 'Cestas de 2 pontos',
                        14 : 'Tentativas de cestas de 2 pontos',
                        15 : 'Porcentagem de cestas de 2 pontos',
                        16 : 'EFG%',
                        17 : 'Lances livres',
                        18 : 'Tentativas de lances livres',
                        19 : 'Porcentagem de lances livres',
                        20 : 'Rebotes ofensivos',
                        21 : 'Rebotes defensivos',
                        22 : 'Rebotes totais',
                        23 : 'Assistências',
                        24 : 'Roubos de bola',
                        25 : 'Bloqueios',
                        26 : 'Perdas de bola',
                        27 : 'Faltas pessoais',
                        28 : 'Pontos'
})


rebotes = df[[
    'Jogador',
    'Equipe',
    'Minutos Jogados',
    'Rebotes ofensivos',
    'Rebotes defensivos',
    'Rebotes totais'
]]

assistencias = df[[
    'Jogador',
    'Equipe',
    'Minutos Jogados',
    'Assistências'
]]

pontos = df[[
    'Jogador',
    'Equipe',
    'Minutos Jogados',
    'Cestas totais',
    'Cestas tentadas totais',
    'Cestas de 3 pontos',
    'Tentativas de cestas de 3',
    'Porcentagem de cestas de 3 pontos',
    'Cestas de 2 pontos',
    'Tentativas de cestas de 2 pontos',
    'Porcentagem de cestas de 2 pontos',

]]


filtro = ['Dados gerais','Pontos','Rebotes', 'Assistencias']
filtrado = st.sidebar.selectbox('NBA', filtro)


if filtrado == 'Dados gerais':
    st.title('Dados gerais')
    faz_busca(df)
    df

if filtrado == 'Rebotes':
    st.title('Rebotes por jogador')
    faz_busca(rebotes)
    rebotes

if filtrado == 'Assistencias':
    st.title('Assistência por jogador')
    faz_busca(assistencias)
    assistencias

if filtrado == 'Pontos':
    st.title('Pontos por jogador')
    faz_busca(pontos)
    pontos