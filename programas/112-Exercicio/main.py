def multiplica(*args):
    x=1
    for n in args:
       x=x*n
    return x 

def par_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'impar'        

i = 2,3,5,6
j = 10
print(multiplica(*i))
print(f'O numero {j} é {par_impar(j)}')