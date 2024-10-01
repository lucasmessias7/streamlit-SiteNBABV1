import pandas as pd
import streamlit as st
import plotly


dados_times = pd.read_csv('dados/dados_times_23-24.csv', delimiter=';')
team_team = pd.read_csv('dados/teamVSteam_23-24.csv', delimiter=';')

dados_times = dados_times.rename(columns={
    'Unnamed: 0' : 'Posição',
    'Unnamed: 1' : 'Time',
    'Unnamed: 2' : 'Geral',
    'Vitorias' : 'Em casa',
    'Vitorias.1' : 'Fora de casa',
    'Conference' : 'Contra Leste',
    'Conferencia' : 'Contra Oeste'
}).drop(columns=['Mês','Mês.1','Mês.2','Mês.3','Mês.4','Mês.5','Mês.6'])

team_team = team_team.rename(columns={'ATL' : 'Atlanta Hawks',
    'BOS' : 'Boston Celtics',
    'BRK' : 'Brooklyn Nets',
    'CHI' : 'Chicago Bulls',
    'CHO' : 'Charlotte Hornets',
    'CLE' : 'Cleveland Cavaliers',
    'DAL' : 'Dallas Mavericks',
    'DEN' : 'Denver Nuggets',
    'DET' : 'Detroit Pistons',
    'GSW' : 'Golden State Warriors',
    'HOU' : 'Houston Rockets',
    'IND' : 'Indiana Pacers',
    'LAC' : 'Los Angeles Clippers',
    'LAL' : 'Los Angeles Lakers',
    'MEM' : 'Memphis Grizzlies',
    'MIA' : 'Miami Heat',
    'MIL' : 'Milwaukee Buckes',
    'MIN' : 'Minnesota Timberwolves',
    'NOP' : 'New Orleans Pelicans',
    'NYK' : 'New York Knicks',
    'OCK' : 'Oklahoma City Thunder',
    'ORL' : 'Orlando Magic',
    'PHI' : 'Philadelphia 76ers',
    'PHO' : 'Phoenix Suns',
    'POR' : 'Portland Trail Blazers',
    'SAC' : 'Sacramento Kings',
    'SAS' : 'San Antonio Spurs',
    'TOR' : 'Toronto Raptors',
    'UTA' : 'Utah Jazz',
    'WAS' : 'Washington Wizards'})





def busca_time(df):
    pesquisa = st.text_input('Digite o  nome do time:')
    if pesquisa:
        dados_filtrados = df[df.apply(lambda row: row.astype(str).str.contains(pesquisa, case=False).any(), axis=1)]
        st.write(f"Resultados para '{pesquisa}':")
        st.dataframe(dados_filtrados)
    else:
        st.write("Digite algo na barra de pesquisa para ver os resultados.")



st.title('Dados dos Times na temporada 23-24')


filtro_time = ['Confrontos','Vitorias']
filtrado_time = st.sidebar.selectbox('Dados', filtro_time)



if filtrado_time == 'Confrontos':
    st.title('Confrontos')
    busca_time(team_team)



if filtrado_time == 'Vitorias':
    st.title('Vitórias e derrotas ')
    busca_time(dados_times)