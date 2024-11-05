import pandas as pd
import streamlit as st
import plotly


dados_jogadores = pd.read_csv('dados/dados_jogadores25-26.csv', delimiter=';', encoding='latin1')


def faz_busca(df):
    pesquisa = st.text_input('Digite sua pesquisa:')
    if pesquisa:
        dados_filtrados = df[df.apply(lambda row: row.astype(str).str.contains(pesquisa, case=False).any(), axis=1)]
        st.write(f"Resultados para '{pesquisa}':")
        st.dataframe(dados_filtrados)
    else:
        st.write("Digite algo na barra de pesquisa para ver os resultados.")

dados_jogadores.rename(columns={
                        'Player' : 'Jogador',
                        'Team' : 'Equipe',
                        'Pos' : 'Posição',
                        'G' : 'Jogos',
                        'GS' : 'Jogos Iniciados',
                        'MP' : 'Minutos Jogados',
                        'FG' : 'Cestas totais',
                        'FGA' : 'Cestas tentadas totais',
                        'FG%' : 'Porcentagem de cestas',
                        '3P' : 'Cestas de 3 pontos',
                        '3PA' : 'Tentativas de cestas de 3',
                        '3P%' : 'Porcentagem de cestas de 3 pontos',
                        '2P' : 'Cestas de 2 pontos',
                        '2PA' : 'Tentativas de cestas de 2 pontos',
                        '2P%' : 'Porcentagem de cestas de 2 pontos',
                        'FT' : 'Lances livres',
                        'FTA' : 'Tentativas de lances livres',
                        'FT%' : 'Porcentagem de lances livres',
                        'ORB' : 'Rebotes ofensivos',
                        'DRB' : 'Rebotes defensivos',
                        'TRB' : 'Rebotes totais',
                        'AST' : 'Assistências',
                        'STL' : 'Roubos de bola',
                        'BLK' : 'Bloqueios',
                        'TOV' : 'Perdas de bola',
                        'PF' : 'Faltas pessoais',
                        'PTS' : 'Pontos'
                    }, inplace=True

                       )







rebotes = dados_jogadores[[
    'Jogador',
    'Equipe',
    'Minutos Jogados',
    'Rebotes ofensivos',
    'Rebotes defensivos',
    'Rebotes totais'
]]



assistencias = dados_jogadores[[
    'Jogador',
    'Equipe',
    'Minutos Jogados',
    'Assistências'
]]


filtro = ['Dados gerais','Rebotes', 'Assistencias']
filtrado = st.sidebar.selectbox('NBA', filtro)


if filtrado == 'Dados gerais':
    st.title('Dados gerais')
    faz_busca(dados_jogadores)
    dados_jogadores

if filtrado == 'Rebotes':
    st.title('Rebotes por jogador')
    faz_busca(rebotes)
    rebotes

if filtrado == 'Assistencias':
    st.title('Assistência por jogador')
    faz_busca(assistencias)
    assistencias
