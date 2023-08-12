# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


alunos_02 = ['a','a','a','a','b','b','c','a']  
grupos_02 = groupby(sorted(alunos_02))

print('Exemplo 01:')
for chave, valor in grupos_02:
    print(chave)
    print(list(valor))
print('==================')
print(' ')
print('Exemplo 02:')
def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena) # para mostrar qual coluna dever ser ordenada
grupos = groupby(alunos_agrupados, key=ordena) # para mostrar qual coluna deve ser agrupada

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
print('==================')        

