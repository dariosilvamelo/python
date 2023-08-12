"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
i=0
for nome in lista:
    print(str(i)+' = ',nome, type(nome))
    i+=1
    #ou
print('====================')
indices = range(len(lista))
for n in indices:
    print(str(n)+' = ',lista[n], type(lista[n]))