import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from vid5 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.photo.clear()

        base_dir = os.path.dirname(__file__)
        self.image_dog = os.path.join(base_dir, "IMG-4683.jpg")
        self.image_cat = os.path.join(base_dir, "IMG-4743.jpg")

        self.ui.noormal.clicked.connect(self.show_dog)
        self.ui.nootnormal.clicked.connect(self.show_cat)

    def show_dog(self):
        if not os.path.exists(self.image_dog):
            print(f"Image not found: {self.image_dog}")
            return
        pixmap = QPixmap(self.image_dog)
        self.ui.photo.setPixmap(pixmap)

    def show_cat(self):
        if not os.path.exists(self.image_cat):
            print(f"Image not found: {self.image_cat}")
            return
        pixmap = QPixmap(self.image_cat)
        self.ui.photo.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())