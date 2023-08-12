perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções'  :['1','2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções'  :['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes'  :['4','5','2','1'],
        'Resposta': '5',
    },
]

acertos=0

for i in range (len(perguntas)):
     print('')
     chave = list(perguntas[i].keys())
     valor = list(perguntas[i].values())
     print(chave[0]+': '+valor[0])
     print('')
     
     print(chave[1]+':')
     
     for j in range(len(valor[1])):
        print(f'{j} ) {valor[1][j]}')
     
     try:
       resposta = input('Escolha uma opção: ')
       indice_resposta = int(resposta)
       if valor[2] == valor[1][indice_resposta]:
          print('Acertou!')
          acertos +=1
       else:
            print('Errou!')   
     except ValueError:
            print('Errou')#o numero não é inteiro
     except IndexError:
            print('Errou')#o indice não esta na lista

print('')
print(f'Você acerto {acertos}')
print(f'de {len(perguntas)} perguntas')      
     
     

   

   