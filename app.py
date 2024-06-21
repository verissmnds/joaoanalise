import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import streamlit as st

st.set_page_config(page_title="Análise do Instagram de João Campos", page_icon="📐", layout="wide")

st.title('Análise do Instagram de João Campos')

df = joao_df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("As 10 publicações com maior taxa de engajamento:")
st.dataframe(df)

st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

if __name__ == '__main__':
    main()
