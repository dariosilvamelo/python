# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    # 1° Paramentro: a metaclasse
    # 2° Paramentro: o nome da classe que está sendo criada
    # 3° Paramentro: uma tupla com as heranças da classe  
    # 4° Paramentro: dict da classe { Em nosso exemplo é a classe Pesooa}          
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234 # é possvel criar atributos e metodos.
        cls.__repr__ = meu_repr

        # no caso de um desevolvedor usar seu tipo e não implementar 
        # o metodo "falar", na classe pessoa irá ocorreu uma execão
        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    # é resposavel para tornar a classe executavel.
    # No nosso exemplo o call é perposavel por
    # fazer "Pessoa()" torna-se um secutavel. 
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia


class Pessoa(metaclass=Meta):

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Luiz')
p1.falar()
print(repr(p1))
print(Pessoa.__dict__)