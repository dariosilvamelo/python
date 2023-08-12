"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def duplicidade (lista, elemento):
    repeticao = 0
    for i in lista:    
        if i== elemento:
            repeticao +=1    
    if repeticao>=2:
        return elemento
    else:
        return -1                

def ordenar_set(set):
    lista_set = list(set)
    for j in range (len(lista_set)):
        for i in range(len(lista_set)-1):
            if i < len(lista_set)-1:
                posicao1= lista_set[i]
                posicao2= lista_set[i+1]
                if posicao1 > posicao2: 
                    lista_set[i]   = posicao2
                    lista_set[i+1] = posicao1
    return lista_set

def imprimir(lista_origem, lista_numero_duplicado): 
      
    print(lista_origem,end='')
    print(' -> ',end='')
    if len(lista_numero_duplicado)==0:
        print('não tem duplicados')
    else:    
        for i in range(len(lista_numero_duplicado)):
              print(lista_numero_duplicado[i],end='')
              if i ==len(lista_numero_duplicado)-1:
                print(' ', end='')
              elif i ==len(lista_numero_duplicado)-2:
                print(' e ', end='')
              else:  
                print(', ',end='')
        print(' são duplicados')   


for lista in lista_de_listas_de_inteiros:
    itens_com_duplicidade = set()
    for indice in range(len(lista)):
        if duplicidade (lista, lista[indice]) != -1:
           itens_com_duplicidade.add( lista[indice]) 
    imprimir(lista, ordenar_set(itens_com_duplicidade))
    itens_com_duplicidade.clear       

