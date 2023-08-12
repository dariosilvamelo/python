import sys

from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.show()

app.exec()
