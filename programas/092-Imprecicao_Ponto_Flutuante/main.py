"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
print('Opção:1')
numero_1 = 0.1
numero_2 = 0.7
print(numero_1)
print(numero_2)
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print('===================')
print('Opção:2')
numero_1 = 0.1
numero_2 = 0.7
print(numero_1)
print(numero_2)
numero_3 = numero_1 + numero_2
print(numero_3)
print(round(numero_3, 3))
print('===================')
print('Opção:3')
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
print(numero_1)
print(numero_2)
numero_3 = numero_1 + numero_2
print(numero_3)
print('===================')
print('Opção:4')
numero_1 = decimal.Decimal(0.1) # utilizar quando deseja vazer calculos precisos com as ultimas casas do ponto flutuante
numero_2 = decimal.Decimal(0.7) 
print(numero_1)
print(numero_2)
numero_3 = numero_1 + numero_2
print(numero_3)