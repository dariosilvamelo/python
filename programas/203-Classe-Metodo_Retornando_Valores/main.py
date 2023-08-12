# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return 
            # é usado pra já retornar o metodo e não executar o 
            # o que está embaixo
            # seria como se fosse um break dentro de lanço

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()