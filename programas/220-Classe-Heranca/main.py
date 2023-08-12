# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = 'Classe Pessoa = CPF'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa = '+self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        #sobrepondo a classe pai PESSOA
        print('Classe Cliente = '+self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    #o atributo cpf esta sobrepondo o atributo cpf da classe pai
    cpf = 'Classe Aluno = CPF'
    ...


c1 = Cliente('Luiz', 'Otávio')
a1 = Aluno('Maria', 'Helena')

c1.falar_nome_classe()
a1.falar_nome_classe()
print('c1 = '+ c1.cpf)
print('a1 = '+ a1.cpf)
# help(Cliente)