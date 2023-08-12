import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
                               QTreeWidget, QTreeWidgetItem, QVBoxLayout)

lista = [
    ['001', 'R$200,00', 'R$ 36,00', 'R$ 10,00'],
    ['001', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
    ['001', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
    ['002', 'R$200,00', 'R$ 36,00', 'R$ 10,00'],
    ['002', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
    ['002', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
    ['003', 'R$200,00', 'R$ 36,00', 'R$ 10,00'],
    ['003', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
    ['003', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeWidget")

        self.botao = QPushButton('Imprimir Campo')

        self.tw = QTreeWidget()
        self.tw.setHeaderLabels(['CODIGO', 'VALOR', 'ICMS', 'IPI'])

        aux = ''

        for item in lista:
            if not item[0] == aux:
                pai = QTreeWidgetItem(self.tw, item)
                pai.setCheckState(0, Qt.CheckState.Checked)
            else:
                filho = QTreeWidgetItem(pai, item)
            aux = item[0]

        self.painel_principal = QVBoxLayout()

        self.painel_principal.addWidget(self.botao)
        self.painel_principal.addWidget(self.tw)

        self.conteiner = QFrame()
        self.conteiner.setLayout(self.painel_principal)

        self.setCentralWidget(self.conteiner)

        self.botao.clicked.connect(self.imprimir)

    def imprimir(self, s):
        ...


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
