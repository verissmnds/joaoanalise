import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

st.set_page_config(page_title="Análise do Instagram de João Campos", page_icon="📐", layout="wide")

st.title('Análise do Instagram de João Campos')

df = joao_df.sort_values(by='Post interaction rate', ascending=False).head(10)

    st.header("As 10 publicações com maior taxa de engajamento:")
    st.dataframe(df)

    st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

stopwords = []
with open('stopjoao.txt', 'r') as arquivo_de_stopwords:
    for linha in arquivo_de_stopwords:
        stopwords.append(linha.strip())  # Use strip para remover novas linhas e espaços em branco

def limpar_texto(texto):
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    texto = re.sub(r'\d+', '', texto)      # Remove números
    texto = texto.lower()                  # Converte para minúsculas
    return texto

texto = joao_df['Message'].dropna().apply(limpar_texto)

palavras = ' '.join(texto).split()

palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

dicionario_palavras = Counter(palavras_sem_stopwords)

wordcloud = WordCloud(width=800, height=400, background_color='white')
wordcloud.generate_from_frequencies(dicionario_palavras)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


if __name__ == '__main__':
    main()
