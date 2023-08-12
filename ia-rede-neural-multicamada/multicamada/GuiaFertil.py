import csv
from pathlib import Path

import numpy as np
from sklearn import preprocessing


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

lista_registro = []
registro = []

CAMINHO_CSV = Path(__file__).parent / 'analise_solo.csv'
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        registro.append(float(linha['ph']))
        registro.append(float(linha['ctc']))
        registro.append(float(linha['v']))
        registro.append(float(linha['to']))
        registro.append(float(linha['ta']))
        lista_registro.append(registro)
        registro = []

analise_solo  = np.array(lista_registro)

lista_registro = []

CAMINHO_CSV = Path(__file__).parent / 'produtividade.csv'
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        registro.append(float(linha['produtividade']))
        lista_registro.append(registro)
        registro = []
produtividade = np.array(lista_registro) 

entradas_minmax = preprocessing.MinMaxScaler().fit(analise_solo)
entradas = entradas_minmax.transform(analise_solo)

saidas_minmax = preprocessing.MinMaxScaler().fit(produtividade)
saidas = saidas_minmax.transform(produtividade)

pesos0 = 2*np.random.random((5,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1
epocas = 4000
taxaAprendizagem = 0.5
momento = 1

camadaSaida = [[]]
for j in range(epocas):
    if (j==1):
        print('Processamento.....')

    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)

    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))

    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida

    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

    camadaOcultaTransposta = camadaOculta.T
    ed1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (ed1 * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    ed0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (ed0 * taxaAprendizagem)
    
print('***** Processo Finalizado *****')
print('')
print('=================================================================')
print('')
print('Analises de Solo (camada de Entrada): [ pH, CTC, V, MO, TA ]')
print('')
print(str(analise_solo))
print('')
print('Dados de Entrada Normalizados:')
print(str(entradas))
print('=================================================================')
print('')
print('Produtividade (camada de Saída): [ kg / ha ]')
print('')
print(str(produtividade))
print('')
print('Dados de saída Normalizados:')
print(str(saidas))
print('=================================================================')
print('')
print('Pesos ajustados da Camada de Entrada para Camada Oculta:')
print('')
print(str(pesos0))
print('')
print('=================================================================')
print('')
print('Pesos ajustados de Camada Oculta para Camada de Saída:')
print('')
print(str(pesos1))
print('')
print('=================================================================')
print('')
print("Erro.......: " + str(mediaAbsoluta*100))
print("Precição...: " + str(100-(mediaAbsoluta*100)))
print('')
print('=================================================================')
print('Saida Esperada:')
print(str(saidas))
print('')
print('Camada de Saída:')
print(str(camadaSaida))
