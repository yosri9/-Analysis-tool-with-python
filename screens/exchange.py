# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boursewindoww.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt5.uic.properties import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from api import ApiUtilities
from databases import Database
from databases.models import Exchange
from screens.add_new_exchange import  ui_add_exchange
from screens.analyse import Ui_analyze


class Ui_boursewindoww(object):

    def setupUi(self, boursewindoww):
        if not boursewindoww.objectName():
            boursewindoww.setObjectName(u"boursewindoww")
        boursewindoww.resize(1266, 762)
        icon = QIcon()
        icon.addFile(u"images/stock.png", QSize(), QIcon.Normal, QIcon.Off)
        boursewindoww.setWindowIcon(icon)
        boursewindoww.setStyleSheet(u"background-color:rgb(161, 161, 161)")
        self.centralwidget = QWidget(boursewindoww)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet("background: grey; \n"
                                         u"QWidget\n"
                                         "{\n"
                                         "qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
                                         "background:grey;\n"
                                         "}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(321, 500))
        self.frame.setStyleSheet(u"background: black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 321, 631))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(150, 150))
        self.label_5.setPixmap(QPixmap(u"images/exchangee.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Select = QPushButton(self.layoutWidget)
        self.Select.setObjectName(u"Select")
        self.Select.setMinimumSize(QSize(80, 40))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Select.setFont(font)
        self.Select.setStyleSheet(u"QPushButton {\n"
                                  "    \n"
                                  "color:white;\n"
                                  "border-radius: 2px;\n"
                                  "background:rgb(0, 0, 0);\n"
                                  "/* border: 2px solid #00007f;*/\n"
                                  "text-align:left;\n"
                                  " min-width: 80px;\n"
                                  "\n"
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
                                  "border: 2px solid rgb(66, 199, 0);\n"
                                  "    border-radius: 2px;\n"
                                  "    background-color:  black;\n"
                                  "    min-width: 80px;\n"
                                  "}")
        icon1 = QIcon()
        icon1.addFile(u"images/196-1966434_your-effectiveness-as-an-executive-is-inextricably-growth.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.Select.setIcon(icon1)
        self.Select.setIconSize(QSize(32, 32))
        self.Select.clicked.connect(self.goToAnalysisWindow)

        self.verticalLayout_3.addWidget(self.Select)
        iconAddNew = QIcon()
        iconAddNew.addFile(u"images/NNNB.png", QSize(),
                           QIcon.Normal, QIcon.Off)

        self.ADD_new = QPushButton(self.layoutWidget)
        self.ADD_new.clicked.connect(self.addExchangeItem)
        # ui_add_exchange().addButton.clicked.connect( print("hello"))
        # item = QListWidgetItem(exchange[1])
        # self.listbourse.addItem(item)

        self.ADD_new.setObjectName(u"ADD_new")
        self.ADD_new.setMinimumSize(QSize(80, 40))
        self.ADD_new.setFont(font)
        self.ADD_new.setIcon(iconAddNew)
        self.ADD_new.setStyleSheet(u"QPushButton {\n"
                                   "    \n"
                                   "color:white;\n"
                                   "border-radius: 2px;\n"
                                   "background:rgb(0, 0, 0);\n"
                                   "/* border: 2px solid #00007f;*/\n"
                                   " min-width: 80px;\n"
                                   "text-align:left;\n"
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
                                   "border: 2px solid rgb(66, 199, 0);\n"
                                   "    border-radius: 2px;\n"
                                   "    background-color:  black;\n"
                                   "    min-width: 80px;\n"
                                   "}")
        icon2 = QIcon()
        icon2.addFile(
            u"images/NNNB.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ADD_new.setIcon(icon2)
        self.ADD_new.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.ADD_new)

        self.Remove = QPushButton(self.layoutWidget)
        self.Remove.setObjectName(u"Remove")
        self.Remove.setMinimumSize(QSize(80, 40))
        self.Remove.setFont(font)
        self.Remove.setStyleSheet(u"QPushButton {\n"
                                  "    \n"
                                  "color:white;\n"
                                  "border-radius: 2px;\n"
                                  "background:rgb(0, 0, 0);\n"
                                  "/* border: 2px solid #00007f;*/\n"
                                  "text-align:left;\n"
                                  " min-width: 80px;\n"
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
                                  "border: 2px solid rgb(66, 199, 0);\n"
                                  "    border-radius: 2px;\n"
                                  "    background-color:  black;\n"
                                  "    min-width: 80px;\n"
                                  "}")
        icon3 = QIcon()
        icon3.addFile(u"images/REMOVVV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Remove.setIcon(icon3)
        self.Remove.setIconSize(QSize(32, 32))

        self.Remove.clicked.connect(self.deleteExchangeItem)
        self.verticalLayout_3.addWidget(self.Remove)

        self.About = QPushButton(self.layoutWidget)
        self.About.setObjectName(u"About")
        self.About.setMinimumSize(QSize(80, 40))
        self.About.setFont(font)
        self.About.setStyleSheet(u"QPushButton {\n"
                                 "    \n"
                                 "color:white;\n"
                                 "border-radius: 2px;\n"
                                 "background:rgb(0, 0, 0);\n"
                                 "/* border: 2px solid #00007f;*/\n"
                                 "text-align:left;\n"
                                 " min-width: 80px;\n"
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
                                 "border: 2px solid rgb(66, 199, 0);\n"
                                 "    border-radius: 2px;\n"
                                 "    background-color:  black;\n"
                                 "    min-width: 80px;\n"
                                 "}")
        icon4 = QIcon()
        icon4.addFile(u"images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About.setIcon(icon4)
        self.About.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.About)

        self.QUIT = QPushButton(self.layoutWidget)
        self.QUIT.setObjectName(u"QUIT")
        self.QUIT.setMinimumSize(QSize(84, 40))
        self.QUIT.setFont(font)
        self.QUIT.setStyleSheet(u"QPushButton {\n"
                                "  border: 2px solid black;\n"
                                "    border-radius: 2px;\n"
                                "/*    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);*/\n"
                                "background-color: black;\n"
                                "    min-width: 80px;\n"
                                "text-align:left;\n"
                                "color:white;\n"
                                "  \n"
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
                                "{color:white;\n"
                                "border-radius: 2px;\n"
                                "background:black;\n"
                                " border: 2px solid rgb(98, 0, 0);\n"
                                " min-width: 80px;\n"
                                "\n"
                                "}")
        icon5 = QIcon()
        icon5.addFile(u"images/turn_off_on_power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QUIT.setIcon(icon5)
        self.QUIT.setIconSize(QSize(32, 32))
        self.QUIT.setCheckable(False)
        self.QUIT.setAutoRepeat(False)
        self.QUIT.setAutoDefault(False)
        self.QUIT.setFlat(False)
        self.verticalLayout_3.addWidget(self.QUIT)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(100, 50))
        self.frame_2.setMaximumSize(QSize(10000, 10000))
        self.frame_2.setStyleSheet(u"background-color: black;\n"
                                   "border:black;\n"
                                   "color:white;\n"
                                   "border-bottom:1px solid #717072;\n"
                                   "border-radius:3px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setMaximumSize(QSize(80, 80))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_6.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "background:black;\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "\n"
                                   "\n"
                                   "}\n"
                                   "")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setLineWidth(0)
        self.label_6.setPixmap(QPixmap(u"images/stock.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(500, 50))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_4.setPalette(palette1)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: back;\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "border-bottom:0px solid #717072;\n"
                                   "border-radius:0px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_text = QLineEdit(self.centralwidget)
        self.search_text.setObjectName(u"search_text")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.search_text.setFont(font3)
        self.search_text.setStyleSheet(u"/*QLineEdit\n"
                                       "{\n"
                                       "background:white;\n"
                                       "border:none;\n"
                                       "color:black;\n"
                                       "border-bottom:1px solid #717072;\n"
                                       "border-radius:20px;\n"
                                       " border: 1px solid red;\n"
                                       "}*/\n"
                                       "\n"
                                       "/*\n"
                                       "QLineEdit { color: red }\n"
                                       "QLineEdit[readOnly=\"true\"] { color: gray }\n"
                                       "QDialog QLineEdit { color: brown }\n"
                                       "*/\n"
                                       "QLineEdit {\n"
                                       "    border: 2px solid gray;\n"
                                       "    border-radius: 4px;\n"
                                       "    padding: 0 8px;\n"
                                       "    background: white;\n"
                                       "    selection-background-color: darkgray;\n"
                                       "	font: 75 12pt \"Arial\";\n"
                                       "}")
        self.search_text.textChanged.connect(self.showWantedItem)

        self.horizontalLayout.addWidget(self.search_text)

        self.find = QToolButton(self.centralwidget)
        self.find.setObjectName(u"find")
        self.find.setFont(font)
        self.find.setStyleSheet(u"QPushButton {\n"
                                "    border: 2px solid #8f8f91;\n"
                                "    border-radius: 2px;\n"
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
                                "border-radius: 2px;\n"
                                "background:rgb(0, 0, 0);\n"
                                " border: 2px solid GREEN;\n"
                                " min-width: 80px;\n"
                                "}")

        self.horizontalLayout.addWidget(self.find)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.listbourse = QListWidget(self.centralwidget)
        self.listbourse.setObjectName(u"listbourse")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listbourse.sizePolicy().hasHeightForWidth())
        self.listbourse.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Arial Black")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.listbourse.setFont(font4)
        self.listbourse.setStyleSheet(u"/*.Listwidget::item {\n"
                                      "    background-color: #fff;\n"
                                      "}\n"
                                      "\n"
                                      ".lstSnapQuote::item:selected {\n"
                                      "    background-color: #5555FF;\n"
                                      "}*/\n"
                                      "/*\n"
                                      "QListView::item:selected { background: palette(Highlight) }\n"
                                      "\n"
                                      "QListWidget::item[text=\"ghjgjh\"] {\n"
                                      "    color: red;\n"
                                      "    background: white;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "*/\n"
                                      "QListView {\n"
                                      "    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:alternate {\n"
                                      "    background:  rgb(255, 170, 255) ;\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item\n"
                                      "{\n"
                                      "background:rgb(0, 0, 0);\n"
                                      "COLOR: white;\n"
                                      "}\n"
                                      "QListView::item:selected {\n"
                                      "    border: 1px solid #6a6ea9;\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:selected:!active {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:selected:active {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                            "
                                      "    stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:hover {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
                                      "color:black;\n"
                                      "}\n"
                                      "")
        self.listbourse.setResizeMode(QListView.Adjust)
        self.listbourse.setViewMode(QListView.ListMode)
        self.listbourse.setUniformItemSizes(False)
        self.listbourse.setWordWrap(False)
        self.listbourse.setSelectionRectVisible(False)
        self.listbourse.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.listbourse)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.number = QLabel(self.centralwidget)
        self.number.setObjectName(u"number")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(246, 247, 250, 255))
        gradient.setColorAt(1, QColor(218, 219, 222, 255))
        brush2 = QBrush(gradient)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 0, 217, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(246, 247, 250, 255))
        gradient1.setColorAt(1, QColor(218, 219, 222, 255))
        brush4 = QBrush(gradient1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(246, 247, 250, 255))
        gradient2.setColorAt(1, QColor(218, 219, 222, 255))
        brush5 = QBrush(gradient2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(246, 247, 250, 255))
        gradient3.setColorAt(1, QColor(218, 219, 222, 255))
        brush6 = QBrush(gradient3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(246, 247, 250, 255))
        gradient4.setColorAt(1, QColor(218, 219, 222, 255))
        brush7 = QBrush(gradient4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(246, 247, 250, 255))
        gradient5.setColorAt(1, QColor(218, 219, 222, 255))
        brush8 = QBrush(gradient5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush9 = QBrush(QColor(120, 120, 120, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(246, 247, 250, 255))
        gradient6.setColorAt(1, QColor(218, 219, 222, 255))
        brush10 = QBrush(gradient6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(246, 247, 250, 255))
        gradient7.setColorAt(1, QColor(218, 219, 222, 255))
        brush11 = QBrush(gradient7)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(246, 247, 250, 255))
        gradient8.setColorAt(1, QColor(218, 219, 222, 255))
        brush12 = QBrush(gradient8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.number.setPalette(palette2)
        self.number.setFont(font)
        self.number.setStyleSheet(u"QLabel\n"
                                  " {\n"
                                  "    border: 2px solid #8f8f91;\n"
                                  "    border-radius: 6px;\n"
                                  "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                  "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                  "    min-width: 80px;\n"
                                  "    \n"
                                  "}")

        self.horizontalLayout_2.addWidget(self.number)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        palette3 = QPalette()
        gradient9 = QLinearGradient(0, 0, 0, 1)
        gradient9.setSpread(QGradient.PadSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(246, 247, 250, 255))
        gradient9.setColorAt(1, QColor(218, 219, 222, 255))
        brush13 = QBrush(gradient9)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush13)
        gradient10 = QLinearGradient(0, 0, 0, 1)
        gradient10.setSpread(QGradient.PadSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(246, 247, 250, 255))
        gradient10.setColorAt(1, QColor(218, 219, 222, 255))
        brush14 = QBrush(gradient10)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush14)
        gradient11 = QLinearGradient(0, 0, 0, 1)
        gradient11.setSpread(QGradient.PadSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(246, 247, 250, 255))
        gradient11.setColorAt(1, QColor(218, 219, 222, 255))
        brush15 = QBrush(gradient11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush15)
        gradient12 = QLinearGradient(0, 0, 0, 1)
        gradient12.setSpread(QGradient.PadSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(246, 247, 250, 255))
        gradient12.setColorAt(1, QColor(218, 219, 222, 255))
        brush16 = QBrush(gradient12)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        gradient13 = QLinearGradient(0, 0, 0, 1)
        gradient13.setSpread(QGradient.PadSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(246, 247, 250, 255))
        gradient13.setColorAt(1, QColor(218, 219, 222, 255))
        brush17 = QBrush(gradient13)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        gradient14 = QLinearGradient(0, 0, 0, 1)
        gradient14.setSpread(QGradient.PadSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(246, 247, 250, 255))
        gradient14.setColorAt(1, QColor(218, 219, 222, 255))
        brush18 = QBrush(gradient14)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush18)
        gradient15 = QLinearGradient(0, 0, 0, 1)
        gradient15.setSpread(QGradient.PadSpread)
        gradient15.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(246, 247, 250, 255))
        gradient15.setColorAt(1, QColor(218, 219, 222, 255))
        brush19 = QBrush(gradient15)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        gradient16 = QLinearGradient(0, 0, 0, 1)
        gradient16.setSpread(QGradient.PadSpread)
        gradient16.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(246, 247, 250, 255))
        gradient16.setColorAt(1, QColor(218, 219, 222, 255))
        brush20 = QBrush(gradient16)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        gradient17 = QLinearGradient(0, 0, 0, 1)
        gradient17.setSpread(QGradient.PadSpread)
        gradient17.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(246, 247, 250, 255))
        gradient17.setColorAt(1, QColor(218, 219, 222, 255))
        brush21 = QBrush(gradient17)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        self.label_3.setPalette(palette3)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "    border: 2px solid #8f8f91;\n"
                                   "    border-radius: 6px;\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                   "    min-width: 80px;\n"
                                   "}")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        boursewindoww.setCentralWidget(self.centralwidget)

        self.retranslateUi(boursewindoww)

        self.QUIT.setDefault(False)

        QMetaObject.connectSlotsByName(boursewindoww)

    # setupUi

    def retranslateUi(self, boursewindoww):
        boursewindoww.setWindowTitle(QCoreApplication.translate("boursewindoww", u"MainWindow", None))
        self.label_5.setText("")
        # if QT_CONFIG(tooltip)
        self.Select.setToolTip(QCoreApplication.translate("boursewindoww",
                                                          u"<html><head/><body><p><span style=\" font-size:9pt; color:#3c3c5a;\">Select a stock exchange and then clic here to display Analyze window</span></p></body></html>",
                                                          None))
        # endif // QT_CONFIG(tooltip)
        self.Select.setText(QCoreApplication.translate("boursewindoww", u"       Select", None))
        # if QT_CONFIG(tooltip)
        self.ADD_new.setToolTip(QCoreApplication.translate("boursewindoww",
                                                           u"<html><head/><body><p><span style=\" font-size:9pt; color:#3c3c5a;\">Clic here if you want to add a new stock exchange</span></p></body></html>",
                                                           None))
        # endif // QT_CONFIG(tooltip)
        self.ADD_new.setText(QCoreApplication.translate("boursewindoww", u"       Add New / Save", None))
        # if QT_CONFIG(tooltip)
        self.Remove.setToolTip(QCoreApplication.translate("boursewindoww",
                                                          u"<html><head/><body><p><span style=\" font-size:9pt; color:#3c3c5a;\">select a stock exchange from a list and clic here to delete it</span></p></body></html>",
                                                          None))
        # endif // QT_CONFIG(tooltip)
        self.Remove.setText(QCoreApplication.translate("boursewindoww", u"      Remove", None))
        # if QT_CONFIG(tooltip)
        self.About.setToolTip(QCoreApplication.translate("boursewindoww",
                                                         u"<html><head/><body><p><span style=\" font-family:'Helvetica Neue,Helvetica,Arial,sans-serif'; font-size:9pt; color:#3c3c5a; background-color:#ffffff;\">Click\u00a0here\u00a0to\u00a0view more\u00a0informations\u00a0about\u00a0the\u00a0list\u00a0of\u00a0stock exchanges</span></p></body></html>",
                                                         None))
        # endif // QT_CONFIG(tooltip)
        self.About.setText(QCoreApplication.translate("boursewindoww", u"      About ", None))
        self.QUIT.setText(QCoreApplication.translate("boursewindoww", u"      Quit", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("boursewindoww", u" STOCK EXCHANGES LIST", None))
        self.find.setText(QCoreApplication.translate("boursewindoww", u"Find", None))
        self.number.setText(QCoreApplication.translate("boursewindoww", u"Number of items", None))
        self.label_3.setText(QCoreApplication.translate("boursewindoww", u"0", None))

    # retranslateUi
        Database.analysisToolDatabase()

        self.IDNameMap = {}
        i = 0
        for exchange in Database.getAll(Exchange):
            i += 1
            self.IDNameMap[exchange[0]] = exchange[1]
            item = QListWidgetItem(exchange[1])
            self.listbourse.addItem(item)
            self.label_3.setText(str(i))

    @Slot()
    def addExchangeItem(self):
            oldData = Database.getAll(Exchange)
            oldTableLength = len(oldData)
            ui = ui_add_exchange()
            ui.show()
            ui.exec_()
            newData = Database.getAll(Exchange)
            newTableLength = len(newData)
            if( oldTableLength != newTableLength):
                item = QListWidgetItem(newData[-1][1])
                self.listbourse.addItem(item)
                self.IDNameMap[newData[-1][0]] = newData[-1][1]
            self.label_3.setText(str(self.listbourse.count()))

    @Slot()
    def deleteExchangeItem(self):
           item =  self.listbourse.currentItem()
           itemName = ""
           if item is not None:
                itemName = item.text()

           for id , name in self.IDNameMap.items():
                if itemName == name:
                        self.IDNameMap.pop(id)
                        Database.delete(Exchange(id))
                        self.listbourse.currentItem().setHidden(True)
                        print(self.IDNameMap)
           self.label_3.setText(str(self.listbourse.count()))

    @Slot()
    def goToAnalysisWindow(self):
        selectedItem = self.listbourse.currentItem()
        selectedItemData = None

        for id , name in self.IDNameMap.items():
            print(self.IDNameMap)
            if( name == str(selectedItem.text() )):
                selectedItemID = id
                ApiUtilities.EXCHANGE_ID = id



        window = QMainWindow()
        ui = Ui_analyze()
        ui.setupUi(window)



        allData = Database.getAll(Exchange)
        # if row id in database  == selectedItemID than selectedItemData = data of this row id
        for data in allData:
            if data[0] == selectedItemID:
                selectedItemData = data
        print(selectedItemData)
        ApiUtilities.MAIN_API_URL = selectedItemData[2]
        print(ApiUtilities.MAIN_API_URL)
        ApiUtilities.USERNAME = selectedItemData[3]
        print( ApiUtilities.USERNAME)
        ApiUtilities.PASSWORD = selectedItemData[4]
        print( ApiUtilities.PASSWORD )

        window.show()
        window.setAutoFillBackground()

    @Slot()
    def showWantedItem(self):
        self.listbourse.clear()
        exchange = Exchange(exchangeName=self.search_text.text())
        print(self.search_text.text())
        items = Database.findExchangeItem(exchange)
        print(items)
        for item in items:
            exchangeToShow = QListWidgetItem(item[1])
            print(item)
            self.listbourse.addItem(exchangeToShow)
        self.label_3.setText(str(self.listbourse.count()))




