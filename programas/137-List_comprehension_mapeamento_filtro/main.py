# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'agua',   'preco': 20, 'unidade':'L' },
    {'nome': 'agua',   'preco': 10, 'unidade':'L'  },
    {'nome': 'granola','preco': 30, 'unidade':'g'  },
]

print('Exemplo 01:')
novos_produtos_01 = [
    produto for produto in produtos
]

print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 02:')
novos_produtos_01 = [
    {produto['nome'], produto['preco']} for produto in produtos
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 03:')
novos_produtos_01 = [
    {**produto} for produto in produtos
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 04:')
novos_produtos_01 = [
    {'altera_nome_chave':produto['nome']} for produto in produtos
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 05:')
novos_produtos_01 = [
    {**produto, 'preco':produto['preco']*2} for produto in produtos
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 06:')
novos_produtos_01 = [
    {**produto,'preco': 1000.00} if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 07:')
novos_produtos_01 = [
    {**produto,'preco': 1000.00} if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco']>=30
]
print(novos_produtos_01, sep='\n')
print('================')

print('Exemplo 08:')
novos_produtos_01 = [
    {**produto,'preco': 1000.00} if produto['preco'] == 20 else {**produto}
    for produto in produtos
    if produto['nome'] in ('agua') and produto['preco']>=10
]
print(novos_produtos_01, sep='\n')
print('================')
