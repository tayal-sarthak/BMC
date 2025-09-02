import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui  import QImage, QPixmap



class CamThread(QThread): #camthread captures a qImage to the GUI
    frame_ready = Signal(QImage)

    def __init__(self):
        super().__init__()
        self.cap     = cv2.VideoCapture(0) #open cam
        self.filter  = "none" #the button on rn
        self.running = True #the boolean loop statement

    def stop(self):
        self.running = False  #if we stop than we free webcam
        self.wait()
        self.cap.release()

    def run(self): #auto runs on execute
        while self.running:
            ok, frame = self.cap.read() #this is one BGR frame
            if not ok:
                continue

            # why 110 and why 80? this is because its hard to find that PURE exact green. Thats why we are doing upper and lower bounds. we filter thru images
            # some notable videos: https://www.youtube.com/watch?v=WXeO2qlfGuY&ab_channel=Life2Coding (good), https://www.youtube.com/watch?v=GnRQZT15hiE&ab_channel=CodeLines (wasnt great) 
            if   self.filter == "red":
                frame[:,:,0]=0
                frame[:,:,1]=0
                # lower, upper = (0, 0, 110),  (80,  80, 255)
                # mask = cv2.inRange(frame, lower, upper)

            elif self.filter == "green":
                frame[:,:,0]=0 # set all blue to 0
                frame[:,:,2]=0
                # lower, upper = (0, 110, 0),  (80, 255,  80)
                # mask = cv2.inRange(frame, lower, upper)

            elif self.filter == "blue":
                frame[:,:,1]=0
                frame[:,:,2]=0
                # lower, upper = (110, 0, 0), (255,  80,  80)
                # mask = cv2.inRange(frame, lower, upper)
            elif self.filter == "inrange":
                frame
            
            else:                       # “Normal” button
                mask = None
            
            
            # ---------------------------------------------------------------

            shown = (
                cv2.bitwise_and(frame, frame, mask=mask) #mask holds binary image for keep or discard
                if mask is not None else frame
            )

            rgb = cv2.cvtColor(shown, cv2.COLOR_BGR2RGB) #again convert cause o pencv is bgr we qt wants rgb. . . .  .
            h, w, _ = rgb.shape #height width and channels 
            img = QImage(rgb.data, w, h, 3 * w, QImage.Format_RGB888) # 3 * w is for the byte per line stride , 888 is the bit size
            self.frame_ready.emit(img)
            #https://www.youtube.com/watch?v=dTDgbx-XelY&ab_channel=SH <--- great video for this!!!!  ------------------------------

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RGB filter cam")

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter) #pixmap needs to be centered, thats why we d othis

        self.thread = CamThread() #again, grabs the framse
        self.thread.frame_ready.connect(self.show_frame)
        self.thread.start() #run() 

        b_red   = QPushButton("Red") #buttons
        b_green = QPushButton("Green")
        b_blue  = QPushButton("Blue")
        b_none  = QPushButton("Normal")

        # flip the filter string inside the thread
        b_red.clicked.connect(lambda: setattr(self.thread, "filter", "red")) #(clicked) is true when the buttons are pressed. idk too much, heres video:
        b_green.clicked.connect(lambda: setattr(self.thread, "filter", "green")) # really good but boring https://www.youtube.com/watch?v=akAKMw7lQf8&ab_channel=KDAB
        b_blue.clicked.connect(lambda: setattr(self.thread, "filter", "blue")) # not boring but pretty bad https://www.youtube.com/watch?v=aDej6q6WpBo&ab_channel=FinxterAINuggets
        b_none.clicked.connect(lambda: setattr(self.thread, "filter", "none"))

        bar = QHBoxLayout()
        for b in (b_red, b_green, b_blue, b_none):
            bar.addWidget(b)

        lay = QVBoxLayout()
        lay.addWidget(self.label)
        lay.addLayout(bar)

        box = QWidget()
        box.setLayout(lay)
        self.setCentralWidget(box)
        self.resize(700, 550)

    def show_frame(self, img):
        self.label.setPixmap(QPixmap.fromImage(img))

    def closeEvent(self, e):
        self.thread.stop()
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window().show()
    sys.exit(app.exec())