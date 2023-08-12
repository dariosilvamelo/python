from dataclasses import dataclass

# o modulo dataclasse nos ajuda a apreviar a estrutura da casse e
# __init__(), __repr__(), __eq__() (entre outros)
# inicializa  imprime     verifica se dois objetos são iguais
#             atributos
#             e seu valor


@dataclass
class Pessoa:
    nome: str
    idade: int

    def __post__init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Dário', 45)
    p2 = Pessoa('Serena', 3)
    print(p1 == p2)

    p1.nome_completo = 'Dário Silva Melo'
    print(p1)
    print(p1.nome_completo)

    p2.nome_completo = 'Dário Silva Melo'
    print(p2)
    print(p2.nome_completo)
