import os
menu  = ''
lista = []
while menu !='S':
    print('Selecione uma Opção: ')

    menu = input('[I]nseir [A]pagar [L]istar [S]air: ')
    if   menu == 'I':
         
         lista.append(input('Valor: '))

         os.system('cls')
    
    elif menu == 'A':
       
       try:  
         n=int(input('Escolha o indice para apagar: '))
         if len(lista)>0:
            if 0<=n<=len(lista):
                del lista[n]
            else:
              print('Indice Incorreto.')      
         else:
            print('Nada para apagar. Lista Vazia!')
       except:
        print('Indice Incorreto.')

    elif menu == 'L':
       
        if len(lista)>0:
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:    
             print('Nada para Listar')
else:
    print('Finalizado Sistema.')    