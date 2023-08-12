# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.exemplo_01    = 'atributo público'
        self._exemplo_02   = 'atrinuto protegido' # classe e suas subcasses
        self.__exemplo_03  = 'atributo privato' # classe

    def metodo_publico(self):
        print(self.__exemplo_03)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        return '_metodo_protected'

    def __metodo_private(self):
        return '__metodo_private'


f = Foo()
print(f.exemplo_01)
print(f._exemplo_02)
# print(f.__exemplo_03) Dá erro só posso acessar dentro da classe.
print('===================')
print(f.metodo_publico())
print(f._metodo_protected())
#print(f.__metodo_private()) Dá erro só pode ser acessado dentro da classe.

