import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QFormLayout, QLabel, QLCDNumber,
                               QLineEdit, QMainWindow, QPlainTextEdit,
                               QProgressBar, QPushButton, QRadioButton,
                               QSlider, QSpinBox, QVBoxLayout, QWidget)


class EditorCSS(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.resize(500, 400)
        self.setWindowTitle("Editor CSS")
        self.css = ' QMainWindow{background-color: rgb(51,51,51)}' \
            + '    QCheckBox{'+'color: white}' \
            + '    QRadioButton{'+'color: white}' \
            + '    QLabel{'+'color: white}' \
            + '    QPushButton{' \
            + '      background-color: orange;' \
            + '      font-size: 14px;' \
            + '      font-weight: bold;' \
            + '    }'
        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.aplicar_estilos)
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.editor.setPlainText(self.css)
        self.show()

    def aplicar_estilos(self):
        self.css = self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(self.css)
        except:
            pass


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

        container = QWidget()
        container.setLayout(formulario)

        self.setCentralWidget(container)

        self.editoCss = EditorCSS(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
