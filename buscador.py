import streamlit as st

def faz_busca(df):
    pesquisa = st.text_input('Digite sua pesquisa:')
    if pesquisa:
        dados_filtrados = df[df.apply(lambda row: row.astype(str).str.contains(pesquisa, case=False).any(), axis=1)]
        st.write(f"Resultados para '{pesquisa}':")
        st.dataframe(dados_filtrados)
    else:
        st.write("Digite algo na barra de pesquisa para ver os resultados.")