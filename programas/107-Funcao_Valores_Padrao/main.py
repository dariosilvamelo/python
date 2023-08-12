def soma(x, y=2, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)  


soma(1, 2, 3)
soma(1, 2)
soma(z=10, x=20, y=30)
soma(1)
