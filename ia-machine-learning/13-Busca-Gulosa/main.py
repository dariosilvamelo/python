import numpy as np


class Vertice:

    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice):
        self.vertice = vertice


class Grafo:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.adiciona_adjacente(Adjacente(zerind))
    arad.adiciona_adjacente(Adjacente(sibiu))
    arad.adiciona_adjacente(Adjacente(timisoara))

    zerind.adiciona_adjacente(Adjacente(arad))
    zerind.adiciona_adjacente(Adjacente(oradea))

    oradea.adiciona_adjacente(Adjacente(zerind))
    oradea.adiciona_adjacente(Adjacente(sibiu))

    sibiu.adiciona_adjacente(Adjacente(oradea))
    sibiu.adiciona_adjacente(Adjacente(arad))
    sibiu.adiciona_adjacente(Adjacente(fagaras))
    sibiu.adiciona_adjacente(Adjacente(rimnicu))

    timisoara.adiciona_adjacente(Adjacente(arad))
    timisoara.adiciona_adjacente(Adjacente(lugoj))

    lugoj.adiciona_adjacente(Adjacente(timisoara))
    lugoj.adiciona_adjacente(Adjacente(mehadia))

    mehadia.adiciona_adjacente(Adjacente(lugoj))
    mehadia.adiciona_adjacente(Adjacente(dobreta))

    dobreta.adiciona_adjacente(Adjacente(mehadia))
    dobreta.adiciona_adjacente(Adjacente(craiova))

    craiova.adiciona_adjacente(Adjacente(dobreta))
    craiova.adiciona_adjacente(Adjacente(pitesti))
    craiova.adiciona_adjacente(Adjacente(rimnicu))

    rimnicu.adiciona_adjacente(Adjacente(craiova))
    rimnicu.adiciona_adjacente(Adjacente(sibiu))
    rimnicu.adiciona_adjacente(Adjacente(pitesti))

    fagaras.adiciona_adjacente(Adjacente(sibiu))
    fagaras.adiciona_adjacente(Adjacente(bucharest))

    pitesti.adiciona_adjacente(Adjacente(rimnicu))
    pitesti.adiciona_adjacente(Adjacente(craiova))
    pitesti.adiciona_adjacente(Adjacente(bucharest))

    bucharest.adiciona_adjacente(Adjacente(fagaras))
    bucharest.adiciona_adjacente(Adjacente(pitesti))
    bucharest.adiciona_adjacente(Adjacente(giurgiu))


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo,
                      ' - ', self.valores[i].distancia_objetivo)


class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado == True
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0])


grafo = Grafo()

"""
vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.lugoj)
vetor.imprime()
"""

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
