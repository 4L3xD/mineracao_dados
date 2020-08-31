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

id_astigmatismo = []
id_producao_lacrimal = []
id_diagnostico = []

id_idade_jovem = []
id_idade_prePresbiopico = []
id_idade_presbiópico = []

for info in range(23):
  lente = paciente[info]['Lentre prescrita']
  if lente == 'nenhuma':
    id_nenhuma.append(paciente[info]['ID'])
  if lente == 'gelatinosa':
    id_gelatinosa.append(paciente[info]['ID'])
  if lente == 'rígida':
    id_rigida.append(paciente[info]['ID'])
  
  astigmatismo = paciente[info]['Astigmatismo']
  if astigmatismo == 'sim':
    id_astigmatismo.append(paciente[info]['ID'])
  
  idade = paciente[info]['Idade']
  if idade == 'Jovem':
    id_idade_jovem.append(paciente[info]['ID'])
  if idade == 'pre-presbiópico':
    id_idade_prePresbiopico.append(paciente[info]['ID'])
  if idade == 'presbiópico':
    id_idade_presbiópico.append(paciente[info]['ID'])

  producao_lacrimal = paciente[info]['Produção lacrimal']
  if producao_lacrimal == 'reduzida':
    id_producao_lacrimal.append(paciente[info]['ID'])

  diagnostico = paciente[info]['Diagnóstico']
  if diagnostico == 'hipermetrope':
    id_diagnostico.append(paciente[info]['ID'])

id_idades = ['Jovem: {}'.format(id_idade_jovem), 'pre-presbiópico: {}'.format(id_idade_prePresbiopico), 'presbiópico: {}'.format(id_idade_presbiópico)]

nenhuma_astigmatismo = []
nenhuma_prodLacReduzida = []
nenhuma_diagHipermetrope = []
nenhuma_jovem = []
nenhuma_prePresbiopico = []
nenhuma_presbiópico = []

for nenhumaLente in range(len(id_nenhuma)):
  for astig in range(len(id_astigmatismo)):
    if id_nenhuma[nenhumaLente] == id_astigmatismo[astig]:
      nenhuma_astigmatismo.append(id_astigmatismo[astig])
  for prodLacrimal in range(len(id_nenhuma)):
    if id_nenhuma[nenhumaLente] == id_producao_lacrimal[prodLacrimal]:
      nenhuma_prodLacReduzida.append(id_producao_lacrimal[prodLacrimal])
  for diagnost in range(len(id_diagnostico)):
    if id_nenhuma[nenhumaLente] == id_diagnostico[diagnost]:
      nenhuma_diagHipermetrope.append(id_diagnostico[diagnost])
  for jovem in range(len(id_idade_jovem)):
    if id_nenhuma[nenhumaLente] == id_idade_jovem[jovem]:
      nenhuma_jovem.append(id_idade_jovem[jovem])
  for prePresbiopico in range(len(id_idade_prePresbiopico)):
    if id_nenhuma[nenhumaLente] == id_idade_prePresbiopico[prePresbiopico]:
      nenhuma_prePresbiopico.append(id_idade_prePresbiopico[prePresbiopico])
  for presbiópico in range(len(id_idade_presbiópico)):
    if id_nenhuma[nenhumaLente] == id_idade_presbiópico[presbiópico]:
      nenhuma_presbiópico.append(id_idade_presbiópico[presbiópico])

rigida_astigmatismo = []
rigida_prodLacReduzida = []
rigida_diagHipermetrope = []
rigida_jovem = []
rigida_prePresbiopico = []
rigida_presbiópico = []

for lenteRigida in range(len(id_rigida)):
  for astig in range(len(id_astigmatismo)):
    if id_rigida[lenteRigida] == id_astigmatismo[astig]:
      rigida_astigmatismo.append(id_astigmatismo[astig])
  for prodLacrimal in range(len(id_rigida)):
    if id_rigida[lenteRigida] == id_producao_lacrimal[prodLacrimal]:
      rigida_prodLacReduzida.append(id_producao_lacrimal[prodLacrimal])
      # Output: Lente rígida + produção lacrimal reduzida: [7] ERR: output correto [7, 15]
  for diagnost in range(len(id_diagnostico)):
    if id_rigida[lenteRigida] == id_diagnostico[diagnost]:
      rigida_diagHipermetrope.append(id_diagnostico[diagnost])
  for jovem in range(len(id_idade_jovem)):
    if id_rigida[lenteRigida] == id_idade_jovem[jovem]:
      rigida_jovem.append(id_idade_jovem[jovem])
  for prePresbiopico in range(len(id_idade_prePresbiopico)):
    if id_rigida[lenteRigida] == id_idade_prePresbiopico[prePresbiopico]:
      rigida_prePresbiopico.append(id_idade_prePresbiopico[prePresbiopico])
  for presbiópico in range(len(id_idade_presbiópico)):
    if id_rigida[lenteRigida] == id_idade_presbiópico[presbiópico]:
      rigida_presbiópico.append(id_idade_presbiópico[presbiópico])

print('='*60)
print('Análise de variáveis por ID')
print('='*60)
print('\nTipos de lentes: \n Nenhuma: {}, Gelatinosa: {}, Rígida: {}\n'.format(len(id_nenhuma), len(id_gelatinosa), len(id_rigida)))

print(' IDs:\n  Nenhuma lente: ', id_nenhuma)
print('  Lentes gelatinosas: ', id_gelatinosa)
print('  Lentes rígidas: ', id_rigida)
print('\n')
print('Astigmatismo:\n Total: {}\n IDs: {}\n'.format(len(id_astigmatismo), id_astigmatismo))
print('Idade:\n Total:{}\n IDs: {}\n'.format(len(id_idades), id_idades))
print('Diagnóstico:\n Total hipermetropes: {}\n Total míopes: {}\n IDs hipermetropes: {}\n'.format(len(id_diagnostico), 23-len(id_diagnostico), id_diagnostico))
print('Produção lacrimal:\n Total reduzida: {}\n IDs reduzida: {}\n Total normal: {}\n'.format(len(id_producao_lacrimal), id_producao_lacrimal, 23-len(id_producao_lacrimal)))

print('='*60)
print('Lente: NENHUMA:')
print('='*60)
print('Nenhuma lente + astigmatismo: {}'.format(nenhuma_astigmatismo))
print('Nenhuma lente + produção lacrimal reduzida: {}'.format(nenhuma_prodLacReduzida))
print('Nenhuma lente + hipermetropia: {}'.format(nenhuma_diagHipermetrope))
print('Nenhuma lente em jovens: {}'.format(nenhuma_jovem))
print('Nenhuma lente em prePresbiopico: {}'.format(nenhuma_prePresbiopico))
print('Nenhuma lente em presbiopico: {}'.format(nenhuma_presbiópico))

print('='*60)
print('Lente: RÍGIDA:')
print('='*60)
print('Lente rígida + astigmatismo: {}'.format(rigida_astigmatismo))
print('Lente rígida + produção lacrimal reduzida: {}'.format(rigida_prodLacReduzida))
print('Lente rígida + hipermetropia: {}'.format(rigida_diagHipermetrope))
print('Lente rígida em jovens: {}'.format(rigida_jovem))
print('Lente rígida em prePresbiopico: {}'.format(rigida_prePresbiopico))
print('Lente rígida em presbiopico: {}'.format(rigida_presbiópico))

#print('='*60)
#print('Lente: NENHUMA:')
#print('='*60)
#print('Nenhuma lente + astigmatismo: {}'.format#(nenhuma_astigmatismo))
#print('Nenhuma lente + produção lacrimal reduzida: {}#'.format(nenhuma_prodLacReduzida))
#print('Nenhuma lente + hipermetropia: {}'.format#(nenhuma_diagHipermetrope))
#print('Nenhuma lente em jovens: {}'.format#(nenhuma_jovem))
#print('Nenhuma lente em prePresbiopico: {}'.format#(nenhuma_prePresbiopico))
#print('Nenhuma lente em presbiopico: {}'.format#(nenhuma_presbiópico))