n = input('Digite um número inteiro: ')
numero_par   = True
numero_texto = 'impar'
try:
    numero_par = int(n) % 2 == 0
    
    if numero_par:
        numero_texto = 'par'
    
    print(f'O número {n} é {numero_texto}.')    
except:
    print('O número não é inteiro.')