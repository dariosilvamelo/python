# Dictionary Comprehension e Set Comprehension

print('Exemplo 01:')
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
for chave, valor in produto.items():
    print(chave, valor)
print('================================')

print('Exemplo 02:')
dc = {
chave: valor for chave, valor in produto.items()
}
print(dc)
print('================================')

print('Exemplo 03:')
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dc)
print('================================')

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)