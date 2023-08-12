
# Métodos úteis:
# add, update, clear, discard
s1 = set()
s2 = set()
s1.add('Luiz')
s1.add(1)
print(s1)
s2.update('Olá mundo')
print(s2)
s1.clear()
print(s1)
s1.update(('Luiz','Olá mundo', 1, 2, 3, 4))
print(s1)
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)

# Operadores úteis:
# união | união (union) - Une