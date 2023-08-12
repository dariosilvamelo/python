palavra_secreta = 'perfume'
palavra         = len(palavra_secreta)*'*'
tentativas      = 0
while palavra != 'perfume':
    letra = input('Digite uma letra: ')
    tentativas +=1
    if len(letra) == 1:
        
        if letra in palavra_secreta:
           
           for i in range(0, len(palavra_secreta),1):
                 
                 if letra==palavra_secreta[i]:
                 
                    parte1  = palavra[:i]
                    parte2  = palavra[i+1:]
                    palavra =  parte1 + letra + parte2
        
        print(f'Palavra formatada: {palavra}')
    else:
        print('Digite apenas uma letra')
else:
    print('VOCÊ GANHOU PARABÉNS')
    print(f'a palabra era: {palavra_secreta}')
    print(f'Tentativas {tentativas}')

