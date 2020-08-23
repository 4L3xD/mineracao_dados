import pandas as pd
import xlrd

df = pd.read_excel('pao-pra-ja.xlsx') 

print(df)

for i in df.index:
    if df['Café'][i] == 'sim':
      print('Clientes que compraram café: {} '.format(df['N'][i]))


# Análise por linha (quais produtos cada cliente consumiu)
# Análise por coluna (quantos clientes consumiram determinado produto)
