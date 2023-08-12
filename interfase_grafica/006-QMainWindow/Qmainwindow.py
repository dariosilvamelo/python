import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu primeiro Programa')
        self.setFixedSize(QSize(600, 400))

        self.button = QPushButton('Desligado')
        self.setCentralWidget(self.button)
        self.button.setStyleSheet(u"background-color:red")

        self.button.setCheckable(True)

        self.button.clicked.connect(self.imprimir)
        self.button.clicked.connect(self.clicado)

    def imprimir(self):
        print('testendo botão')

    def clicado(self, s):
        print('clicado:', s)
        if s:
            self.button.setStyleSheet(u"background-color:green")
            self.button.setText("Ligado")
        else:
            self.button.setStyleSheet(u"background-color:red")
            self.button.setText("Desligado")


app = QApplication(sys.argv)

janela_principal = MainWindow()
janela_principal.show()

app.exec()
