import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QFormLayout, QLabel, QLCDNumber,
                               QLineEdit, QMainWindow, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox,
                               QWidget)
from qt_material import apply_stylesheet


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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")
    apply_stylesheet(app, theme='dark_yellow.xml')
"""
['dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml']

"""

window = MainWindow()

window.show()

sys.exit(app.exec())
