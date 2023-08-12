import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QVBoxLayout)


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exercicio 10:')
        self.setFixedSize(QSize(300, 200))

        self.entrada_dados = QLineEdit()
        self.label_dados = QLabel()
        self.painel_principal = QVBoxLayout()

        self.painel_principal.addWidget(self.entrada_dados)
        self.painel_principal.addWidget(self.label_dados)

        self.conteiner = QFrame()
        self.conteiner.setLayout(self.painel_principal)

        self.setCentralWidget(self.conteiner)

        self.entrada_dados.textChanged.connect(self.label_dados.setText)


app = QApplication(sys.argv)

janela_principal = MainWindow()
janela_principal.show()

app.exec()
