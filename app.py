import pandas as pd
import streamlit as st

df = pd.read_excel('posts1.xlsx')

st.set_page_config(page_title="Análise do Instagram de João Campos", page_icon="📐", layout="wide")

st.title('Análise do Instagram de João Campos')

df2 = df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

url_imagem = 'fotojoao.png'
st.image(url_imagem)

st.header("As 10 publicações com maior taxa de engajamento:")
st.markdown("Na análise eu foquei apenas nas três primeiras publicações.")
st.dataframe(df2)
