# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum
                      # 1° paramentro é o segundo paramentro 
                      # é uma lista com CONSTANTES
Direcoes = enum.Enum('Direcoes',['ESQUERDA', 'DIREITA','ACIMA','ABAIXO'])
                      #indices ->     0            1


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)