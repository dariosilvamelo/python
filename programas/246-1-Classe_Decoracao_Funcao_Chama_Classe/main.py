class Multiplicar:
    def __init__(self, funcao):# recebe a função soma
        self.funcao = funcao # está armazenando a função soma
        self.multiplicador = 10 

    def __call__(self, *args, **kwargs): 
        # args armazena os valores dos paramentos x e y ( x=2 e y=4 )
        print(*args, **kwargs)
        return self.funcao(*args, **kwargs) * self.multiplicador


@Multiplicar
def soma_e_multiplica_por_10(x, y):
    return x + y


s = soma_e_multiplica_por_10(2, 4)
print(s)