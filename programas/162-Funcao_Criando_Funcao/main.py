def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def funcao_interna(x,y):
        return funcao(x, y)
    return funcao_interna


soma_com_cinco = criar_funcao(soma)
multiplica_por_dez = criar_funcao(multiplica)

print(soma_com_cinco(5,6))
print(multiplica_por_dez(2,10))

