
algarismos       = ['0','1','2','3','4','5','6','7','8','9']
cpf              = []
digito01_entrada = 0
digito02_entrada = 0

cpf_entrada   = input('Digite o n° do CPF: ')

for indice, digito in enumerate(cpf_entrada):
        if cpf_entrada[indice] in algarismos:
           cpf.append(cpf_entrada[indice])

if len(cpf)== 11:
    
    somatorio        = 0
    multiplicador    = 10
    digito01_entrada = int(cpf[9])
    digito02_entrada = int(cpf[10])
    cpf.pop()
    cpf.pop()    

    for indice, digito in enumerate(cpf):
        somatorio += int(cpf[indice]) * multiplicador
        multiplicador -=1
    
    primeiro_digito = (somatorio*10)%11
    print(somatorio)
    print(primeiro_digito)

    if primeiro_digito > 9:
        primeiro_digito = 0

    print(f'O primeiro digito do cpd é {primeiro_digito}')

    cpf.append(primeiro_digito)
    somatorio     = 0
    multiplicador = 11

    for indice, digito in enumerate(cpf):
        somatorio += int(cpf[indice]) * multiplicador
        multiplicador -=1
    
    segundo_digito = (somatorio*10)%11
    print(somatorio)
    print(segundo_digito)

    if segundo_digito > 9:
        segundo_digito = 0

    print(f'O segundo digito do CPF é {segundo_digito}')

    if (digito01_entrada == primeiro_digito) and (digito02_entrada == segundo_digito):
        print(f'O CPF:{cpf_entrada} é valido!')
    else:
        print(f'O CPF:{cpf_entrada} não é valido!')

else:
    print('O cpf tem que ter 11 digitos!')




        