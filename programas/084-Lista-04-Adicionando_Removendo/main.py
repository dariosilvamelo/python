
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print('Lista B')
print(lista_b)
print('============')
lista_b = lista_a.copy()
lista_a[0] = 'Ola Mundo'
print('Lista A')
print(lista_a)
print('============')
print('Lista B')
print(lista_b)