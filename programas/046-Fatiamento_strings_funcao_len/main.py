"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
import re

#         + 012345678

variavel = 'Olá mundo'
#         - 987654321
print(variavel[0:6])
print(variavel[4:6])
print(variavel[4:])  # vai até o final
print(variavel[:4])  # vai do inicio até a posição 4
print(variavel[-7:-3])
print(variavel[0:9:1])  # pula de um em um
print(variavel[0:9:2])  # pula de dois em dois
print(variavel[::-1])  # inverter iniciar com a posição -1 a -9
print(len(variavel))
print(len(variavel[4:6]))
print(variavel[4:len(variavel)])
# remover caracter da string

cpf = '026.872.056-80' \
    .replace('.', '') \
    .replace('-', '')

print(cpf)
cnpj = '1'
cnpj = re.sub(r'[^0-9]', '', '22.023.139/0001-93')
print(cnpj)
