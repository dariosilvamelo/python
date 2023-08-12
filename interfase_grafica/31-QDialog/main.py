import sys

from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QLabel,
                               QLineEdit, QMainWindow, QPushButton,
                               QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog ")
        btn = QPushButton("Click para abrir um Dialog!")
        btn.clicked.connect(self.button_clicked)

        self.setCentralWidget(btn)

    def button_clicked(self, s):
        print("click", s)
        dlg = Meu_dialog()
        if dlg.exec_():
            print("sucesso")
            print(dlg.texto)
        else:
            print("cancelar!")


class Meu_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu Dialog")
        self.texto = ""

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.btn_box = QDialogButtonBox(buttons)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)
        self.btn_box.button(QDialogButtonBox.Ok).setText('S I M')
        self.btn_box.button(QDialogButtonBox.Cancel).setText('C A N C E L A R')
        self.btn_box.addButton('Executar', QDialogButtonBox.ActionRole)

        self.txt_nome = QLineEdit()

        self.btn_box.clicked.connect(self.executar)

        self.layout = QVBoxLayout()
        msg = QLabel("Você deseja continuar")
        self.layout.addWidget(self.txt_nome)
        self.layout.addWidget(msg)
        self.layout.addWidget(self.btn_box)
        self.setLayout(self.layout)

    def executar(self):
        print('Executando...')

    def accept(self) -> None:
        self.texto = self.txt_nome.text()
        return super().accept()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
