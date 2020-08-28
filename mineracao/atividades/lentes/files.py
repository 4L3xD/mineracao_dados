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

print(carregar_json('data.json')) 

data = pd.read_json('data.json')