from collections import deque
from time import sleep

# fila o primeiro que entra é o primeiro que sai

fila = deque(maxlen=5)
for i in range(20):
    fila.append(i)
    sleep(1)
    print(*fila)
"""
append(x)................: Adicione x ao lado direito do deque. 
appendleft(x)............: Adicione x ao lado esquerdo do deque.
clear()..................: Remova todos os elementos do deque deixando-o com 
comprimento 0. 
copy()...................: Crie uma cópia rasa do deque.
count(x).................: Conte o número de elementos deque igual a x.
extend(iterable).........: Estenda o lado direito do deque anexando elementos
do argumento iterável.
extendleft(iterable).....: Estenda o lado esquerdo do deque anexando elementos
de iterable. Observe que a série de acréscimos à esquerda resulta na inversão
da ordem dos elementos no argumento iterável.
index(x[, start[, stop]]): Retorna a posição de x no deque (no início ou após
o início do índice e antes da parada do índice). Retorna a primeira 
correspondência ou gera ValueError se não for encontrado.
insert(i, x).............: Insira x no deque na posição i. Se a inserção fizer
com que um deque limitado cresça além do maxlen, um IndexError será gerado.
pop()....................: Remova e retorne um elemento do lado direito do 
deque.  Se nenhum elemento estiver presente, gera um IndexError. 
popleft()................: Remova e retorne um elemento do lado esquerdo do 
deque. Se nenhum elemento estiver presente, gera um IndexError
remove(value)............: Remova a primeira ocorrência de valor. Se não for 
encontrado, levanta um ValueError.
reverse()................: Inverta os elementos do deque in-place e então 
retorne None.
rotate(n=1)..............: "Gire o deque n passos para a direita. Se n for 
negativo, gire para a esquerda. Quando o
deque não está vazio, girar um passo para a direita é equivalente a 
d.appendleft(d.pop()), e girar um passo para a esquerda é equivalente a 
d.append(d.popleft())."
maxlen...................: Tamanho máximo de um deque ou None se ilimitado.
"""
