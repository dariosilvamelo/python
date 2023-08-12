# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Dário', 'Mayra', 'Serena')

    print(lista.__len__())
    print(lista.__getitem__(2))
    print(lista.__setitem__(2, 'Mayra'))
    print(lista.__getitem__(2))
    print(lista.__setitem__(2, 'Lusmar'))
    print(lista.__iter__())
    print(lista.__next__())
    print(lista.__next__())
    print(lista.__next__())
    print(str(lista._next_index))
    for lista in lista._data, lista._index, lista._next_index:
        print(lista)
