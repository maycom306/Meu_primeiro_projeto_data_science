import pandas as pd
import sqlite3
from datetime import datetime as dt
import json

# Caminho relativo para o arquivo JSON Lines
file_path = 'data.jsonl'

df = pd.read_json(file_path, lines=True)
# Exibir o DataFrame]
pd.options.display.max_columns = None

df['_source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'
df['_data_coleta'] = dt.now()


df['preço_reais'] = df['preço_reais'].fillna(0).astype(float)
df['preço_centavos'] = df['preço_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

df['preço'] = df['preço_reais'] + df['preço_centavos'] / 100

conn = sqlite3.connect('quotes.db')
df.to_sql('quotes', conn, if_exists='append', index=False)
conn.close()

print(df.head())
