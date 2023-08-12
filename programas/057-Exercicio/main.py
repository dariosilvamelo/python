
nome = input('Digite Seu primeiro nome :')

n = len(nome)
   
if   1 <= n <= 4 :
     print('Seu nome é curto.')
elif 5 <= n <= 6:
     print('Seu nome é normal.')
elif n > 6 :
     print('Seu nome é muito grande')
else:
     print('O nome não foi digitado')
