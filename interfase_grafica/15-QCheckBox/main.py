
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
                               QMainWindow, QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 15")
        self.setFixedSize(QSize(600, 400))

        self.lbl1 = QLabel("Você fuma?")
        self.ckb = QCheckBox('Marque Esta opção')
        self.ckb.setCheckState(Qt.CheckState(False))  # True para vir marcado
        self.lbl2 = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        layout.addWidget(self.ckb)
        layout.addWidget(self.lbl2)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.ckb.stateChanged.connect(self.estatus)

    def estatus(self, s):
        if s:
            self.lbl2.setText('Preencha o Formulario Abaixo!')
        else:
            self.lbl2.setText('')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
