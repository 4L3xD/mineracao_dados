import pandas as pd
import xlrd

padaria = pd.read_excel('pao-pra-ja.xlsx') 
print(padaria)

produtos = ['Leite', 'Café',  'Pão', 'Mortadela', 'Suco', 'Manteiga']
venda = ['']
cliente = []

print('\n')
for i in padaria.index:
  consumo = ['']
  for produto in produtos:
      if padaria[produto][i] == 'sim':
        consumo.append([[padaria['N'][i]], [produto]]) 
        print('Nº do consumidor de {}:  {}'.format(produto, padaria['N'][i]))
        print(consumo)

print('Produtos consumidos: {}'.format(produto))

    

# Análise por linha (quais produtos cada i consumiu)
# Análise por coluna (quantos is consumiram determinado produto)
