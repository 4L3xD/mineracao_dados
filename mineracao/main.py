import pandas as pd
import xlrd

df = pd.read_excel('pao-pra-ja.xlsx') 
print(df)

produtos = ['Leite', 'Café',  'Pão', 'Mortadela', 'Suco', 'Manteiga']

print('\n')
for i in df.index:
  for produto in produtos:
    if df[produto][i] == 'sim':
      print('Clientes que compraram {}: {} '.format(produto, df['N'][i]))

# Análise por linha (quais produtos cada cliente consumiu)
# Análise por coluna (quantos clientes consumiram determinado produto)
