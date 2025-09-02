# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QRect, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QComboBox, QLabel, QMainWindow, QMenuBar,
                               QPushButton, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QFont()
        font.setPointSize(20)

        self.comboX = QComboBox(self.centralwidget)
        self.comboX.setGeometry(QRect(60, 80, 221, 161))
        self.comboX.setObjectName("comboX")
        self.comboX.setFont(font)
        self.comboX.addItems(["0", "1"])

        self.comboY = QComboBox(self.centralwidget)
        self.comboY.setGeometry(QRect(440, 80, 221, 161))
        self.comboY.setObjectName("comboY")
        self.comboY.setFont(font)
        self.comboY.addItems(["0", "1"])

        font_button = QFont()
        font_button.setPointSize(22)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(290, 370, 201, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font_button)

        font_label = QFont()
        font_label.setPointSize(21)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(300, 280, 171, 71))
        self.label.setObjectName("label")
        self.label.setFont(font_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Submit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "X XORY Y:", None))