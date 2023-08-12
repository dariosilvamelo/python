# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):# recebe o paramentro 10
        self.multiplicador = multiplicador

    def __call__(self, funcao): #recebe a funcao soma 
        
        def call_interno(*args, **kwargs):
            return funcao(*args, **kwargs) * self.multiplicador

        return call_interno


@Multiplicar(10)
def soma_e_multiplica_por_10(x, y):
    return x + y


s = soma_e_multiplica_por_10(2, 4)
print(s)