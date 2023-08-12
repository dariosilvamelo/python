"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase1 = '    Olha só que, coisa interessante    '
lista_palavras = frase1.split() 
print(lista_palavras)
print('============================')

lista_frase = frase1.split(',') 
print(lista_frase)
print('============================')

nova_lista_frase = []

for i, frase in enumerate(lista_frase):
    nova_lista_frase.append(lista_frase[i].strip())
print(nova_lista_frase)
print('============================')

nova_lista_frase = []

for i, frase in enumerate(lista_frase):
    nova_lista_frase.append(lista_frase[i].rstrip())
print(nova_lista_frase)
print('============================')

nova_lista_frase = []

for i, frase in enumerate(lista_frase):
    nova_lista_frase.append(lista_frase[i].lstrip())
print(nova_lista_frase)
print('============================')


frases_unidas = ' * '.join(nova_lista_frase)
print(frases_unidas)
