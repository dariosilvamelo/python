import random
import sys

for j in range(100):
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
    print(nove_digitos)
sys.exit
