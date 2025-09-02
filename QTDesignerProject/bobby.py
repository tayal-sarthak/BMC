import sys
import cv2  # the camera friend
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer  #this lets us grab a new camera frame for x milliseconds we want

 
class MyCoolCameraThing(QWidget): #essentially, a class for the camera window. 
    def __init__(self): #q widget is base class of GUi elements.
        super().__init__() #call parent class constructor 

        self.setWindowTitle("camera thingy wow") #window title ontop of frame

        # ok here's a label
        self.thing_on_screen = QLabel("waiting for the camera... be patient pls") #display images, frame from camera
        self.thing_on_screen.setFixedSize(640, 480)  # normal size, ion know what i was doin last time
        self.useless_button = QPushButton("press me for no reason")
        self.useless_button.clicked.connect(self.say_something_pointless)
        # stacking stuff vertically because why not
        my_layout = QVBoxLayout() #yes, vertical laytout, but mainly tells self ot use the layout
        my_layout.addWidget(self.thing_on_screen)
        my_layout.addWidget(self.useless_button)
        self.setLayout(my_layout)

        # say hi to the camera
        self.eyeball = cv2.VideoCapture(0)  # 0 is the default cam
        if not self.eyeball.isOpened():
            self.thing_on_screen.setText("camera wont open dawg") # if cam aint opened it says that
            return #ends it

        # set up our magical time loop
        self.loopy = QTimer() 
        self.loopy.timeout.connect(self.make_new_frame_happen) #(30-33 times a second)
        self.loopy.start(30)  # try to look alive ~30 fps is good enough

    def make_new_frame_happen(self):
        # take a quick peek for the frame through a camerA 
        success, picture = self.eyeball.read()
        if not success:
            return  # nothing lol

        # openCV speaks in bgr, but we want rgb no??? lets convert 
        colorful_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)

        # figure out the size of this colorful masterpiece
        h, w, c = colorful_picture.shape
        bits_per_line = c * w

        # turn numpy thing into qt thing. This took me forever to figure out. 
        qt_version = QImage( 
            colorful_picture.data, w, h, bits_per_line, QImage.Format_RGB888
        )

        # finally, slap the image onto the label
        self.thing_on_screen.setPixmap(QPixmap.fromImage(qt_version))
    def say_something_pointless(self):
        print("test")  # it literally just does this. wow.
    def closeEvent(self, whatever):  # close window event when user closes window 
        self.loopy.stop()
        if self.eyeball.isOpened():
            self.eyeball.release()  # let go of the camera
        whatever.accept()


if __name__ == "__main__": #this is typical qt thing to run. creates cvustom camera viewer window
    app = QApplication(sys.argv)

    window = MyCoolCameraThing()
    window.show()

    sys.exit(app.exec())#keeps app alive until window is closed