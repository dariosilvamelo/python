lista = [x for x in range(3)]
print(lista)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)