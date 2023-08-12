"""
Introdução ao empacotamento e desempacotamento
"""
nome = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nome
print(nome1, nome2, nome3)

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome1, nome2, nome3)


_, _, nome, *resto = ['Maria', 'Helena', 'Luiz', 'Clariano', 'Dário']
print(nome)
print(resto)

# caso não queira o resto posso fazer assim:
resto = 'não quero o resto'
_, _, nome, *_= ['Maria', 'Helena', 'Luiz', 'Clariano', 'Dário']
print(nome)
print(resto)

# caso não queira o resto posso fazer assim:
resto = 'não quero o resto'
primeiro, segundo, *_, penultimo, ultimo= ['Maria', 'Helena', 'Luiz', 'Clariano', 'Dário']
print(primeiro, segundo, penultimo, ultimo)

