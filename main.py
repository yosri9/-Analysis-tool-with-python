import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from api.Bug import *
from  screens.analyse import Ui_analyze

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_analyze()
        self.ui.setupUi(self )

if __name__ == "__main__":
    fetchBugs()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
   # fetchBugs( "root" , "ya3tik 3AR")

