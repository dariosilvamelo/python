import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Icones")
        self.setFixedSize(QSize(600, 400))

        icon = QIcon('.\\44-Icone_Externo\\icone.png')

        button = QPushButton(icon, "Telefone")
        button.setIconSize(QSize(200, 200))
        self.setCentralWidget(button)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
