import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

dados = pd.read_csv('dados.csv')

# Cria o painel lateral na esquerda da tela
st.sidebar.header('Filtro')

# Adiciona o widget de seleção única ao painel lateral
filtro0 = st.sidebar.selectbox('Selecione um valor:', dados['ORDERNUMBER'].unique())
filtro1 = st.sidebar.slider('selecione os filtro1', value=[0, 100])

# Filtra os dados
dados = dados[dados['ORDERNUMBER'] == filtro0]
dados = dados[dados['PRICEEACH'] >= filtro1[0]]
dados = dados[dados['PRICEEACH'] <= filtro1[1]]

st.dataframe(dados)
