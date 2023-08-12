import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

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
        self.model.select()

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
