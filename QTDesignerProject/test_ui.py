import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import ui_compiled

FrameWidth = 800
FrameHeight = 600

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_compiled.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_camera)
        self.timer.start(30)

        self.ui.cameraView.ui.histogram.hide()
        self.ui.cameraView.ui.roiBtn.hide()
        self.ui.cameraView.ui.menuBtn.hide()

    def show_camera(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        frame = cv2.flip(frame, 0)  # flip vertically to fix upside down
        frame = cv2.resize(frame, (FrameWidth, FrameHeight))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.ui.cameraView.setImage(frame, autoLevels=False, levels=(0, 255))

    def closeEvent(self, e):
        self.cap.release()

app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())