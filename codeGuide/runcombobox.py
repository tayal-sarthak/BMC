import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from combobox import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.pressed)

    def pressed(self):
        try:
            x = int(self.ui.comboX.currentText())
            y = int(self.ui.comboY.currentText())
            xor = x ^ y
            self.ui.label.setText(f"X XOR Y = {xor}")
        except Exception as e:
            self.ui.label.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())