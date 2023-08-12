import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabelas")
        self.setFixedSize(QSize(600, 400))

        layout = QVBoxLayout()

        self.tb = QTableWidget()
        self.tb.setRowCount(3)
        self.tb.setColumnCount(3)

        self.tb.setHorizontalHeaderLabels(['Nome', 'Enderço', 'e-mail'])
        self.tb.setItem(0, 0, QTableWidgetItem('Dário da Silva Melo'))
        self.tb.setItem(0, 1, QTableWidgetItem(
            "Av. Joaquim Flores Silva, 1201"))
        self.tb.setItem(0, 2, QTableWidgetItem("dariosilvamelo@gmail.com"))

        self.tb.setItem(1, 0, QTableWidgetItem("Serena Costa Melo"))
        self.tb.setItem(1, 1, QTableWidgetItem(
            "Rua Matuzalem de Freitas Cardoso, 300"))
        self.tb.setItem(1, 2, QTableWidgetItem("serenacostamelo@gmail.com"))

        self.tb.setItem(2, 0, QTableWidgetItem("Mayra Cabrera Costa"))
        self.tb.setItem(2, 1, QTableWidgetItem(
            "Rua Perimental,200"))
        self.tb.setItem(2, 2, QTableWidgetItem("mayracabreracosta@gmail.com"))
        self.tb.cellChanged.connect(self.result)
        self.tb.itemChanged.connect(self.item_changed)
        self.tb.cellActivated.connect(self.cell_Activated)

        layout.addWidget(self.tb)

        self.setLayout(layout)

    def result(self, linha, coluna):
        print(linha, coluna)

    def item_changed(self, item):
        print(item.text())

    def cell_Activated(self, linha, coluna):
        print('ativado ', linha, coluna)  # Quando preciona enter é ativado


"""
cellActivated(int row, int column)
cellChanged(int row, int column)
cellClicked(int row, int column)
cellDoubleClicked(int row, int column)
cellEntered(int row, int column)
cellPressed(int row, int column)
currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
currentItemChanged(QTableWidgetItem *current, QTableWidgetItem *previous)
itemActivated(QTableWidgetItem *item)
itemChanged(QTableWidgetItem *item)
itemClicked(QTableWidgetItem *item)
itemDoubleClicked(QTableWidgetItem *item)
itemEntered(QTableWidgetItem *item)
itemPressed(QTableWidgetItem *item)
itemSelectionChanged()        
"""
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
