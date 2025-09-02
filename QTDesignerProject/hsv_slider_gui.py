import cv2
import numpy as np
import sys
from PySide6.QtWidgets import QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
# install pyqtgraph library
#integrate pyqtgraph library into THIS project
# replace label with a widget (from PyQTGraph)
# for now, outpout cam ( add things as i wish)
# ImageAnalysis

# yep, actually using pyqtgraph now
# USE DESIGNER!
# nexts teps till end of august 




# run code from pythonGUI.ui code into QT Designer
# run code that can make it qt designer
# put pyqtgraph widgets in place of it
# opens the py, put pyqtgraph in camera and plot


import pyqtgraph as pg
pg.setConfigOptions(imageAxisOrder='row-major')  # make numpy-style images behave, because why not

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pick a Color Range")

        self.camera = cv2.VideoCapture(0)

        # self.video_feed = QLabel()
        # self.video_feed.setFixedSize(640, 480)
        # ^ using pg instead of QLabel, so that gets the boot
        self.video_feed = pg.GraphicsLayoutWidget() 
        self.plot = self.video_feed.addPlot()        
        self.plot.setMenuEnabled(False)              
        self.plot.setMouseEnabled(x=False, y=False)  # not a science fair demo
        self.plot.invertY(True)                      # match top-left origin like cv2 !! important gang
        self.plot.setAspectLocked(True)              
        self.img_item = pg.ImageItem()               
        self.plot.addItem(self.img_item)

        self.bars = []
        self.bar_names = ["Hue Low", "Sat Low", "Val Low", "Hue High", "Sat High", "Val High"]
        bar_blocks = []

        for i, label_text in enumerate(self.bar_names):
            bar = QSlider(Qt.Horizontal)
            bar.setMinimum(0)
            bar.setMaximum(179 if i % 3 == 0 else 255)
            bar.setValue(0 if i < 3 else (179 if i % 3 == 0 else 255))
            self.bars.append(bar)

            label = QLabel(label_text)
            group = QVBoxLayout()
            group.addWidget(label)
            group.addWidget(bar)
            bar_blocks.append(group)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_feed) 

        bars_layout = QHBoxLayout()
        left_side = QVBoxLayout()
        right_side = QVBoxLayout()
        for i in range(3):
            left_side.addLayout(bar_blocks[i])
            right_side.addLayout(bar_blocks[i + 3])
        bars_layout.addLayout(left_side)
        bars_layout.addLayout(right_side)

        main_layout.addLayout(bars_layout)
        self.setLayout(main_layout)

        self.loop = QTimer()
        self.loop.timeout.connect(self.draw)
        self.loop.start(30)

    def draw(self):
        ok, image = self.camera.read()
        if not ok:
            return

        image = cv2.resize(image, (640, 480))  # old size so nothing bad
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h1, s1, v1 = [b.value() for b in self.bars[:3]]
        h2, s2, v2 = [b.value() for b in self.bars[3:]]

        lower_bound = np.array([h1, s1, v1])
        upper_bound = np.array([h2, s2, v2])

        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        image[mask == 0] = 0

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # pg wants RGB not BGR
        # ^ we’re not doing QImage/QPixmap anymore
        self.img_item.setImage(rgb, autoLevels=False) 

    def closeEvent(self, event):
        self.camera.release()

app = QApplication(sys.argv)
window = ColorPicker()
window.show()
app.exec()