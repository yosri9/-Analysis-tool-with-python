import sys
from asyncio.windows_events import NULL
from tkinter.tix import Form

import paramiko
from PySide2.QtCore import Slot, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog, QLabel, QGridLayout, QListWidgetItem)

from api import Authentication, ApiUtilities
from databases.models.exchange import Exchange
from databases import database, Database


class ui_add_exchange(QDialog):
    def __init__(self, *args, **kwargs):
        super(ui_add_exchange, self).__init__(*args, **kwargs)
        self.setWindowTitle("Exchange Item")
        icon = QIcon()
        icon.addFile(u"images/stock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: grey;")

        self.nameLabel = QLabel(self.tr("&Exchange Name:"))
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setStyleSheet("background-color: white;")
        self.nameLabel.setBuddy(self.nameLineEdit)

        self.ipAddressLabel = QLabel(self.tr("IP Address:"))
        self.ipAddressLineEdit = QLineEdit()
        self.ipAddressLineEdit.setStyleSheet("background-color: white;")
        self.ipAddressLabel.setBuddy(self.ipAddressLineEdit)

        self.usernameLabel = QLabel(self.tr("Username:"))
        self.usernameLineEdit = QLineEdit()
        self.usernameLineEdit.setStyleSheet("background-color: white;")
        self.usernameLabel.setBuddy(self.ipAddressLineEdit)

        self.passwordLabel = QLabel(self.tr("Password:"))
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setStyleSheet("background-color: white;")
        self.passwordLabel.setBuddy(self.ipAddressLineEdit)

        self.showError = QLabel(self.tr(""))
        self.showError.setStyleSheet("color: red ; " )

        self.addButton = QPushButton("ADD EXCHANGE")
        self.addButton.clicked.connect(self.storeExchangeElements)

        self.testButton = QPushButton("TEST CONNECTION")
        self.testButton.clicked.connect(self.testConnection)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.nameLabel, 0, 0)
        gridLayout.addWidget(self.nameLineEdit, 0, 1)
        gridLayout.addWidget(self.ipAddressLabel, 1, 0)
        gridLayout.addWidget(self.ipAddressLineEdit, 1, 1)
        gridLayout.addWidget(self.usernameLabel, 2, 0)
        gridLayout.addWidget(self.usernameLineEdit, 2, 1)
        gridLayout.addWidget(self.passwordLabel, 3, 0)
        gridLayout.addWidget(self.passwordLineEdit, 3, 1)
        gridLayout.addWidget(self.showError, 4, 1)
        gridLayout.addWidget(self.addButton, 5, 0)
        gridLayout.addWidget(self.testButton, 5, 1)

        self.setLayout(gridLayout)

    # Greets the user

    @Slot()
    def storeExchangeElements(self):
        Database.analysisToolDatabase()
        exchange = Exchange(None, self.nameLineEdit.text(), self.ipAddressLineEdit.text(),
                            self.usernameLineEdit.text(), self.passwordLineEdit.text())
        if self.addButton.text() =="ADD EXCHANGE":
            Database.insert(exchange)

        self.close()

    @Slot()
    def testConnection(self):
        ApiUtilities.USERNAME = self.usernameLineEdit.text()
        ApiUtilities.PASSWORD = self.passwordLineEdit.text()
        ApiUtilities.MAIN_API_URL = self.ipAddressLineEdit.text()
        try:
            Authentication.login()
            # client = paramiko.SSHClient()
            # client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            # client.connect(hostname=IPAddress, username=userName, password=password)
            self.showError.setStyleSheet("color : green ;")
            self.showError.setText("Connection Succeed")
        except Exception as error:
            self.showError.setStyleSheet("color : #d61340 ;")
            print(error)
            self.showError.setText(str(error))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form

    # Run the main Qt loop
    sys.exit(app.exec_())
