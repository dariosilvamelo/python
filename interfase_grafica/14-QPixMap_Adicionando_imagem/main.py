
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Imagem")

        self.lbl = QLabel()
        self.lbl.setPixmap(
            QPixmap('.\\14-QPixMap_Adicionando_imagem\\imagem.jpg'))
        # True a imagem é redimencionado junto com a tela.
        self.lbl.setScaledContents(False)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
