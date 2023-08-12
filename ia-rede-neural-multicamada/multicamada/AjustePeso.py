import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# saidas = np.array([0, 0, 0, 1])

saidas = np.array([0, 1, 1, 1])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1


def stepFuncioton(soma):
    if (soma >= 1):
        return 1
    return 0


def soma(entradas, peso):
    return entradas.dot(peso)


def treinar(entradas, saidas, taxaAprendizagem, pesos):
    erroTotal = 1

    while (erroTotal != 0):

        erroTotal = 0
        for i in range(len(saidas)):

            saidaCalculada = stepFuncioton(soma(np.asarray(entradas[i]), pesos))
            erro = abs(saidas[i]-saidaCalculada)

            erroTotal += erro

            for j in range(len(pesos)):
                print('Peso : '+str(pesos[j]))

                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j]*erro)

            print(str(entradas[i])+'saida=' +
                  str(saidaCalculada)+' erro='+str(erro))
            print()

        print('Total de erros: '+str(erroTotal))
        print()
        print('========================')


def saidaTreinada(e, p):
    return stepFuncioton(soma(np.asarray(e), p))


treinar(entradas, saidas, taxaAprendizagem, pesos)
print()
print('Rede Treinada')
print()

print()
print(saidaTreinada(entradas[3], pesos))
