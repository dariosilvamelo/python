
horario = input('Digite a horário (HH) :')
try:
    hora = int(horario[0:2])
    if    0 <= hora <= 11 :
            print('Bom dia!')
    elif 12 <= hora <= 17:
            print('Boa tarde!')
    elif 18 <= hora <= 23:
            print('Boa noite')
    else:
            print('O horário digitado terá que ser entre 00 as 23')
except:
    print('Horário invalido!')
