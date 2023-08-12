nome   = 'Luiz Otávio'
altura = 1.80
peso   = 95
imc    = peso / altura ** 2

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

#format
linha_4 = '{nome} tem {altura:.2f} de altura,'
linha_5 = 'pesa {peso} quilos e seu imc é'
linha_6 = '{imc:.2f}'

linha_4 = linha_4.format(nome=nome, altura=altura)
linha_5 = linha_5.format(peso=peso)
linha_6 = linha_6.format(imc=imc)

#interpolação
linha_7 = '%s tem %.2f de altura,' % (nome,altura)
linha_8 = 'pesa %.0f quilos e seu imc é' % (peso)
linha_9 = '%.2f' % (imc)

#f-strings
print('metodo: F-String')
print(' ')
print(linha_1)
print(linha_2)
print(linha_3)
print(' ')
print('=================')
print(' ')
print('metodo: Format')
print(' ')
print(linha_4)
print(linha_5)
print(linha_6)
print(' ')
print('=================')
print(' ')
print('metodo: Interpolação')
print(' ')
print(linha_7)
print(linha_8)
print(linha_9)
print(' ')
print ( 'O hexadecimal de %d é %08X  ' % ( 1500,1500 ) )


