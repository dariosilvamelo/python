# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
print('Exemplo 01:')#mostra qual dado da lista é do tipo "set"
for item in lista:
    print(item,isinstance(item, set))
print('=====================')

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print(item.upper())

    elif isinstance(item, (int, float)):
        print(item, item * 2)
    else:
        print(item)