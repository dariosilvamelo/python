
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Programa Principal")
        self.setFixedSize(QSize(600, 400))

        self.lbl = QLabel("Meu Label")

        fonte = self.lbl.font()
        fonte.setPointSize(35)
        self.lbl.setFont(fonte)

        self.lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                              Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
