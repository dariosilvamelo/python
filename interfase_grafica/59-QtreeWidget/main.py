import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QTreeWidget, QTreeWidgetItem)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeWidget")

        self.tw = QTreeWidget()

        self.tw.setHeaderLabels(['Nome', 'valor'])  # Titulo das colunas

        self.tw.setAlternatingRowColors(True)  # alternancia de cor na linha

        # adicionado o item na tabela
        doce = QTreeWidgetItem(self.tw, ["Doce", '2,00'])

        # a variavel "doce" serve caso queira fazer checkbox e subniveis
        doce.setCheckState(0, Qt.CheckState.Unchecked)  # checkbox
        QTreeWidgetItem(doce, ['brigadeiro', '1,00'])  # subniveis
        QTreeWidgetItem(doce, ['beijinho', '1,00'])

        QTreeWidgetItem(self.tw, ['verdura', '5,00'])
        self.setCentralWidget(self.tw)

        bebida = QTreeWidgetItem(self.tw, ['bebida', '10,00'])
        bebida.setDisabled(True)
        self.setCentralWidget(self.tw)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
