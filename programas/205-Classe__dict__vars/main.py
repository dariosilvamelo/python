# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Serena', 'idade': 3}
p1 = Pessoa('Dário', 35)
print('Exemplo 01:')
print('')
print('__dict__ inicial:')
print(p1.__dict__)
# ou
print(vars(p1))
print('')
print('O __dict__ É EDITAVEL!')
print('')
p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'EITA'
print(p1.__dict__)
print('')
print('===============================')
print('')
print('Exemplo 02:')
print('')
p2 = Pessoa(**dados)
print('__dict__ inicial:')
print(p2.__dict__)
print('')
print('===============================')
