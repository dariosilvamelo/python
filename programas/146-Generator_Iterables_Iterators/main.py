import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
print(next(iterator))#passa para o proximo
print(next(iterator))#passa para o proximo
print(next(iterator))#se tentar para o proximo na lista não tem mais e gera erro.

lista     = [n for n in range(10000000)]
generator = (n for n in range(10000000))

print(sys.getsizeof(lista))      #espaço que ocupa da memoria
print(sys.getsizeof(generator))  #espaço que ocupa da memoria

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator:
#     print(n)