import pandas as pd
import xlrd
import json
import os.path

oftalmo = pd.read_excel('oftalmo.xlsx',sheet_name='Página1', usecols=['ID', 'Idade', 'Diagnóstico', 'Astigmatismo', 'Produção lacrimal', 'Lentre prescrita'])

paciente = oftalmo.to_dict(orient='records')

def escrever_json(lista):
    with open('data.json', 'w') as f:
        json.dump(lista, f)

escrever_json(paciente)

def carregar_json(arquivo):
    try:
      with open('data.json', 'r') as f:
        return json.load(f)
    except IOError:
        ('Arquivo não carregado!')

data = pd.read_json('data.json')

paciente = data.to_dict(orient='records')

id_nenhuma = []
id_rigida = []
id_gelatinosa = []

for info in range(23):
  lente = (paciente[info]['Lentre prescrita'])
  if lente == 'nenhuma':
    id_nenhuma.append(paciente[info]['ID'])
  if lente == 'gelatinosa':
    id_gelatinosa.append(paciente[info]['ID'])
  if lente == 'rígida':
    id_rigida.append(paciente[info]['ID'])
print('Nenhuma lente: ', id_nenhuma)
print('Lentes gelatinosas: ', id_gelatinosa)
print('Lentes rígidas: ', id_rigida)