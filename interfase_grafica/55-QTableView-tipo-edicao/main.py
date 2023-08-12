import re
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
                               QPushButton, QTableView, QVBoxLayout)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName('.\\000-dados\\banco.db')
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(600, 400))
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable("notas")

        # removendo colunas
        # coloca o "numero da coluna" e
        # numero de quantos colunas deseja remover a partir dela
        # Exemplo:
        # vai remover duas colunas a partir da coluna 1
        # self.model.removeColumns(1, 2)
        # ou passando o nome
        colunas = ['index', 'ipi']
        for campo in colunas:
            id = self.model.fieldIndex(campo)
            self.model.removeColumns(id, 1)

        # Ordenação:
        self.model.setSort(2, Qt.DescendingOrder)  # ordem decrescente
        # self.model.setSort(2, Qt.AscendingOrder)  # ordem crescente

        self.model.select()

        # o salvemente vai ter que ser manual
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.filtro = QLineEdit()
        self.btn_alterar = QPushButton("alterar valoes")

        layout = QVBoxLayout()
        layout.addWidget(self.filtro)
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_alterar.clicked.connect(self.alterar_dados)
        self.filtro.textChanged.connect(self.filtrar_nota)

    def alterar_dados(self):

        self.model.submitAll()  # salva

    def reverter(self):
        self.model.revertAll()  # volta salvamento

    def filtrar_nota(self, s):
        a = s
        s = re.sub('[\W_]+', '', s)
        filte_nota = f'Notas LIKE "%{s}%"'
        self.model.setFilter(filte_nota)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
