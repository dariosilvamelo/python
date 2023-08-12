'''
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite ouro valor: ')
if primeiro_valor < segundo_valor:
    linha = f"o sengulo valor ='{segundo_valor}' é maior que o primeiro valor = '{primeiro_valor}'"
else:
    linha = f"o primeiro valor ='{primeiro_valor}' é maior que o segundo valor = '{segundo_valor}'"

print(linha)

ou 

'''

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    linha = f'{primeiro_valor=} é maior ou igual 'f'ao que {segundo_valor=}'
else:
    linha = f'{segundo_valor=} é maior 'f'do que {primeiro_valor=}'

print(linha)   
