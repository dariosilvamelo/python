
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Dário', 45, 'Silva Melo')
    p2 = Pessoa('Serena', 3, 'Costa Melo')
    print(p1 == p2)

    p1.nome_completo = 'Dário Silva Melo'
    print(p1)
    print(p1.nome_completo)

    p2.nome_completo = 'Dário Silva Melo'
    print(p2)
    print(p2.nome_completo)
