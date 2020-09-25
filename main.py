import random
import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow

from screens.analyse import Ui_analyze
from screens.exchange import Ui_boursewindoww


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui =Ui_boursewindoww()
        self.ui.setupUi(self )
        _style = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window =MainWindow()
    window.show()
    sys.exit(app.exec_())


# def magic(self):
#     self.text.setText(random.choice(self.hello))
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MyWidget()
#     widget.resize(400, 300)
#     widget.show()
#
#     sys.exit(app.exec_())

