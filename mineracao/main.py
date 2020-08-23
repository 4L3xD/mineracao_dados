import pandas as pd
import xlrd

padaria = pd.read_excel('pao-pra-ja.xlsx') 
print(padaria)

produtos = ['Leite', 'Café',  'Pão', 'Mortadela', 'Suco', 'Manteiga']

print('\n')
for i in padaria.index:
  consumo = []
  for produto in produtos:
      if padaria[produto][i] == 'sim':
        consumo.append(produto) 
  print('Consumidor: {} → Produtos: {}.'.format(padaria['N'][i], consumo))

# Análise por linha (quais produtos cada i consumiu)
# Análise por coluna (quantos is consumiram determinado produto)