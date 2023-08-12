# Empacotamento e desempacotamento de dicionários
print('Exemplo:01')
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
print('=========')

print('Exemplo:02')
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
a, b = pessoa
print(a,b)
a, b = pessoa.values()
print(a, b)
a, b = pessoa.items()
print(a, b)
(a1,a2), (b1,b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
for chave, valor in pessoa.items():
     print(chave, valor)
print('=========')

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

print('Exemplo:03')
pessoas_completa = {**pessoa, 'sexo':'feminino',**dados_pessoa}
print(pessoas_completa)
print('=========')

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

print('Exemplo:04')
def mostro_argumentos_nomeados(*args, **kwargs):
    if len(args)>0:
        print('Paramentros não nomeados p1, p2, p3, ... ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Dário', idade='45', sexo='masculino')
mostro_argumentos_nomeados(1, 2, 3, nome='Dário', idade='45', sexo='masculino')
print('=========')

print('Exemplo:05')
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
print('=========')