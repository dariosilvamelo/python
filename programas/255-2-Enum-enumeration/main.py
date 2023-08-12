# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA  = enum.auto()
    ACIMA    = enum.auto()
    ABAIXO   = enum.auto()


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
print('===========================')

print(Direcoes(1))
print(Direcoes(1).name)
print(Direcoes.ESQUERDA)
print(Direcoes.ESQUERDA.value)
print(Direcoes['ESQUERDA'])