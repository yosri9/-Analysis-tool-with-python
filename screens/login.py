# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Login(object):
    def setupUi(self,):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1701, 1037)
        Login.setMinimumSize(QSize(700, 111))
        icon = QIcon()
        icon.addFile(u":/fis_stacked_tagline_green_rgb.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"")
        self.centralWidget = QWidget(Login)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"#centralWidget\n"
                                         "{\n"
                                         "\n"
                                         "border-radius:60px;\n"
                                         "	\n"
                                         "	\n"
                                         "background-color: rgb(65, 197, 96);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.gridLayout_5 = QGridLayout(self.centralWidget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.centralWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(450, 16777215))
        self.frame.setStyleSheet(u"*{\n"
                                 "font-family:arial;\n"
                                 "\n"
                                 "font-size:24px;\n"
                                 "}\n"
                                 "QFrame\n"
                                 "{\n"
                                 "background:#333;\n"
                                 "border-radius:4px;\n"
                                 "\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"*{\n"
                                      "font-family:century gothic;\n"
                                      "font-size:24px;\n"
                                      "}\n"
                                      "QFrame\n"
                                      "{\n"
                                      "background:#333;\n"
                                      "}\n"
                                      "QPushButton\n"
                                      "{\n"
                                      "background:red;\n"
                                      "border-radius:60px;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton\n"
                                      "{\n"
                                      "background:white;\n"
                                      "border-radius:7px;\n"
                                      "}\n"
                                      "")
        icon1 = QIcon()
        icon1.addFile(u":/images.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(64, 64))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.toolButton, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
                                 "QLabel\n"
                                 "{\n"
                                 "background:rgb(65, 197, 96);\n"
                                 "\n"
                                 "color:white;\n"
                                 "border-bottom:1px solid #717072;\n"
                                 "\n"
                                 "border-radius: 2px;\n"
                                 "\n"
                                 " border: 2px solid black;\n"
                                 " min-width: 80px;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"arial")
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.userLabel = QLabel(self.frame)
        self.userLabel.setObjectName(u"userLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy2)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet(u"QLabel\n"
                                     "{\n"
                                     "background-color: rgb(65, 197, 96);\n"
                                     "color: WHITE;\n"
                                     "border-bottom:1px solid #717072;\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "border-radius: 2px;\n"
                                     "\n"
                                     " border: 2px solid black;\n"
                                     " min-width: 80px;\n"
                                     "}")
        self.userLabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.userLabel)

        self.userEdit = QLineEdit(self.frame)
        self.userEdit.setObjectName(u"userEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.userEdit.sizePolicy().hasHeightForWidth())
        self.userEdit.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.userEdit.setFont(font2)
        self.userEdit.setStyleSheet(u"QLineEdit\n"
                                    "{\n"
                                    "background:white;\n"
                                    "\n"
                                    "color:black;\n"
                                    "border-bottom:1px solid #717072;\n"
                                    "border-radius:2px;\n"
                                    " border: 2px solid black;\n"
                                    " min-width: 80px;\n"
                                    "	font: 14pt \"Times New Roman\";\n"
                                    "}\n"
                                    "")
        self.userEdit.setMaxLength(64)

        self.horizontalLayout.addWidget(self.userEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passLabel = QLabel(self.frame)
        self.passLabel.setObjectName(u"passLabel")
        sizePolicy2.setHeightForWidth(self.passLabel.sizePolicy().hasHeightForWidth())
        self.passLabel.setSizePolicy(sizePolicy2)
        self.passLabel.setFont(font)
        self.passLabel.setStyleSheet(u"QLabel\n"
                                     "{\n"
                                     "\n"
                                     "background-color: rgb(65, 197, 96);\n"
                                     "\n"
                                     "\n"
                                     "color:white;\n"
                                     "border-bottom:1px solid #717072;\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "border-radius: 2px;\n"
                                     "\n"
                                     " border: 2px solid black;\n"
                                     " min-width: 80px;\n"
                                     "}")

        self.horizontalLayout_2.addWidget(self.passLabel)

        self.passEdit = QLineEdit(self.frame)
        self.passEdit.setObjectName(u"passEdit")
        sizePolicy3.setHeightForWidth(self.passEdit.sizePolicy().hasHeightForWidth())
        self.passEdit.setSizePolicy(sizePolicy3)
        self.passEdit.setStyleSheet(u"QLineEdit\n"
                                    "{\n"
                                    "background:white;\n"
                                    "\n"
                                    "color:black;\n"
                                    "border-bottom:1px solid #717072;\n"
                                    "border-radius:2px;\n"
                                    " border: 2px solid black;\n"
                                    " min-width: 80px;\n"
                                    "font: 14pt \"Times New Roman\";\n"
                                    "}\n"
                                    "")
        self.passEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.passEdit)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"QCheckBox\n"
                                    "{\n"
                                    "color:white;\n"
                                    "font-family:century gothic;\n"
                                    "font-size:24px;\n"
                                    " \n"
                                    "	font: 18pt \"Arial\";\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.checkBox.setTristate(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy1.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy1)
        self.loginButton.setFont(font1)
        self.loginButton.setStyleSheet(u"QPushButton {\n"
                                       "    border: 2px solid #8f8f91;\n"
                                       "    border-radius: 4px;\n"
                                       "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                       "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                       "    min-width: 80px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                       "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:flat {\n"
                                       "    border: none; /* no border for a flat push button */\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:default {\n"
                                       "    border-color: navy; /* make the default button prominent */\n"
                                       "}\n"
                                       "QPushButton:hover\n"
                                       "{\n"
                                       "color:white;\n"
                                       "border-radius: 4px;\n"
                                       "background:rgb(0, 0, 0);\n"
                                       "/* border: 2px solid #00007f;*/\n"
                                       " min-width: 80px;\n"
                                       "}")

        self.verticalLayout.addWidget(self.loginButton)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "    border: 2px solid #8f8f91;\n"
                                        "    border-radius: 4px;\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                        "    min-width: 80px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:flat {\n"
                                        "    border: none; /* no border for a flat push button */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:default {\n"
                                        "    border-color: navy; /* make the default button prominent */\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "color:white;\n"
                                        "border-radius: 4px;\n"
                                        "background:rgb(0, 0, 0);\n"
                                        "/* border: 2px solid #00007f;*/\n"
                                        " min-width: 80px;\n"
                                        "}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.centralWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setMinimumSize(QSize(0, 111))
        self.label_4.setPixmap(QPixmap(u":/111.jpg"))
        self.label_4.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        Login.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(Login)
        self.statusBar.setObjectName(u"statusBar")
        Login.setStatusBar(self.statusBar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.toolButton.setText("")
        self.label.setText(QCoreApplication.translate("Login", u" LOGIN HERE", None))
        self.label_2.setText(QCoreApplication.translate("Login",
                                                        u"<html><head/><body><p><span style=\" font-size:10pt; color:#55ffff;\">Please enter all of the required informations and click on the &quot;Login&quot; button</span></p></body></html>",
                                                        None))
        self.userLabel.setText(QCoreApplication.translate("Login", u"Username", None))
        # if QT_CONFIG(tooltip)
        self.userEdit.setToolTip(QCoreApplication.translate("Login",
                                                            u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter your username or id here</span></p></body></html>",
                                                            None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.userEdit.setWhatsThis(
            QCoreApplication.translate("Login", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.passLabel.setText(QCoreApplication.translate("Login", u"Password ", None))
        # if QT_CONFIG(tooltip)
        self.passEdit.setToolTip(QCoreApplication.translate("Login",
                                                            u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter your password here</span></p></body></html>",
                                                            None))
        # endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Login", u"Show password", None))
        self.loginButton.setText(QCoreApplication.translate("Login", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Register", None))
        self.label_4.setText("")

    # retranslateUi
