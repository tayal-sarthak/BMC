# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vid5.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 841)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.photo = QLabel(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(170, 130, 621, 301))
        self.photo.setPixmap(QPixmap(u"IMG-4683.jpg"))
        self.photo.setScaledContents(True)
        self.noormal = QPushButton(self.centralwidget)
        self.noormal.setObjectName(u"noormal")
        self.noormal.setGeometry(QRect(220, 610, 251, 151))
        self.nootnormal = QPushButton(self.centralwidget)
        self.nootnormal.setObjectName(u"nootnormal")
        self.nootnormal.setGeometry(QRect(700, 600, 251, 151))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1094, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.photo.setText("")
        self.noormal.setText(QCoreApplication.translate("MainWindow", u"normal", None))
        self.nootnormal.setText(QCoreApplication.translate("MainWindow", u"not normal", None))
    # retranslateUi

