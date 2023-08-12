# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV_01 = Path(__file__).parent / 'aula_exemplo_01_295.csv'
CAMINHO_CSV_02 = Path(__file__).parent / 'aula_exemplo_02_295.csv'
CAMINHO_CSV_03 = Path(__file__).parent / 'aula_exemplo_03_295.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

lista_clientes2 = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]

print('Exemplo 01:')
with open(CAMINHO_CSV_01, 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)

    nome_colulas = lista_clientes[0].keys()

    escritor.writerow(nome_colulas)
    for cliente in lista_clientes:
        print(cliente.values())
        escritor.writerow(cliente.values())

print('Arquivo Gerado!')
print('========================================')

print('Exemplo 02:')
with open(CAMINHO_CSV_02, 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)

    nome_colulas2 = ['Nome', 'Endereço']

    escritor.writerow(nome_colulas2)
    for cliente2 in lista_clientes2:
        print(cliente2)
        escritor.writerow(cliente2)
print('Arquivo Gerado!')
print('========================================')

print('Exemplo 03:')

with open(CAMINHO_CSV_03, 'w', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()

    escritor2 = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor2.writeheader()

    for cliente3 in lista_clientes:
        print(cliente3.values())
        escritor2.writerow(cliente3)
print('Arquivo Gerado!')
print('========================================')
