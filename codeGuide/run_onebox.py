import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from onebox import Ui_MainWindow  # auto-generated from onebox.ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button to popup method
        self.ui.pushButton.clicked.connect(self.show_popup)

    def show_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Critical) # i love critical
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText("informative text, ya!")
        msg.setDetailedText("details")
        msg.buttonClicked.connect(self.popup_button)
        msg.exec()
    def popup_button(self, i):
        print(i.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())