import pandas as pd
import streamlit as st

df = pd.read_excel('posts1.xlsx')

joao_df = df[df['Profile'] == 'João Campos']

st.set_page_config(page_title="Análise do Instagram de João Campos", page_icon="📐", layout="wide")

st.title('Análise do Instagram de João Campos')

df2 = joao_df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

url_imagem = 'fotojoao.png'
st.image(url_imagem)

st.header("As 10 publicações com maior taxa de engajamento:")
st.markdown("Na análise eu foquei apenas nas três primeiras publicações:")
st.markdown("1° https://www.instagram.com/reel/C3Gg_eORsFk/")
st.markdown("2° https://www.instagram.com/reel/C2kZVN2u8RQ/")
st.markdown("3° https://www.instagram.com/reel/CxiI9Z0OXfM/")

st.dataframe(df2)
