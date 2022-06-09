# IMPORT MODULES
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # SHOW THE APPLICATION
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    