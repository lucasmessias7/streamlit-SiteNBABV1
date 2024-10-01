import pandas as pd
import streamlit as st
import plotly


dados_jogadores = pd.read_csv('dados/dados_jogadores_23-24.csv', delimiter=';')



def faz_busca(df):
    pesquisa = st.text_input('Digite sua pesquisa:')
    if pesquisa:
        dados_filtrados = df[df.apply(lambda row: row.astype(str).str.contains(pesquisa, case=False).any(), axis=1)]
        st.write(f"Resultados para '{pesquisa}':")
        st.dataframe(dados_filtrados)
    else:
        st.write("Digite algo na barra de pesquisa para ver os resultados.")

    




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


filtro = ['Pontos','Rebotes', 'Assistencias']

filtrado = st.sidebar.selectbox('NBA', filtro)


if filtrado == 'Pontos':
    st.title('Pontos por Jogador')
    faz_busca(pontos)
    pontos


if filtrado == 'Rebotes':
    st.title('Rebotes por jogador')
    faz_busca(rebotes)
    rebotes

if filtrado == 'Assistencias':
    st.title('Assistência por jogador')
    faz_busca(assistencias)
    assistencias
# aba1, aba2, aba3 = st.tabs(['Pontos', 'Rebotes', 'Assistencias'])



# with aba1:
#     pontos

# with aba2:
#     rebotes

# with aba3:
#     assistencias