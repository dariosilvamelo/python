# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

print('Exemplo 01:')
p1 = Pessoa('João', 34)
p2 = Pessoa('Anônima', 23)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print('===============================')
print('')
print('Exemplo 02:')
p3 = Pessoa.criar_com_50_anos('João') 
# criar um objeto por um metodo é porque você quer colocar umar regra 
# (para criar o objeto pessoa tem que sempre seguir uma determinada logica),
# no exemplo você quer criar pessoa sempro com idade de 50 anos
# e no outro exemplo criar sempre a pessoa com nome "Anônimo"
p4 = Pessoa.criar_sem_nome(25)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()