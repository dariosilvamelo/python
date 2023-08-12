# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import icons_rc
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(229, 363)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 10, 181, 341))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_usuario = QLabel(self.frame_3)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.lbl_usuario.setPixmap(QPixmap(u":/icone/_imgs/_imgs/user.png"))
        self.lbl_usuario.setScaledContents(True)
        self.lbl_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_usuario)

        self.lne_usuario = QLineEdit(self.frame_3)
        self.lne_usuario.setObjectName(u"lne_usuario")
        self.lne_usuario.setStyleSheet(u"")
        self.lne_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lne_usuario)

        self.lbl_senha = QLabel(self.frame_3)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.lbl_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_senha)

        self.lne_senha = QLineEdit(self.frame_3)
        self.lne_senha.setObjectName(u"lne_senha")
        self.lne_senha.setLayoutDirection(Qt.LeftToRight)
        self.lne_senha.setStyleSheet(u"")
        self.lne_senha.setEchoMode(QLineEdit.Password)
        self.lne_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lne_senha)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 29))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
                                      "border-radius: 10px\n"
                                      "")

        self.verticalLayout_3.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.lbl_usuario.setText("")
        self.lne_usuario.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Inserir seu usu\u00e1rio", None))
        self.lbl_senha.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icone/_imgs/_imgs/password.png\"/></p></body></html>", None))
        self.lne_senha.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Inserir sua senha", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec()
