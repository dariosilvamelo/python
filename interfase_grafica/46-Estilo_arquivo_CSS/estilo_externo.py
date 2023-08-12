import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QFormLayout, QLabel, QLCDNumber,
                               QLineEdit, QMainWindow, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow(QCheckBox('Checkbox'))
        formulario.addRow(QRadioButton('Radio Button'))
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QDateEdit", QDateEdit())
        formulario.addRow("QDateTimeEdit", QDateTimeEdit())
        formulario.addRow("QSpinBox", QSpinBox())
        formulario.addRow("QDoubleSpinBox", QDoubleSpinBox())
        formulario.addRow("QComboBox", QComboBox())
        formulario.addRow("QFontComboBox", QFontComboBox())
        formulario.addRow("QProgressBar", QProgressBar())
        formulario.addRow("QLCDNumber", QLCDNumber())
        formulario.addRow("QSlider", QSlider(Qt.Horizontal))
        formulario.addRow("QDial", QDial())

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)
        self.aplicar_estilo()

    def aplicar_estilo(self):
        path = '.\\46-Estilo_arquivo_CSS\\estilo_css.css'
        try:
            with open(path)as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
