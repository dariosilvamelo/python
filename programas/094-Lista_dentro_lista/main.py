"""
Lista de listas e seus índices
"""
salas1 = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (10,20,30,40,50)],  # 2
]

print(salas1[1][0])
print(salas1[0][1])
print(salas1[2][2])
print(salas1[2][3][3])

print('================')

salas2 = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda']  # 2
]


for sala in salas2:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)