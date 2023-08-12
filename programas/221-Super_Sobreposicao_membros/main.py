# super() e a sobreposição de membros - Python Orientado a Objetos
#Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

print('Exemplo 01:')

class MinhaString(str):
     def upper(self):
         print('CHAMOU UPPER')
                         # é opcional colocar o nome da 
                         # Clase e self no metodo super
         retorno = super(MinhaString, self).upper()
         
         print('DEPOIS DO UPPER')
         return retorno

string = MinhaString('Luiz')
print(string.upper())
print('============================')
print('Exemplo 02:')

class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        #super(C, self).metodo()
        super(B, self).metodo()
        print('C')

#print(C.mro())  #mostra a orfem da classe filha de das super clases      

C1 = C()
print(C1.atributo_a)
print(C1.atributo_b)
print(C1.atributo_c)
C1.metodo()


