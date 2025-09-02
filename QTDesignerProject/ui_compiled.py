# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pythonGUI.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

from pyqtgraph import ImageView, PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1911, 892)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabCameras = QTabWidget(self.centralwidget)
        self.tabCameras.setObjectName(u"tabCameras")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabCameras.sizePolicy().hasHeightForWidth())
        self.tabCameras.setSizePolicy(sizePolicy)
        self.CMOS = QWidget()
        self.CMOS.setObjectName(u"CMOS")
        self.gridLayout_3 = QGridLayout(self.CMOS)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_8 = QFrame(self.CMOS)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cmosFrame = QFrame(self.frame_8)
        self.cmosFrame.setObjectName(u"cmosFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cmosFrame.sizePolicy().hasHeightForWidth())
        self.cmosFrame.setSizePolicy(sizePolicy2)
        self.cmosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cmosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.cmosFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.panCMOS = QVBoxLayout()
        self.panCMOS.setSpacing(0)
        self.panCMOS.setObjectName(u"panCMOS")

        self.horizontalLayout_3.addLayout(self.panCMOS)


        self.gridLayout_2.addWidget(self.cmosFrame, 1, 1, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_23)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_29.addWidget(self.label_25)

        self.spinCMOSMinClip = QSpinBox(self.frame_8)
        self.spinCMOSMinClip.setObjectName(u"spinCMOSMinClip")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinCMOSMinClip.sizePolicy().hasHeightForWidth())
        self.spinCMOSMinClip.setSizePolicy(sizePolicy3)
        self.spinCMOSMinClip.setMaximum(65535)
        self.spinCMOSMinClip.setSingleStep(100)

        self.horizontalLayout_29.addWidget(self.spinCMOSMinClip)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_29.addWidget(self.label_24)

        self.spinCMOSMaxClip = QSpinBox(self.frame_8)
        self.spinCMOSMaxClip.setObjectName(u"spinCMOSMaxClip")
        sizePolicy3.setHeightForWidth(self.spinCMOSMaxClip.sizePolicy().hasHeightForWidth())
        self.spinCMOSMaxClip.setSizePolicy(sizePolicy3)
        self.spinCMOSMaxClip.setMaximum(65535)
        self.spinCMOSMaxClip.setSingleStep(100)
        self.spinCMOSMaxClip.setValue(65535)

        self.horizontalLayout_29.addWidget(self.spinCMOSMaxClip)

        self.txtGraphCoorninates = QLabel(self.frame_8)
        self.txtGraphCoorninates.setObjectName(u"txtGraphCoorninates")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txtGraphCoorninates.sizePolicy().hasHeightForWidth())
        self.txtGraphCoorninates.setSizePolicy(sizePolicy4)

        self.horizontalLayout_29.addWidget(self.txtGraphCoorninates)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer)

        self.btnCMOSAutoScale = QPushButton(self.frame_8)
        self.btnCMOSAutoScale.setObjectName(u"btnCMOSAutoScale")

        self.horizontalLayout_29.addWidget(self.btnCMOSAutoScale)


        self.gridLayout_2.addLayout(self.horizontalLayout_29, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_8, 0, 1, 2, 2)

        self.frame_6 = QFrame(self.CMOS)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btnStartPauseCMOS = QPushButton(self.frame_6)
        self.btnStartPauseCMOS.setObjectName(u"btnStartPauseCMOS")

        self.verticalLayout_12.addWidget(self.btnStartPauseCMOS)

        self.btnSaveCMOS = QPushButton(self.frame_6)
        self.btnSaveCMOS.setObjectName(u"btnSaveCMOS")

        self.verticalLayout_12.addWidget(self.btnSaveCMOS)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.spinCMOSExposure = QDoubleSpinBox(self.frame_6)
        self.spinCMOSExposure.setObjectName(u"spinCMOSExposure")
        self.spinCMOSExposure.setDecimals(4)
        self.spinCMOSExposure.setMaximum(5.000000000000000)
        self.spinCMOSExposure.setSingleStep(0.010000000000000)
        self.spinCMOSExposure.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinCMOSExposure.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self.spinCMOSExposure)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.btnSetCMOSCameraParameters = QPushButton(self.frame_6)
        self.btnSetCMOSCameraParameters.setObjectName(u"btnSetCMOSCameraParameters")

        self.verticalLayout_8.addWidget(self.btnSetCMOSCameraParameters)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnShowAdminSettings = QPushButton(self.frame_6)
        self.btnShowAdminSettings.setObjectName(u"btnShowAdminSettings")
        self.btnShowAdminSettings.setCheckable(True)

        self.verticalLayout.addWidget(self.btnShowAdminSettings)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy5)
        self.frame_18.setFrameShape(QFrame.Shape.Box)
        self.frame_18.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_39 = QLabel(self.frame_18)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_39)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_82 = QLabel(self.frame_18)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_35.addWidget(self.label_82)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_18)

        self.spinLaserX = QDoubleSpinBox(self.frame_18)
        self.spinLaserX.setObjectName(u"spinLaserX")
        self.spinLaserX.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinLaserX.setMaximum(9999.989999999999782)

        self.horizontalLayout_35.addWidget(self.spinLaserX)


        self.verticalLayout_17.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_84 = QLabel(self.frame_18)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_36.addWidget(self.label_84)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_19)

        self.spinLaserY = QDoubleSpinBox(self.frame_18)
        self.spinLaserY.setObjectName(u"spinLaserY")
        self.spinLaserY.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinLaserY.setMaximum(9999.989999999999782)

        self.horizontalLayout_36.addWidget(self.spinLaserY)


        self.verticalLayout_17.addLayout(self.horizontalLayout_36)

        self.label_34 = QLabel(self.frame_18)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_34)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_56 = QLabel(self.frame_18)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_5.addWidget(self.label_56)

        self.lblLenz1 = QLabel(self.frame_18)
        self.lblLenz1.setObjectName(u"lblLenz1")

        self.horizontalLayout_5.addWidget(self.lblLenz1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.spinLenz1 = QDoubleSpinBox(self.frame_18)
        self.spinLenz1.setObjectName(u"spinLenz1")
        self.spinLenz1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinLenz1.setDecimals(6)

        self.horizontalLayout_5.addWidget(self.spinLenz1)


        self.verticalLayout_17.addLayout(self.horizontalLayout_5)

        self.btnSaveSettings = QPushButton(self.frame_18)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btnSaveSettings.sizePolicy().hasHeightForWidth())
        self.btnSaveSettings.setSizePolicy(sizePolicy6)

        self.verticalLayout_17.addWidget(self.btnSaveSettings)


        self.verticalLayout.addWidget(self.frame_18)


        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 2, 1)

        self.tabCameras.addTab(self.CMOS, "")
        self.Brillouin = QWidget()
        self.Brillouin.setObjectName(u"Brillouin")
        self.gridLayout_4 = QGridLayout(self.Brillouin)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AquisitionArea = QHBoxLayout()
        self.AquisitionArea.setObjectName(u"AquisitionArea")
        self.panAqc = QVBoxLayout()
        self.panAqc.setObjectName(u"panAqc")
        self.panAqc.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.acquisitionPlot = PlotWidget(self.Brillouin)
        self.acquisitionPlot.setObjectName(u"acquisitionPlot")

        self.panAqc.addWidget(self.acquisitionPlot)


        self.AquisitionArea.addLayout(self.panAqc)


        self.gridLayout_4.addLayout(self.AquisitionArea, 3, 3, 4, 4)

        self.frame_11 = QFrame(self.Brillouin)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy7)
        self.frame_11.setFrameShape(QFrame.Shape.Box)
        self.frame_11.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_11.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_52 = QLabel(self.frame_11)
        self.label_52.setObjectName(u"label_52")
        sizePolicy7.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy7)
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_52)

        self.spinNumHPixels = QSpinBox(self.frame_11)
        self.spinNumHPixels.setObjectName(u"spinNumHPixels")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.spinNumHPixels.sizePolicy().hasHeightForWidth())
        self.spinNumHPixels.setSizePolicy(sizePolicy8)
        self.spinNumHPixels.setReadOnly(True)
        self.spinNumHPixels.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinNumHPixels.setMaximum(450)

        self.horizontalLayout_33.addWidget(self.spinNumHPixels)


        self.verticalLayout_16.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_53 = QLabel(self.frame_11)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_53)

        self.spinNumVPixels = QSpinBox(self.frame_11)
        self.spinNumVPixels.setObjectName(u"spinNumVPixels")
        self.spinNumVPixels.setReadOnly(True)
        self.spinNumVPixels.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinNumVPixels.setMaximum(450)

        self.horizontalLayout_34.addWidget(self.spinNumVPixels)


        self.verticalLayout_16.addLayout(self.horizontalLayout_34)

        self.btnStartPauseBrill = QPushButton(self.frame_11)
        self.btnStartPauseBrill.setObjectName(u"btnStartPauseBrill")

        self.verticalLayout_16.addWidget(self.btnStartPauseBrill)

        self.btnShowFullBrill = QPushButton(self.frame_11)
        self.btnShowFullBrill.setObjectName(u"btnShowFullBrill")

        self.verticalLayout_16.addWidget(self.btnShowFullBrill)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_49 = QLabel(self.frame_11)
        self.label_49.setObjectName(u"label_49")
        sizePolicy7.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy7)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_49)

        self.spinHStart = QSpinBox(self.frame_11)
        self.spinHStart.setObjectName(u"spinHStart")
        sizePolicy8.setHeightForWidth(self.spinHStart.sizePolicy().hasHeightForWidth())
        self.spinHStart.setSizePolicy(sizePolicy8)
        self.spinHStart.setMaximum(450)

        self.horizontalLayout_30.addWidget(self.spinHStart)


        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_50 = QLabel(self.frame_11)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_50)

        self.spinVStart = QSpinBox(self.frame_11)
        self.spinVStart.setObjectName(u"spinVStart")
        self.spinVStart.setMaximum(450)

        self.horizontalLayout_31.addWidget(self.spinVStart)


        self.verticalLayout_15.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_51 = QLabel(self.frame_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_51)

        self.spinBrillExposure = QDoubleSpinBox(self.frame_11)
        self.spinBrillExposure.setObjectName(u"spinBrillExposure")
        self.spinBrillExposure.setDecimals(5)
        self.spinBrillExposure.setMinimum(0.000010000000000)
        self.spinBrillExposure.setMaximum(1.000000000000000)
        self.spinBrillExposure.setValue(1.000000000000000)

        self.horizontalLayout_32.addWidget(self.spinBrillExposure)


        self.verticalLayout_15.addLayout(self.horizontalLayout_32)

        self.btnBrillSetParameters = QPushButton(self.frame_11)
        self.btnBrillSetParameters.setObjectName(u"btnBrillSetParameters")

        self.verticalLayout_15.addWidget(self.btnBrillSetParameters)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.ullbrilframe = QFrame(self.frame_11)
        self.ullbrilframe.setObjectName(u"ullbrilframe")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.ullbrilframe.sizePolicy().hasHeightForWidth())
        self.ullbrilframe.setSizePolicy(sizePolicy9)
        self.ullbrilframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.ullbrilframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.ullbrilframe)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.panFullBrill = QHBoxLayout()
        self.panFullBrill.setObjectName(u"panFullBrill")

        self.gridLayout_8.addLayout(self.panFullBrill, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.ullbrilframe)

        self.line_4 = QFrame(self.frame_11)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_4)

        self.panCMOSSnapframe = QFrame(self.frame_11)
        self.panCMOSSnapframe.setObjectName(u"panCMOSSnapframe")
        sizePolicy9.setHeightForWidth(self.panCMOSSnapframe.sizePolicy().hasHeightForWidth())
        self.panCMOSSnapframe.setSizePolicy(sizePolicy9)
        self.panCMOSSnapframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.panCMOSSnapframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.panCMOSSnapframe)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.panCMOSSnap = QHBoxLayout()
        self.panCMOSSnap.setObjectName(u"panCMOSSnap")

        self.verticalLayout_9.addLayout(self.panCMOSSnap)


        self.horizontalLayout_8.addWidget(self.panCMOSSnapframe)

        self.line_7 = QFrame(self.frame_11)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Shadow.Plain)
        self.line_7.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.line_8 = QFrame(self.frame_11)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Shadow.Plain)
        self.line_8.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_8)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_47 = QLabel(self.frame_11)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_47)

        self.spinYStep = QDoubleSpinBox(self.frame_11)
        self.spinYStep.setObjectName(u"spinYStep")
        self.spinYStep.setDecimals(2)
        self.spinYStep.setMaximum(99.989999999999995)
        self.spinYStep.setSingleStep(0.250000000000000)
        self.spinYStep.setValue(1.000000000000000)

        self.verticalLayout_23.addWidget(self.spinYStep)


        self.gridLayout_13.addLayout(self.verticalLayout_23, 2, 4, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_41 = QLabel(self.frame_11)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_41)

        self.spinCurrentShift = QDoubleSpinBox(self.frame_11)
        self.spinCurrentShift.setObjectName(u"spinCurrentShift")
        self.spinCurrentShift.setEnabled(True)
        self.spinCurrentShift.setReadOnly(True)
        self.spinCurrentShift.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinCurrentShift.setProperty(u"showGroupSeparator", False)
        self.spinCurrentShift.setDecimals(5)
        self.spinCurrentShift.setMaximum(999.990000000000009)
        self.spinCurrentShift.setValue(100.000000000000000)

        self.verticalLayout_13.addWidget(self.spinCurrentShift)


        self.gridLayout_13.addLayout(self.verticalLayout_13, 1, 1, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_46 = QLabel(self.frame_11)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_46)

        self.spinGHzPerPixel = QDoubleSpinBox(self.frame_11)
        self.spinGHzPerPixel.setObjectName(u"spinGHzPerPixel")
        self.spinGHzPerPixel.setReadOnly(False)
        self.spinGHzPerPixel.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinGHzPerPixel.setDecimals(3)

        self.verticalLayout_22.addWidget(self.spinGHzPerPixel)


        self.gridLayout_13.addLayout(self.verticalLayout_22, 0, 4, 1, 1)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_109 = QLabel(self.frame_11)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_109)

        self.spinXDistance = QSpinBox(self.frame_11)
        self.spinXDistance.setObjectName(u"spinXDistance")
        self.spinXDistance.setMaximum(9999)

        self.verticalLayout_66.addWidget(self.spinXDistance)


        self.gridLayout_13.addLayout(self.verticalLayout_66, 1, 3, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_48)

        self.spinFSR = QDoubleSpinBox(self.frame_11)
        self.spinFSR.setObjectName(u"spinFSR")
        self.spinFSR.setReadOnly(False)
        self.spinFSR.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinFSR.setDecimals(3)

        self.verticalLayout_24.addWidget(self.spinFSR)


        self.gridLayout_13.addLayout(self.verticalLayout_24, 0, 5, 1, 1)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_108 = QLabel(self.frame_11)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_65.addWidget(self.label_108)

        self.spinYDistance = QSpinBox(self.frame_11)
        self.spinYDistance.setObjectName(u"spinYDistance")
        self.spinYDistance.setMaximum(9999)

        self.verticalLayout_65.addWidget(self.spinYDistance)


        self.gridLayout_13.addLayout(self.verticalLayout_65, 1, 4, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_44 = QLabel(self.frame_11)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_44)

        self.spinCalNum = QDoubleSpinBox(self.frame_11)
        self.spinCalNum.setObjectName(u"spinCalNum")
        self.spinCalNum.setReadOnly(True)
        self.spinCalNum.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinCalNum.setDecimals(0)
        self.spinCalNum.setMaximum(9999.000000000000000)

        self.verticalLayout_20.addWidget(self.spinCalNum)


        self.gridLayout_13.addLayout(self.verticalLayout_20, 0, 3, 1, 1)

        self.btnAbortAquisition = QPushButton(self.frame_11)
        self.btnAbortAquisition.setObjectName(u"btnAbortAquisition")
        sizePolicy.setHeightForWidth(self.btnAbortAquisition.sizePolicy().hasHeightForWidth())
        self.btnAbortAquisition.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.btnAbortAquisition.setFont(font)
        self.btnAbortAquisition.setAutoFillBackground(False)
        self.btnAbortAquisition.setFlat(False)

        self.gridLayout_13.addWidget(self.btnAbortAquisition, 2, 0, 1, 2)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_67 = QLabel(self.frame_11)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_67)

        self.spinZStep = QDoubleSpinBox(self.frame_11)
        self.spinZStep.setObjectName(u"spinZStep")
        self.spinZStep.setDecimals(2)
        self.spinZStep.setMaximum(99.989999999999995)
        self.spinZStep.setSingleStep(0.250000000000000)
        self.spinZStep.setValue(1.000000000000000)

        self.verticalLayout_32.addWidget(self.spinZStep)


        self.gridLayout_13.addLayout(self.verticalLayout_32, 2, 5, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_45 = QLabel(self.frame_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_45)

        self.spinXStep = QDoubleSpinBox(self.frame_11)
        self.spinXStep.setObjectName(u"spinXStep")
        self.spinXStep.setDecimals(2)
        self.spinXStep.setMaximum(99.989999999999995)
        self.spinXStep.setSingleStep(0.250000000000000)
        self.spinXStep.setValue(1.000000000000000)

        self.verticalLayout_21.addWidget(self.spinXStep)


        self.gridLayout_13.addLayout(self.verticalLayout_21, 2, 3, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_42 = QLabel(self.frame_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_42)

        self.spinSTDLastLine = QDoubleSpinBox(self.frame_11)
        self.spinSTDLastLine.setObjectName(u"spinSTDLastLine")
        self.spinSTDLastLine.setReadOnly(True)
        self.spinSTDLastLine.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinSTDLastLine.setDecimals(5)
        self.spinSTDLastLine.setMaximum(999.990000000000009)
        self.spinSTDLastLine.setValue(100.000000000000000)

        self.verticalLayout_19.addWidget(self.spinSTDLastLine)


        self.gridLayout_13.addLayout(self.verticalLayout_19, 0, 1, 1, 1)

        self.line = QFrame(self.frame_11)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.gridLayout_13.addWidget(self.line, 0, 2, 3, 1)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_107 = QLabel(self.frame_11)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_107)

        self.spinZDistance = QSpinBox(self.frame_11)
        self.spinZDistance.setObjectName(u"spinZDistance")
        self.spinZDistance.setMaximum(9999)

        self.verticalLayout_64.addWidget(self.spinZDistance)


        self.gridLayout_13.addLayout(self.verticalLayout_64, 1, 5, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.comboScanPlane = QComboBox(self.frame_11)
        self.comboScanPlane.addItem("")
        self.comboScanPlane.addItem("")
        self.comboScanPlane.addItem("")
        self.comboScanPlane.setObjectName(u"comboScanPlane")
        sizePolicy.setHeightForWidth(self.comboScanPlane.sizePolicy().hasHeightForWidth())
        self.comboScanPlane.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(False)
        self.comboScanPlane.setFont(font1)

        self.verticalLayout_7.addWidget(self.comboScanPlane)


        self.gridLayout_13.addLayout(self.verticalLayout_7, 0, 0, 2, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_13)

        self.frame_25 = QFrame(self.frame_11)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.Box)
        self.frame_25.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_25.setLineWidth(1)
        self.verticalLayout_11 = QVBoxLayout(self.frame_25)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.label_43 = QLabel(self.frame_25)
        self.label_43.setObjectName(u"label_43")
        sizePolicy7.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy7)
        font2 = QFont()
        font2.setPointSize(9)
        self.label_43.setFont(font2)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_43)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_116 = QLabel(self.frame_25)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_116.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_116)

        self.lblWaterCalibrated = QLabel(self.frame_25)
        self.lblWaterCalibrated.setObjectName(u"lblWaterCalibrated")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.lblWaterCalibrated.sizePolicy().hasHeightForWidth())
        self.lblWaterCalibrated.setSizePolicy(sizePolicy10)

        self.horizontalLayout_15.addWidget(self.lblWaterCalibrated)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_113 = QLabel(self.frame_25)
        self.label_113.setObjectName(u"label_113")
        sizePolicy1.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy1)
        self.label_113.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_113)

        self.spinWaterLeft = QDoubleSpinBox(self.frame_25)
        self.spinWaterLeft.setObjectName(u"spinWaterLeft")
        self.spinWaterLeft.setFrame(True)
        self.spinWaterLeft.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinWaterLeft.setReadOnly(False)
        self.spinWaterLeft.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinWaterLeft.setMaximum(200.000000000000000)
        self.spinWaterLeft.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinWaterLeft.setValue(0.000000000000000)

        self.verticalLayout_70.addWidget(self.spinWaterLeft)


        self.horizontalLayout_23.addLayout(self.verticalLayout_70)

        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_111 = QLabel(self.frame_25)
        self.label_111.setObjectName(u"label_111")
        sizePolicy1.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy1)
        self.label_111.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_111.setWordWrap(False)

        self.verticalLayout_68.addWidget(self.label_111)

        self.spinWaterDist = QDoubleSpinBox(self.frame_25)
        self.spinWaterDist.setObjectName(u"spinWaterDist")
        self.spinWaterDist.setFrame(True)
        self.spinWaterDist.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinWaterDist.setReadOnly(False)
        self.spinWaterDist.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinWaterDist.setMaximum(200.000000000000000)
        self.spinWaterDist.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinWaterDist.setValue(0.000000000000000)

        self.verticalLayout_68.addWidget(self.spinWaterDist)


        self.horizontalLayout_23.addLayout(self.verticalLayout_68)


        self.verticalLayout_11.addLayout(self.horizontalLayout_23)

        self.line_9 = QFrame(self.frame_25)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Shadow.Plain)
        self.line_9.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_11.addWidget(self.line_9)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_122 = QLabel(self.frame_25)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_122.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_122)

        self.lblMethilCalibrated = QLabel(self.frame_25)
        self.lblMethilCalibrated.setObjectName(u"lblMethilCalibrated")
        sizePolicy10.setHeightForWidth(self.lblMethilCalibrated.sizePolicy().hasHeightForWidth())
        self.lblMethilCalibrated.setSizePolicy(sizePolicy10)

        self.horizontalLayout_17.addWidget(self.lblMethilCalibrated)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_117 = QLabel(self.frame_25)
        self.label_117.setObjectName(u"label_117")
        sizePolicy1.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy1)
        self.label_117.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_71.addWidget(self.label_117)

        self.spinOtherLeft = QDoubleSpinBox(self.frame_25)
        self.spinOtherLeft.setObjectName(u"spinOtherLeft")
        self.spinOtherLeft.setFrame(True)
        self.spinOtherLeft.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinOtherLeft.setReadOnly(False)
        self.spinOtherLeft.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinOtherLeft.setMaximum(200.000000000000000)
        self.spinOtherLeft.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinOtherLeft.setValue(0.000000000000000)

        self.verticalLayout_71.addWidget(self.spinOtherLeft)


        self.horizontalLayout_24.addLayout(self.verticalLayout_71)

        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_115 = QLabel(self.frame_25)
        self.label_115.setObjectName(u"label_115")
        sizePolicy1.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy1)
        self.label_115.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_72.addWidget(self.label_115)

        self.spinOtherDist = QDoubleSpinBox(self.frame_25)
        self.spinOtherDist.setObjectName(u"spinOtherDist")
        self.spinOtherDist.setFrame(True)
        self.spinOtherDist.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinOtherDist.setReadOnly(False)
        self.spinOtherDist.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinOtherDist.setMaximum(200.000000000000000)
        self.spinOtherDist.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinOtherDist.setValue(0.000000000000000)

        self.verticalLayout_72.addWidget(self.spinOtherDist)


        self.horizontalLayout_24.addLayout(self.verticalLayout_72)


        self.verticalLayout_11.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_8.addWidget(self.frame_25)


        self.gridLayout_4.addWidget(self.frame_11, 0, 0, 1, 7)

        self.frame_14 = QFrame(self.Brillouin)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy7.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy7)
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.panFitting = QHBoxLayout()
        self.panFitting.setSpacing(0)
        self.panFitting.setObjectName(u"panFitting")

        self.horizontalLayout_7.addLayout(self.panFitting)

        self.verticalSlider = QSlider(self.frame_14)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy11)
        self.verticalSlider.setMaximum(10000)
        self.verticalSlider.setPageStep(0)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider.setInvertedControls(False)

        self.horizontalLayout_7.addWidget(self.verticalSlider)


        self.gridLayout_4.addWidget(self.frame_14, 5, 0, 3, 2)

        self.BrillFrame = QFrame(self.Brillouin)
        self.BrillFrame.setObjectName(u"BrillFrame")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.BrillFrame.sizePolicy().hasHeightForWidth())
        self.BrillFrame.setSizePolicy(sizePolicy12)
        self.BrillFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BrillFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.BrillFrame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.panBrill = QVBoxLayout()
        self.panBrill.setSpacing(0)
        self.panBrill.setObjectName(u"panBrill")
        self.cameraView = ImageView(self.BrillFrame)
        self.cameraView.setObjectName(u"cameraView")

        self.panBrill.addWidget(self.cameraView)


        self.horizontalLayout_16.addLayout(self.panBrill)


        self.gridLayout_4.addWidget(self.BrillFrame, 3, 0, 1, 2)

        self.line_3 = QFrame(self.Brillouin)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.gridLayout_4.addWidget(self.line_3, 2, 2, 6, 1)

        self.label_12 = QLabel(self.Brillouin)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        font3 = QFont()
        font3.setPointSize(12)
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.Brillouin)
        self.label_13.setObjectName(u"label_13")
        sizePolicy10.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy10)
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 2, 3, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblAqGraphCoordinatesLabel = QLabel(self.Brillouin)
        self.lblAqGraphCoordinatesLabel.setObjectName(u"lblAqGraphCoordinatesLabel")

        self.horizontalLayout_10.addWidget(self.lblAqGraphCoordinatesLabel)

        self.lblAqGraphCoordinatesNumbers = QLabel(self.Brillouin)
        self.lblAqGraphCoordinatesNumbers.setObjectName(u"lblAqGraphCoordinatesNumbers")

        self.horizontalLayout_10.addWidget(self.lblAqGraphCoordinatesNumbers)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.btnCopyAqPlotCoords1 = QToolButton(self.Brillouin)
        self.btnCopyAqPlotCoords1.setObjectName(u"btnCopyAqPlotCoords1")

        self.horizontalLayout_11.addWidget(self.btnCopyAqPlotCoords1)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.line_5 = QFrame(self.Brillouin)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Shadow.Plain)
        self.line_5.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_10.addWidget(self.line_5)

        self.lblAqGraphCoordinatesLabel_2 = QLabel(self.Brillouin)
        self.lblAqGraphCoordinatesLabel_2.setObjectName(u"lblAqGraphCoordinatesLabel_2")

        self.horizontalLayout_10.addWidget(self.lblAqGraphCoordinatesLabel_2)

        self.lblAqGraphCoordinatesNumbers_2 = QLabel(self.Brillouin)
        self.lblAqGraphCoordinatesNumbers_2.setObjectName(u"lblAqGraphCoordinatesNumbers_2")

        self.horizontalLayout_10.addWidget(self.lblAqGraphCoordinatesNumbers_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.btnCopyAqPlotCoords2 = QToolButton(self.Brillouin)
        self.btnCopyAqPlotCoords2.setObjectName(u"btnCopyAqPlotCoords2")

        self.horizontalLayout_13.addWidget(self.btnCopyAqPlotCoords2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_13)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 7, 3, 1, 4)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_4)

        self.label_118 = QLabel(self.Brillouin)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_118)

        self.spinAquiPlotMin = QDoubleSpinBox(self.Brillouin)
        self.spinAquiPlotMin.setObjectName(u"spinAquiPlotMin")
        self.spinAquiPlotMin.setSingleStep(0.010000000000000)
        self.spinAquiPlotMin.setValue(6.000000000000000)

        self.horizontalLayout_28.addWidget(self.spinAquiPlotMin)

        self.label_119 = QLabel(self.Brillouin)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_119)

        self.spinAquiPlotMax = QDoubleSpinBox(self.Brillouin)
        self.spinAquiPlotMax.setObjectName(u"spinAquiPlotMax")
        self.spinAquiPlotMax.setSingleStep(0.010000000000000)
        self.spinAquiPlotMax.setValue(6.600000000000000)

        self.horizontalLayout_28.addWidget(self.spinAquiPlotMax)


        self.gridLayout_4.addLayout(self.horizontalLayout_28, 2, 4, 1, 3)

        self.line_2 = QFrame(self.Brillouin)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 7)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.Brillouin)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_22)

        self.label_17 = QLabel(self.Brillouin)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_27.addWidget(self.label_17)

        self.spinBrillMinClip = QSpinBox(self.Brillouin)
        self.spinBrillMinClip.setObjectName(u"spinBrillMinClip")
        sizePolicy3.setHeightForWidth(self.spinBrillMinClip.sizePolicy().hasHeightForWidth())
        self.spinBrillMinClip.setSizePolicy(sizePolicy3)
        self.spinBrillMinClip.setMaximum(65535)
        self.spinBrillMinClip.setSingleStep(1000)

        self.horizontalLayout_27.addWidget(self.spinBrillMinClip)

        self.label_18 = QLabel(self.Brillouin)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_27.addWidget(self.label_18)

        self.spinBrillMaxClip = QSpinBox(self.Brillouin)
        self.spinBrillMaxClip.setObjectName(u"spinBrillMaxClip")
        sizePolicy3.setHeightForWidth(self.spinBrillMaxClip.sizePolicy().hasHeightForWidth())
        self.spinBrillMaxClip.setSizePolicy(sizePolicy3)
        self.spinBrillMaxClip.setMaximum(65535)
        self.spinBrillMaxClip.setSingleStep(1000)
        self.spinBrillMaxClip.setValue(65535)

        self.horizontalLayout_27.addWidget(self.spinBrillMaxClip)

        self.btnBrillAutoColor = QPushButton(self.Brillouin)
        self.btnBrillAutoColor.setObjectName(u"btnBrillAutoColor")

        self.horizontalLayout_27.addWidget(self.btnBrillAutoColor)


        self.gridLayout_4.addLayout(self.horizontalLayout_27, 2, 1, 1, 1)

        self.frame_16 = QFrame(self.Brillouin)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy8.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy8)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_16)
        self.label_27.setObjectName(u"label_27")
        sizePolicy7.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy7)
        self.label_27.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_27)

        self.label_40 = QLabel(self.frame_16)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_40)

        self.spinFittingLeft = QDoubleSpinBox(self.frame_16)
        self.spinFittingLeft.setObjectName(u"spinFittingLeft")
        sizePolicy3.setHeightForWidth(self.spinFittingLeft.sizePolicy().hasHeightForWidth())
        self.spinFittingLeft.setSizePolicy(sizePolicy3)
        self.spinFittingLeft.setReadOnly(True)
        self.spinFittingLeft.setMinimum(-99.989999999999995)

        self.horizontalLayout_19.addWidget(self.spinFittingLeft)

        self.label_120 = QLabel(self.frame_16)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_120)

        self.spinFittingRight = QDoubleSpinBox(self.frame_16)
        self.spinFittingRight.setObjectName(u"spinFittingRight")
        sizePolicy3.setHeightForWidth(self.spinFittingRight.sizePolicy().hasHeightForWidth())
        self.spinFittingRight.setSizePolicy(sizePolicy3)
        self.spinFittingRight.setReadOnly(True)
        self.spinFittingRight.setMinimum(-99.989999999999995)

        self.horizontalLayout_19.addWidget(self.spinFittingRight)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.spinMaxFitting = QSpinBox(self.frame_16)
        self.spinMaxFitting.setObjectName(u"spinMaxFitting")
        self.spinMaxFitting.setMaximum(999999)
        self.spinMaxFitting.setSingleStep(1000)
        self.spinMaxFitting.setValue(40000)
        self.spinMaxFitting.setDisplayIntegerBase(10)

        self.horizontalLayout_19.addWidget(self.spinMaxFitting)


        self.gridLayout_4.addWidget(self.frame_16, 4, 0, 1, 2)

        self.tabCameras.addTab(self.Brillouin, "")

        self.gridLayout.addWidget(self.tabCameras, 1, 0, 2, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCalibrate = QPushButton(self.frame)
        self.btnCalibrate.setObjectName(u"btnCalibrate")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(False)
        self.btnCalibrate.setFont(font4)

        self.horizontalLayout.addWidget(self.btnCalibrate)

        self.btnAquare = QPushButton(self.frame)
        self.btnAquare.setObjectName(u"btnAquare")
        sizePolicy6.setHeightForWidth(self.btnAquare.sizePolicy().hasHeightForWidth())
        self.btnAquare.setSizePolicy(sizePolicy6)
        self.btnAquare.setFont(font4)

        self.horizontalLayout.addWidget(self.btnAquare)

        self.btnExit = QPushButton(self.frame)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setFont(font4)

        self.horizontalLayout.addWidget(self.btnExit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)

        self.horizontalLayout_2.addWidget(self.label)

        self.txtPath = QLineEdit(self.frame)
        self.txtPath.setObjectName(u"txtPath")
        sizePolicy6.setHeightForWidth(self.txtPath.sizePolicy().hasHeightForWidth())
        self.txtPath.setSizePolicy(sizePolicy6)
        self.txtPath.setReadOnly(True)
        self.txtPath.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.txtPath)

        self.btnPathChange = QToolButton(self.frame)
        self.btnPathChange.setObjectName(u"btnPathChange")

        self.horizontalLayout_2.addWidget(self.btnPathChange)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy12.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy12)
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txtStageZ = QLineEdit(self.frame_2)
        self.txtStageZ.setObjectName(u"txtStageZ")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.txtStageZ.sizePolicy().hasHeightForWidth())
        self.txtStageZ.setSizePolicy(sizePolicy13)
        self.txtStageZ.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txtStageZ, 2, 5, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 6)

        self.btnCopyYPos = QPushButton(self.frame_2)
        self.btnCopyYPos.setObjectName(u"btnCopyYPos")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.btnCopyYPos.sizePolicy().hasHeightForWidth())
        self.btnCopyYPos.setSizePolicy(sizePolicy14)

        self.gridLayout_5.addWidget(self.btnCopyYPos, 3, 3, 1, 1)

        self.txtStageX = QLineEdit(self.frame_2)
        self.txtStageX.setObjectName(u"txtStageX")
        sizePolicy13.setHeightForWidth(self.txtStageX.sizePolicy().hasHeightForWidth())
        self.txtStageX.setSizePolicy(sizePolicy13)
        self.txtStageX.setReadOnly(True)
        self.txtStageX.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.txtStageX, 2, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy4.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy4)
        self.frame_17.setFrameShape(QFrame.Shape.Box)
        self.frame_17.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_29 = QGridLayout(self.frame_17)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.txtCMOSCurrentT = QLineEdit(self.frame_17)
        self.txtCMOSCurrentT.setObjectName(u"txtCMOSCurrentT")
        sizePolicy13.setHeightForWidth(self.txtCMOSCurrentT.sizePolicy().hasHeightForWidth())
        self.txtCMOSCurrentT.setSizePolicy(sizePolicy13)
        self.txtCMOSCurrentT.setReadOnly(True)

        self.gridLayout_29.addWidget(self.txtCMOSCurrentT, 2, 1, 1, 1)

        self.label_59 = QLabel(self.frame_17)
        self.label_59.setObjectName(u"label_59")
        sizePolicy1.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy1)
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_36 = QLabel(self.frame_17)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_29.addWidget(self.label_36, 0, 1, 1, 1)

        self.txtCMOSTargetT = QLineEdit(self.frame_17)
        self.txtCMOSTargetT.setObjectName(u"txtCMOSTargetT")
        sizePolicy13.setHeightForWidth(self.txtCMOSTargetT.sizePolicy().hasHeightForWidth())
        self.txtCMOSTargetT.setSizePolicy(sizePolicy13)
        self.txtCMOSTargetT.setReadOnly(True)

        self.gridLayout_29.addWidget(self.txtCMOSTargetT, 1, 1, 1, 1)

        self.label_60 = QLabel(self.frame_17)
        self.label_60.setObjectName(u"label_60")
        sizePolicy1.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy1)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_60, 1, 0, 1, 1)

        self.lblCMOSCooler = QLabel(self.frame_17)
        self.lblCMOSCooler.setObjectName(u"lblCMOSCooler")
        self.lblCMOSCooler.setFont(font3)

        self.gridLayout_29.addWidget(self.lblCMOSCooler, 1, 2, 2, 1)


        self.gridLayout_7.addWidget(self.frame_17, 4, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.btnBackward = QPushButton(self.frame_5)
        self.btnBackward.setObjectName(u"btnBackward")
        sizePolicy.setHeightForWidth(self.btnBackward.sizePolicy().hasHeightForWidth())
        self.btnBackward.setSizePolicy(sizePolicy)

        self.gridLayout_11.addWidget(self.btnBackward, 4, 1, 1, 1)

        self.btnForward = QPushButton(self.frame_5)
        self.btnForward.setObjectName(u"btnForward")
        sizePolicy.setHeightForWidth(self.btnForward.sizePolicy().hasHeightForWidth())
        self.btnForward.setSizePolicy(sizePolicy)

        self.gridLayout_11.addWidget(self.btnForward, 2, 1, 1, 1)

        self.btnLeft = QPushButton(self.frame_5)
        self.btnLeft.setObjectName(u"btnLeft")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.btnLeft.sizePolicy().hasHeightForWidth())
        self.btnLeft.setSizePolicy(sizePolicy15)
        self.btnLeft.setMinimumSize(QSize(30, 0))

        self.gridLayout_11.addWidget(self.btnLeft, 2, 0, 3, 1)

        self.btnRight = QPushButton(self.frame_5)
        self.btnRight.setObjectName(u"btnRight")
        sizePolicy15.setHeightForWidth(self.btnRight.sizePolicy().hasHeightForWidth())
        self.btnRight.setSizePolicy(sizePolicy15)
        self.btnRight.setMinimumSize(QSize(30, 0))

        self.gridLayout_11.addWidget(self.btnRight, 2, 2, 3, 1)

        self.btnDown = QPushButton(self.frame_5)
        self.btnDown.setObjectName(u"btnDown")
        sizePolicy13.setHeightForWidth(self.btnDown.sizePolicy().hasHeightForWidth())
        self.btnDown.setSizePolicy(sizePolicy13)

        self.gridLayout_11.addWidget(self.btnDown, 1, 0, 1, 1)

        self.btnUp = QPushButton(self.frame_5)
        self.btnUp.setObjectName(u"btnUp")
        sizePolicy13.setHeightForWidth(self.btnUp.sizePolicy().hasHeightForWidth())
        self.btnUp.setSizePolicy(sizePolicy13)

        self.gridLayout_11.addWidget(self.btnUp, 1, 2, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 3)

        self.spinMoveStep = QDoubleSpinBox(self.frame_5)
        self.spinMoveStep.setObjectName(u"spinMoveStep")
        self.spinMoveStep.setMinimum(-9999.989999999999782)
        self.spinMoveStep.setMaximum(9999.989999999999782)
        self.spinMoveStep.setSingleStep(10.000000000000000)
        self.spinMoveStep.setValue(50.000000000000000)

        self.gridLayout_11.addWidget(self.spinMoveStep, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btnXAbsGo = QPushButton(self.frame_3)
        self.btnXAbsGo.setObjectName(u"btnXAbsGo")
        sizePolicy13.setHeightForWidth(self.btnXAbsGo.sizePolicy().hasHeightForWidth())
        self.btnXAbsGo.setSizePolicy(sizePolicy13)
        self.btnXAbsGo.setMinimumSize(QSize(40, 0))

        self.gridLayout_6.addWidget(self.btnXAbsGo, 3, 0, 1, 1)

        self.btnYAbsGo = QPushButton(self.frame_3)
        self.btnYAbsGo.setObjectName(u"btnYAbsGo")
        sizePolicy13.setHeightForWidth(self.btnYAbsGo.sizePolicy().hasHeightForWidth())
        self.btnYAbsGo.setSizePolicy(sizePolicy13)
        self.btnYAbsGo.setMinimumSize(QSize(40, 0))

        self.gridLayout_6.addWidget(self.btnYAbsGo, 3, 1, 1, 1)

        self.btnZAbsGo = QPushButton(self.frame_3)
        self.btnZAbsGo.setObjectName(u"btnZAbsGo")
        sizePolicy13.setHeightForWidth(self.btnZAbsGo.sizePolicy().hasHeightForWidth())
        self.btnZAbsGo.setSizePolicy(sizePolicy13)
        self.btnZAbsGo.setMinimumSize(QSize(40, 0))

        self.gridLayout_6.addWidget(self.btnZAbsGo, 3, 2, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 3)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 3)

        self.spinAbsolutePosition = QDoubleSpinBox(self.frame_3)
        self.spinAbsolutePosition.setObjectName(u"spinAbsolutePosition")
        self.spinAbsolutePosition.setKeyboardTracking(True)
        self.spinAbsolutePosition.setMinimum(-99999.990000000005239)
        self.spinAbsolutePosition.setMaximum(99999.990000000005239)

        self.gridLayout_6.addWidget(self.spinAbsolutePosition, 2, 0, 1, 3)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_22 = QGridLayout(self.frame_7)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_22.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_22.addWidget(self.label_20, 1, 0, 1, 1)

        self.txtRegionToLaserXum = QLineEdit(self.frame_7)
        self.txtRegionToLaserXum.setObjectName(u"txtRegionToLaserXum")
        sizePolicy13.setHeightForWidth(self.txtRegionToLaserXum.sizePolicy().hasHeightForWidth())
        self.txtRegionToLaserXum.setSizePolicy(sizePolicy13)
        self.txtRegionToLaserXum.setReadOnly(True)

        self.gridLayout_22.addWidget(self.txtRegionToLaserXum, 0, 1, 1, 1)

        self.txtRegionToLaserYum = QLineEdit(self.frame_7)
        self.txtRegionToLaserYum.setObjectName(u"txtRegionToLaserYum")
        sizePolicy13.setHeightForWidth(self.txtRegionToLaserYum.sizePolicy().hasHeightForWidth())
        self.txtRegionToLaserYum.setSizePolicy(sizePolicy13)
        self.txtRegionToLaserYum.setReadOnly(True)

        self.gridLayout_22.addWidget(self.txtRegionToLaserYum, 1, 1, 1, 1)

        self.btnSetRegionToLaser = QPushButton(self.frame_7)
        self.btnSetRegionToLaser.setObjectName(u"btnSetRegionToLaser")

        self.gridLayout_22.addWidget(self.btnSetRegionToLaser, 1, 2, 1, 2)

        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_21, 0, 2, 1, 1)

        self.comboLensSlot = QComboBox(self.frame_7)
        self.comboLensSlot.setObjectName(u"comboLensSlot")

        self.gridLayout_22.addWidget(self.comboLensSlot, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.frame_7, 2, 0, 1, 2)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setFrameShape(QFrame.Shape.Box)
        self.frame_15.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_26 = QGridLayout(self.frame_15)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.txtBrillCurrentT = QLineEdit(self.frame_15)
        self.txtBrillCurrentT.setObjectName(u"txtBrillCurrentT")
        sizePolicy13.setHeightForWidth(self.txtBrillCurrentT.sizePolicy().hasHeightForWidth())
        self.txtBrillCurrentT.setSizePolicy(sizePolicy13)
        self.txtBrillCurrentT.setReadOnly(True)

        self.gridLayout_26.addWidget(self.txtBrillCurrentT, 2, 1, 1, 1)

        self.label_38 = QLabel(self.frame_15)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_26.addWidget(self.label_32, 0, 1, 1, 1)

        self.txtBrillTargetT = QLineEdit(self.frame_15)
        self.txtBrillTargetT.setObjectName(u"txtBrillTargetT")
        sizePolicy13.setHeightForWidth(self.txtBrillTargetT.sizePolicy().hasHeightForWidth())
        self.txtBrillTargetT.setSizePolicy(sizePolicy13)
        self.txtBrillTargetT.setReadOnly(True)

        self.gridLayout_26.addWidget(self.txtBrillTargetT, 1, 1, 1, 1)

        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_37, 1, 0, 1, 1)

        self.lblBrillCooler = QLabel(self.frame_15)
        self.lblBrillCooler.setObjectName(u"lblBrillCooler")
        self.lblBrillCooler.setFont(font3)

        self.gridLayout_26.addWidget(self.lblBrillCooler, 1, 2, 2, 1)


        self.gridLayout_7.addWidget(self.frame_15, 4, 1, 1, 1)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.Box)
        self.frame_19.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_25 = QGridLayout(self.frame_19)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.spinLight = QSpinBox(self.frame_19)
        self.spinLight.setObjectName(u"spinLight")
        self.spinLight.setMaximum(255)

        self.gridLayout_25.addWidget(self.spinLight, 0, 3, 1, 1)

        self.btnLightP2 = QPushButton(self.frame_19)
        self.btnLightP2.setObjectName(u"btnLightP2")
        sizePolicy13.setHeightForWidth(self.btnLightP2.sizePolicy().hasHeightForWidth())
        self.btnLightP2.setSizePolicy(sizePolicy13)
        self.btnLightP2.setMinimumSize(QSize(25, 0))

        self.gridLayout_25.addWidget(self.btnLightP2, 0, 5, 1, 1)

        self.btnTurnOffLED = QPushButton(self.frame_19)
        self.btnTurnOffLED.setObjectName(u"btnTurnOffLED")
        sizePolicy13.setHeightForWidth(self.btnTurnOffLED.sizePolicy().hasHeightForWidth())
        self.btnTurnOffLED.setSizePolicy(sizePolicy13)
        self.btnTurnOffLED.setMinimumSize(QSize(25, 0))

        self.gridLayout_25.addWidget(self.btnTurnOffLED, 0, 1, 1, 1)

        self.btnLightP1 = QPushButton(self.frame_19)
        self.btnLightP1.setObjectName(u"btnLightP1")
        sizePolicy13.setHeightForWidth(self.btnLightP1.sizePolicy().hasHeightForWidth())
        self.btnLightP1.setSizePolicy(sizePolicy13)
        self.btnLightP1.setMinimumSize(QSize(25, 0))

        self.gridLayout_25.addWidget(self.btnLightP1, 0, 4, 1, 1)

        self.btnLightM1 = QPushButton(self.frame_19)
        self.btnLightM1.setObjectName(u"btnLightM1")
        sizePolicy13.setHeightForWidth(self.btnLightM1.sizePolicy().hasHeightForWidth())
        self.btnLightM1.setSizePolicy(sizePolicy13)
        self.btnLightM1.setMinimumSize(QSize(25, 0))

        self.gridLayout_25.addWidget(self.btnLightM1, 0, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_29)

        self.comboMirrorDeck = QComboBox(self.frame_19)
        self.comboMirrorDeck.setObjectName(u"comboMirrorDeck")

        self.horizontalLayout_9.addWidget(self.comboMirrorDeck)

        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_30)

        self.comboLightPath = QComboBox(self.frame_19)
        self.comboLightPath.addItem("")
        self.comboLightPath.addItem("")
        self.comboLightPath.addItem("")
        self.comboLightPath.setObjectName(u"comboLightPath")
        sizePolicy14.setHeightForWidth(self.comboLightPath.sizePolicy().hasHeightForWidth())
        self.comboLightPath.setSizePolicy(sizePolicy14)

        self.horizontalLayout_9.addWidget(self.comboLightPath)


        self.gridLayout_25.addLayout(self.horizontalLayout_9, 1, 0, 1, 6)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_25.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_19, 3, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_4, 4, 0, 1, 6)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy10.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy10)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 2, 2, 1, 1)

        self.txtStageY = QLineEdit(self.frame_2)
        self.txtStageY.setObjectName(u"txtStageY")
        self.txtStageY.setEnabled(True)
        sizePolicy13.setHeightForWidth(self.txtStageY.sizePolicy().hasHeightForWidth())
        self.txtStageY.setSizePolicy(sizePolicy13)
        self.txtStageY.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txtStageY, 2, 3, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy10.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy10)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 2, 4, 1, 1)

        self.btnCopyZPos = QPushButton(self.frame_2)
        self.btnCopyZPos.setObjectName(u"btnCopyZPos")
        sizePolicy14.setHeightForWidth(self.btnCopyZPos.sizePolicy().hasHeightForWidth())
        self.btnCopyZPos.setSizePolicy(sizePolicy14)

        self.gridLayout_5.addWidget(self.btnCopyZPos, 3, 5, 1, 1)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.lblCMOSAlive = QLabel(self.frame_9)
        self.lblCMOSAlive.setObjectName(u"lblCMOSAlive")
        font5 = QFont()
        font5.setPointSize(14)
        self.lblCMOSAlive.setFont(font5)
        self.lblCMOSAlive.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lblCMOSAlive)

        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_16)

        self.lblBrillAlive = QLabel(self.frame_9)
        self.lblBrillAlive.setObjectName(u"lblBrillAlive")
        self.lblBrillAlive.setFont(font5)
        self.lblBrillAlive.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lblBrillAlive)


        self.gridLayout_5.addWidget(self.frame_9, 5, 0, 1, 6)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy10.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy10)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.btnCopyXPos = QPushButton(self.frame_2)
        self.btnCopyXPos.setObjectName(u"btnCopyXPos")
        sizePolicy14.setHeightForWidth(self.btnCopyXPos.sizePolicy().hasHeightForWidth())
        self.btnCopyXPos.setSizePolicy(sizePolicy14)

        self.gridLayout_5.addWidget(self.btnCopyXPos, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy16)

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.gridLayout.addWidget(self.frame, 1, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabCameras.setCurrentIndex(1)
        self.comboLightPath.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Levels:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.txtGraphCoorninates.setText(QCoreApplication.translate("MainWindow", u"Mouse Click Coordinate (X, Y):", None))
        self.btnCMOSAutoScale.setText(QCoreApplication.translate("MainWindow", u"Set Auto Level", None))
        self.btnStartPauseCMOS.setText(QCoreApplication.translate("MainWindow", u"Start/Pause", None))
        self.btnSaveCMOS.setText(QCoreApplication.translate("MainWindow", u"Save CMOS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Exposure (s):", None))
        self.btnSetCMOSCameraParameters.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.btnShowAdminSettings.setText(QCoreApplication.translate("MainWindow", u"Admin Settings", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Laser Position ", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"X: ", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Y: ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Micron/Pixel ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Active Lens: ", None))
        self.lblLenz1.setText(QCoreApplication.translate("MainWindow", u"999x", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("MainWindow", u"Apply and Save", None))
        self.tabCameras.setTabText(self.tabCameras.indexOf(self.CMOS), QCoreApplication.translate("MainWindow", u"CMOS Tab", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"#HPixels", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u" #VPixels", None))
        self.btnStartPauseBrill.setText(QCoreApplication.translate("MainWindow", u"Start/Pause", None))
        self.btnShowFullBrill.setText(QCoreApplication.translate("MainWindow", u"Preview Full Image", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"HStart", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"VStart", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Exposure (s)", None))
        self.btnBrillSetParameters.setText(QCoreApplication.translate("MainWindow", u"Set Parameters", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"YStepSize", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Current Shift (GHz)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"GHz/pixel", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"XDistance", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"FSR", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"YDistance", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"CalNum", None))
        self.btnAbortAquisition.setText(QCoreApplication.translate("MainWindow", u"Abort Acquisition", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"ZStepSize", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"XStepSize", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"STD Last Line", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"ZDistance", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Scan Plane", None))
        self.comboScanPlane.setItemText(0, QCoreApplication.translate("MainWindow", u"XY", None))
        self.comboScanPlane.setItemText(1, QCoreApplication.translate("MainWindow", u"XZ", None))
        self.comboScanPlane.setItemText(2, QCoreApplication.translate("MainWindow", u"YZ", None))

        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Calibration Values", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.lblWaterCalibrated.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.lblMethilCalibrated.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u" Distance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Brillouin Camera", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Acquisition Plot", None))
        self.lblAqGraphCoordinatesLabel.setText(QCoreApplication.translate("MainWindow", u"Click (X,Y) (um):", None))
        self.lblAqGraphCoordinatesNumbers.setText("")
        self.btnCopyAqPlotCoords1.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.lblAqGraphCoordinatesLabel_2.setText(QCoreApplication.translate("MainWindow", u"(X,Y,I) (pix):", None))
        self.lblAqGraphCoordinatesNumbers_2.setText("")
        self.btnCopyAqPlotCoords2.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Color Min", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Color Max", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Clipping:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.btnBrillAutoColor.setText(QCoreApplication.translate("MainWindow", u"Set Auto Level", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Curve Fitting", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y Lim", None))
        self.tabCameras.setTabText(self.tabCameras.indexOf(self.Brillouin), QCoreApplication.translate("MainWindow", u"Brillouin Tab", None))
        self.btnCalibrate.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.btnAquare.setText(QCoreApplication.translate("MainWindow", u"Acquire", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Working Path:", None))
        self.txtPath.setText("")
        self.btnPathChange.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Stage Position (um)", None))
        self.btnCopyYPos.setText(QCoreApplication.translate("MainWindow", u"Copy Y", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Current (C)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CMOS Temp.", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Target (C)", None))
        self.lblCMOSCooler.setText(QCoreApplication.translate("MainWindow", u"\u2744\ufe0f", None))
        self.btnBackward.setText(QCoreApplication.translate("MainWindow", u"Backward", None))
        self.btnForward.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        self.btnLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btnRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.btnDown.setText(QCoreApplication.translate("MainWindow", u"Dwn", None))
        self.btnUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Move By Step (um)", None))
        self.btnXAbsGo.setText(QCoreApplication.translate("MainWindow", u"X Go", None))
        self.btnYAbsGo.setText(QCoreApplication.translate("MainWindow", u"Y Go", None))
        self.btnZAbsGo.setText(QCoreApplication.translate("MainWindow", u"Z Go", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Position (um):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Move To Absolute", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Region To Laser X (um) ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Region To Laser Y (um) ", None))
        self.txtRegionToLaserXum.setText("")
        self.btnSetRegionToLaser.setText(QCoreApplication.translate("MainWindow", u"Set Region", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Lens Slot", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Current (C)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Brillouin Temp.", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Target (C)", None))
        self.lblBrillCooler.setText(QCoreApplication.translate("MainWindow", u"\u2744\ufe0f", None))
        self.btnLightP2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.btnTurnOffLED.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.btnLightP1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.btnLightM1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mirror Deck", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Light Path", None))
        self.comboLightPath.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera", None))
        self.comboLightPath.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera + Eye", None))
        self.comboLightPath.setItemText(2, QCoreApplication.translate("MainWindow", u"Eye", None))

        self.comboLightPath.setCurrentText(QCoreApplication.translate("MainWindow", u"Eye", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Light Brightness", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.btnCopyZPos.setText(QCoreApplication.translate("MainWindow", u"Copy Z", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CMOS Active: ", None))
        self.lblCMOSAlive.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Brillouin Active: ", None))
        self.lblBrillAlive.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btnCopyXPos.setText(QCoreApplication.translate("MainWindow", u"Copy X", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Log", None))
    # retranslateUi

