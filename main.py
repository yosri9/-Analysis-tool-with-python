import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from screens.analyse import Ui_analyze
from screens.boursewindow import Ui_boursewindoww


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui =Ui_analyze()
        self.ui.setupUi(self )
        _style = ""
        with open("styling/styling.qss", "r") as f:
            _style = f.read()
        self.setStyleSheet(_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

