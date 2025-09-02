import sys
import random
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def init(self):
        super().init()
        self.hello = ["Ha llo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
if __name__ == "main":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("Hello App")
    widget.show()

    sys.exit(app.exec())