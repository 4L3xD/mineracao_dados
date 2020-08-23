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

# Análise por linha (quais produtos cada cliente consumiu)
# Análise por coluna (quantos clientes consumiram determinado produto)
# Frequência de compra de cada ítem: Análise de coluna(ordem dos clientes que compraram o produto)
# Produtos que podem ser comprados juntos: Análise de frequência de combinação entre produtos
# Produtos que SEMPRE são comprados juntos: Análise de frequência de combinação entre produtos (produtos com 100% de combinações entre si)
# Produtos que NUNCA são comprados juntos: Análise de frequência de combinação entre produtos (produtos com 0% combinações entre si)