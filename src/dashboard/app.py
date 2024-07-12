import streamlit as st 
import pandas as pd 
import sqlite3

conn = sqlite3.connect('../transformacao/quotes.db')

df = pd.read_sql_query("SELECT * FROM quotes", conn)
conn.close()

#ADCIONAR TITULO 
st.title('pesquisas no Mercado Livre - Tenis de corrida') 
st.subheader('KPIs principais do sistema')
# KPI's
total_itens = df.shape[0]
col1, col2, col3 = st.columns(3)

# KPIs numero total de itens
col1.metric(label='Número Total de Itens', value=total_itens)

unique_brands = df['brand'].nunique()
col2.metric(label='Quantidade de Marcas Unicas', value=unique_brands)
# KPI quantidade de marcas unicas
average_price = df['preço'].mean()
col3.metric(label = 'preço médio (R$)', value=f'{average_price:.2f}')

#Marcas mais encontradas nas 10 paginas
st.subheader('Marcas mais encontradas ate a pagina 10')
col1, col2 = st.columns([4, 2])
top_10 = df['brand'].value_counts().sort_values(ascending=False)

col1.bar_chart(top_10)
col2.write(top_10)

#preço medio por marca
st.subheader('preço medio por marca')
col1, col2 = st.columns([4, 2])
preco_medio = df.groupby('brand')['preço'].mean().sort_values(ascending=False)
col1.bar_chart(preco_medio)
col2.write(preco_medio)

#satisfaçabilidade por marca
st.subheader('satisfacaça por marca')
col1, col2 = st.columns([4, 2])
df_zero_review = df[df['reviews_rating_number'] > 0]
satisfacao = df_zero_review.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfacao)
col2.write(satisfacao)