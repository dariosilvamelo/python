import numpy as np

entradas = np.array([1,7,5])
pesos    = np.array([0.8, 0.1, 0])

def soma(e,p):
    return e.dot(p)

s = soma(entradas, pesos)

def stepFuncioton(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFuncioton(s)

print(r)
