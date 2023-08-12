import sys

from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QMessageBox, QPushButton)
from ui_mai import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Login")

        self.pushButton.clicked.connect(self.login)

    def login(self):

        if self.lne_usuario.text().upper() == 'ADMIN':
            self.msg('OK', 'Usuário valido')
        else:
            self.msg('ERRO', 'Usuário não cadastrado')

        if self.lne_senha.text() == '123':
            self.msg('OK', 'Usuário logado com sucesso!')

    def msg(self, tipo, texto):
        msg = QMessageBox()
        if tipo == 'OK':
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Critical)
        msg.setText(texto)
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
