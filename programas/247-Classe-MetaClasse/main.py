# class Foo: # Classe Food
# ou (é mesma coisa)
Foo = type('Foo', (object,), {})

# type é quem cria a classe
# 1° paramentro é uma String que será o nome da classe
# 2° paramentro uma tupla com as heranças
# 3° paramentro é passado uma " dict "

# type é uma meta classe em Python

f = Foo()  # f é estancia da classe Food

print('" f " é instancia de Foo ('+str(isinstance(f, Foo))+')')
print(' O tipo de "f" é ' + str(type(f)))
print(' O tipo de "Foo" é ' + str(type(Foo)))
