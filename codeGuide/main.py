from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # position x=1000, y=200, size width=300, height=300
        self.setGeometry(1000, 200, 300, 300)
        self.setWindowTitle("Tech With Tim!")
        self.initUI()

    def initUI(self):
        # add a label
        self.label = QLabel("my first label", self)
        self.label.move(50, 50)

        # add a button
        self.b1 = QPushButton("Click Me!", self)
        self.b1.move(50, 100)
        self.b1.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("You Pressed the Button!")
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())