import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QMainWindow,
                               QSlider, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider")
        # veem vertical por padrão basta instaciar como: QSlider()
        # self.slider = QSlider(Qt.Vertical, self)
        self.slider = QSlider(Qt.Horizontal, self)

        # self.slider.setMaximum(5)
        # self.slider.setMinimum(-5)
        # ou
        self.slider.setRange(-10, 20)

        self.setCentralWidget(self.slider)

        self.slider.valueChanged.connect(self.value_Changed)
        self.slider.sliderMoved.connect(self.slider_Moved)
        self.slider.sliderPressed.connect(self.slider_Pressed)
        self.slider.sliderReleased.connect(self.slider_Released)

    def value_Changed(self, i):
        print(i)

    def slider_Moved(self, p):
        print('Posição :', p)

    def slider_Pressed(self):
        print('Presionado')

    def slider_Released(self):
        print('Liberado o botão')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
