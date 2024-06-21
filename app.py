import pandas as pd
import streamlit as st

pip install openpyxl

df = pd.read_excel('posts1.xlsx')

st.set_page_config(page_title="Análise do Instagram de João Campos", page_icon="📐", layout="wide")

st.title('Análise do Instagram de João Campos')

df2 = joao_df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("As 10 publicações com maior taxa de engajamento:")
st.dataframe(df2)

st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

if __name__ == '__main__':
    main()
