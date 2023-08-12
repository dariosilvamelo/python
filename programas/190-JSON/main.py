import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('.\\190-JSON\\aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        # dasebilita o a formatação ascii para
        # visualizar caracteres pesciais e acentos
        ensure_ascii=False,
        indent=2,  # formata o arquivo para facil visualização
    )

with open('.\\190-JSON\\aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

print('')
print(type(pessoa))
print('==============')
for chave in pessoa:
    print(chave, ' : ', pessoa[chave])
