# s1.clear()
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s1 ^ s2
print('S1=',s1)
print('S2=',s2)
print('S3=',s3)
print('S4=',s4)
print('S5=',s5)
print('S6=',s6)
print('S7=',s7)
