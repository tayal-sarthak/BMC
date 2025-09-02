import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from test import Ui_MainWindow  # This is the auto-generated UI class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect menu actions to methods
        self.ui.actionNew.triggered.connect(lambda: self.update_label("New was clicked"))
        self.ui.actionSave.triggered.connect(lambda: self.update_label("Save was clicked"))
        self.ui.actionCopy.triggered.connect(lambda: self.update_label("Copy was clicked"))
        self.ui.actionPaste.triggered.connect(lambda: self.update_label("Paste was clicked"))

    def update_label(self, text):
        self.ui.label.setText(text)
        self.ui.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())