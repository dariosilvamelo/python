import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QStatusBar,
                               QToolBar)

# site para buscar icones: https://p.yusukekamiyamane.com/


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QToolBar")
        self.lbl = QLabel("QToolBAR")
        self.lbl.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.lbl)

        toolbar = QToolBar("Minha toolbar")
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)

        btn_action = QAction(
            QIcon('.\\27-Toolbar\\Icone.png'), "meu botão", self)
        btn_action.setStatusTip("Este é o seu botão")
        btn_action.triggered.connect(self.funcao)
        btn_action.setCheckable(True)
        toolbar.addAction(btn_action)

        toolbar.addSeparator()

        btn_action2 = QAction(
            QIcon('.\\27-Toolbar\\Icone.png'), "segundo botão", self)
        btn_action2.setStatusTip("Este éo segundo botão")
        btn_action2.triggered.connect(self.funcao)
        btn_action2.setCheckable(True)
        toolbar.addAction(btn_action2)

        # Qt.ToolButtonIconOnly - sem texto somente icone
        # Qt.ToolButtonTextOnly - somente texto sem icone
        # Qt.ToolButtonTextBesideIcon icone com o texto acima
        # Qt.ToolButtonTextUnderIcon icone e texto, com texto abaixo
        # Qt.ToolButtonFollowStyle  segue o padrão do descktop

        toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.setStatusBar(QStatusBar(self))

    def funcao(self, s):
        print("click", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
