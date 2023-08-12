# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
class Utilitarios:
    @staticmethod
    def Soma(lista):
        somatorio=0
        for i in lista:
            somatorio +=(i)
        return somatorio    

print(Utilitarios.Soma([100,200,300,400]))
