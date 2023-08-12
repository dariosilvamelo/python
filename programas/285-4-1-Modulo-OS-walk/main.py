import os
from itertools import count

# caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
PASTA_ORIGINAL = 'D:\\Informatica\\Python\\programas'

counter = count()


# imprimit os diretorios, sub diretorios e arquivos do caminha
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for file in files:
        the_counter = next(counter)
        print(the_counter, root, file)
'''
# imprimit os diretorios, sub diretorios
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir in dirs:
        the_counter = next(counter)
        print(the_counter, root, dir)
'''
