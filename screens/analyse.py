# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyze.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.uic.properties import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import SIGNAL, QObject

import images
from api import ApiUtilities
from api.Bug import FetchBugs, bugFile

from databases import Database
from databases.models import Bug, Exchange
from databases.models.bug_exchanges import BugExchange


class Ui_analyze(object):

    def setupUi(self, analyze):
        if not analyze.objectName():
            analyze.setObjectName(u"analyze")
        analyze.resize(1328, 1135)
        icon = QIcon()
        icon.addFile("images/file_log_.jpg", QSize(), QIcon.Normal, QIcon.Off)
        analyze.setWindowIcon(icon)
        analyze.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(analyze)
        self.centralwidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1493, 16777215))
        self.centralwidget.setStyleSheet(u"background: black;")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(334, 16777215))
        self.frame.setStyleSheet(u"background-color:BLACK;\n"
                                 "border: 2px solid #8f8f91;\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-9, -3, 341, 191))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(202, 0))
        self.label_4.setPixmap(QPixmap(u"images/software-test-automation-tool.jpg"))
        self.label_4.setScaledContents(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 187, 261, 64))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"\n"
                                   "QLabel\n"
                                   "{\n"
                                   "    background-color: white;\n"
                                   "color:black;\n"
                                   "border-bottom:1px solid #717072;\n"
                                   "border-radius:2px;\n"
                                   "border:none;\n"
                                   " min-width: 40px;\n"
                                   "}\n"
                                   "")
        self.label_6.setScaledContents(False)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 187, 80, 64))
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(70, 80))
        self.label_5.setStyleSheet(u"\n"
                                   "QLabel\n"
                                   "{\n"
                                   "    background-color: white;\n"
                                   "color:black;\n"
                                   "border-bottom:1px solid #717072;\n"
                                   "border-radius:2px;\n"
                                   "border:none;\n"
                                   " min-width: 80px;\n"
                                   "}\n"
                                   "")
        self.label_5.setPixmap(QPixmap(u"images/log_file.png"))
        self.label_5.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 260, 331, 38))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.select_folder = QPushButton(self.layoutWidget)
        self.select_folder.setObjectName(u"select_folder")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.select_folder.setFont(font1)
        self.select_folder.setStyleSheet(u"QPushButton {\n"
                                         "    \n"
                                         "color:white;\n"
                                         "border-radius: 2px;\n"
                                         "background:rgb(0, 0, 0);\n"
                                         "/* border: 2px solid #00007f;*/\n"
                                         " min-width: 40px;\n"
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
                                         "    min-width: 40px;\n"
                                         "}")
        icon1 = QIcon()
        icon1.addFile(u"images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_folder.setIcon(icon1)
        self.select_folder.setIconSize(QSize(16, 16))
        self.folder_path = ""
        self.select_folder.clicked.connect(self.getDirectory)
        self.select_folder.clicked.connect(self.getDirectoryPath)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.select_folder)

        self.folder_path_label = QLabel(self.layoutWidget)
        self.folder_path_label.setObjectName(u"folder_path_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.folder_path_label.sizePolicy().hasHeightForWidth())
        self.folder_path_label.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.folder_path_label.setFont(font2)
        self.folder_path_label.setStyleSheet(u"\n"
                                             "QLabel\n"
                                             "{\n"
                                             "    background-color: white;\n"
                                             "color:black;\n"
                                             "border-bottom:1px solid #717072;\n"
                                             "border-radius:1px;\n"
                                             "border:none;\n"
                                             " min-width: 40px;\n"
                                             "}\n"
                                             "")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.folder_path_label)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 297, 331, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # server path
        self.log_file_path_label = QLabel(self.layoutWidget1)
        self.log_file_path_label.setObjectName(u"log_file_path_label")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.log_file_path_label.setFont(font3)
        self.log_file_path_label.setStyleSheet(u"QLabel {\n"
                                               "   \n"
                                               "\n"
                                               "color:white;\n"
                                               "border-radius: 1px;\n"
                                               "background:rgb(0, 0, 0);\n"
                                               "/* border: 2px solid #00007f;*/\n"
                                               " min-width: 40px;\n"
                                               "\n"
                                               "}")

        self.horizontalLayout.addWidget(self.log_file_path_label)

        self.log_file_path_editLine = QLineEdit(self.layoutWidget1)
        self.log_file_path_editLine.setObjectName(u"log_file_path_editLine")
        self.log_file_path_editLine.setFont(font3)
        self.log_file_path_editLine.setStyleSheet(u"QLineEdit {\n"
                                                  "    border: 1px solid white;\n"
                                                  "    border-radius: 1px;\n"
                                                  "    background-color: white;\n"
                                                  "    min-width: 40px;\n"
                                                  "	color: black;\n"
                                                  "}")

        self.horizontalLayout.addWidget(self.log_file_path_editLine)

        self.submit_folder_and_file = QPushButton(self.frame)
        self.submit_folder_and_file.setObjectName(u"submit_folder_and_file")
        submitFont = QFont()
        submitFont.setPointSize(20)
        submitFont.setBold(True)
        submitFont.setLetterSpacing(QFont.PercentageSpacing, 150)
        submitFont.setWeight(75)
        self.submit_folder_and_file.setFont(submitFont)
        self.submit_folder_and_file.setText("SUBMIT")
        self.submit_folder_and_file.setStyleSheet(
            u"QPushButton {\n"
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
            "background:green;\n"
            " border: 2px solid GREEN;\n"
            " min-width: 80px;\n"
            "}")

        self.submit_folder_and_file.setGeometry(QRect(7, 450, 320, 30))
        self.submit_folder_and_file.clicked.connect(self.submit)

        self.horizontalLayout_2 = QHBoxLayout(self.submit_folder_and_file)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        # end of  column 1

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.tabWidget.setFont(font4)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet(u"\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "QTabWidget::pane { /* The tab widget frame */\n"
                                     "    border-top: 2px solid #C2C7CB;\n"
                                     "    position: absolute;\n"
                                     "    top: -0.5em;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget::tab-bar {\n"
                                     "    alignment: center;\n"
                                     "}\n"
                                     "\n"
                                     "/* Style the tab using the tab sub-control. Note that\n"
                                     "    it reads QTabBar _not_ QTabWidget */\n"
                                     "QTabBar::tab {\n"
                                     "    background: WHITE; \n"
                                     "/*qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                     "                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3)\n"
                                     "*/\n"
                                     "    border: 2px solid #C4C4C3;\n"
                                     "    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
                                     "    border-top-left-radius: 3px;\n"
                                     "    border-top-right-radius: 3px;\n"
                                     "    min-width: 8ex;\n"
                                     "    padding: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                                     "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
                                     "                "
                                     "                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    border-color: #9B9B9B;\n"
                                     "    border-bottom-color: #C2C7CB; /* same as pane color */\n"
                                     "}")
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.showUnwantedBug)


        self.warning_tab = QPushButton()
        self.warning_tab.setObjectName(u"warning_tab")
        self.gridLayout = QGridLayout(self.warning_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.warning_page = QTreeWidget(self.warning_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"number of occurrences");
        self.warning_page.setHeaderItem(__qtreewidgetitem)
        self.warning_page.setObjectName(u"warning_page")
        self.warning_page.setEnabled(True)
        sizePolicy.setHeightForWidth(self.warning_page.sizePolicy().hasHeightForWidth())
        self.warning_page.setSizePolicy(sizePolicy)
        self.warning_page.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily(u"Monospace")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.warning_page.setFont(font5)
        self.warning_page.setStyleSheet(u"QTreeView {\n"
                                        "	font: 10pt \"Monospace\";\n"
                                        "    show-decoration-selected: 1;\n"
                                        "border: 2px solid #8f8f91;\n"
                                        "	background-color: rgb(51, 51, 51);\n"
                                        "color:white;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::item {\n"
                                        "     border: 1px solid #d9d9d9;\n"
                                        "    border-top-color: transparent;\n"
                                        "    border-bottom-color: transparent;\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::item:hover {\n"
                                        "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                        "    border: 1px solid #bfcde4;\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::item:selected {\n"
                                        "    border: 1px solid #567dbc;\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::item:selected:active{\n"
                                        "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                        "}\n"
                                        "\n"
                                        "QTreeView::item:selected:!active {\n"
                                        "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                        "}")
        self.gridLayout.addWidget(self.warning_page, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u"images/Warning_icon..png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.warning_tab, icon2, "")
        self.fail_tab = QPushButton()
        self.fail_tab.setObjectName(u"fail_tab")
        self.gridLayout_12 = QGridLayout(self.fail_tab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.fail_page = QTreeWidget(self.fail_tab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"number of occurrences");
        self.fail_page.setHeaderItem(__qtreewidgetitem1)
        self.fail_page.setObjectName(u"fail_page")
        self.fail_page.setFont(font5)
        self.fail_page.setStyleSheet(u"QTreeView {\n"
                                     "	font: 10pt \"Monospace\";\n"
                                     "    show-decoration-selected: 1;\n"
                                     "   border: 2px solid #8f8f91;\n"
                                     "background-color: rgb(51, 51, 51);\n"
                                     "color:white;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTreeView::item {\n"
                                     "     border: 1px solid #d9d9d9;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-bottom-color: transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QTreeView::item:hover {\n"
                                     "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                     "    border: 1px solid #bfcde4;\n"
                                     "}\n"
                                     "\n"
                                     "QTreeView::item:selected {\n"
                                     "    border: 1px solid #567dbc;\n"
                                     "}\n"
                                     "\n"
                                     "QTreeView::item:selected:active{\n"
                                     "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                     "}\n"
                                     "\n"
                                     "QTreeView::item:selected:!active {\n"
                                     "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                     "}")
        self.gridLayout_12.addWidget(self.fail_page, 0, 0, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u"images/fail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.fail_tab, icon3, "")
        self.error_tab = QPushButton()
        self.error_tab.setObjectName(u"error_tab")
        self.gridLayout_error = QGridLayout(self.error_tab)
        self.gridLayout_error.setObjectName(u"gridLayout_error")
        self.error_page = QTreeWidget(self.error_tab)
        self.error_page.setObjectName(u"error_page")
        self.error_page.setFont(font5)
        self.error_page.setStyleSheet(u"QTreeView {\n"
                                      "	font: 10pt \"Monospace\";\n"
                                      "    show-decoration-selected: 1;\n"
                                      "border: 2px solid #8f8f91;\n"
                                      "background-color: rgb(51, 51, 51);\n"
                                      "color:white;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item {\n"
                                      "     border: 1px solid #d9d9d9;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:hover {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                      "    border: 1px solid #bfcde4;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected {\n"
                                      "    border: 1px solid #567dbc;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:active{\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:!active {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                      "}")



        self.gridLayout_error.addWidget(self.error_page, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u"images/error-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.error_tab, icon4, "")
        self.information_tab = QPushButton()
        self.information_tab.setObjectName(u"information_tab")
        self.gridLayout_information = QGridLayout(self.information_tab)
        self.gridLayout_information.setObjectName(u"gridLayout_information")
        self.information_page = QTreeWidget(self.information_tab)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"number of occurrences");
        self.information_page.setHeaderItem(__qtreewidgetitem2)
        self.information_page.setObjectName(u"information_page")
        self.information_page.setFont(font5)
        self.information_page.setStyleSheet(u"QTreeView {\n"
                                            "	font: 10pt \"Monospace\";\n"
                                            "    show-decoration-selected: 1;\n"
                                            "border: 2px solid #8f8f91;\n"
                                            "background-color: rgb(51, 51, 51);\n"
                                            "color:white;\n"
                                            "}\n"
                                            "\n"
                                            "QTreeView::item {\n"
                                            "     border: 1px solid #d9d9d9;\n"
                                            "    border-top-color: transparent;\n"
                                            "    border-bottom-color: transparent;\n"
                                            "}\n"
                                            "\n"
                                            "QTreeView::item:hover {\n"
                                            "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                            "    border: 1px solid #bfcde4;\n"
                                            "}\n"
                                            "\n"
                                            "QTreeView::item:selected {\n"
                                            "    border: 1px solid #567dbc;\n"
                                            "}\n"
                                            "\n"
                                            "QTreeView::item:selected:active{\n"
                                            "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                            "}\n"
                                            "\n"
                                            "QTreeView::item:selected:!active {\n"
                                            "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                            "}")
        self.gridLayout_information.addWidget(self.information_page, 0, 0, 1, 1)

        icon5 = QIcon()
        icon5.addFile(u"images/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.information_tab, icon5, "")
        self.debug_tab = QPushButton()
        self.debug_tab.setObjectName(u"debug_tab")
        self.gridLayout_debug = QGridLayout(self.debug_tab)
        self.gridLayout_debug.setObjectName(u"gridLayout_debug")
        self.debug_page = QTreeWidget(self.debug_tab)
        self.debug_page.setObjectName(u"debug_page")
        self.debug_page.setFont(font5)
        self.debug_page.setStyleSheet(u"QTreeView {\n"
                                      "	font: 10pt \"Monospace\";\n"
                                      "    show-decoration-selected: 1;\n"
                                      "border: 2px solid #8f8f91;\n"
                                      "background-color: rgb(51, 51, 51);\n"
                                      "color:white;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item {\n"
                                      "     border: 1px solid #d9d9d9;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:hover {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                      "    border: 1px solid #bfcde4;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected {\n"
                                      "    border: 1px solid #567dbc;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:active{\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:!active {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                      "}")
        self.gridLayout_debug.addWidget(self.debug_page, 0, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u"images/DEBUG.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.debug_tab, icon6, "")
        self.trace_tab = QPushButton()
        self.trace_tab.setObjectName(u"trace_tab")
        self.gridLayout_11 = QGridLayout(self.trace_tab)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.trace_page = QTreeWidget(self.trace_tab)
        self.trace_page.setObjectName(u"trace_page")
        self.trace_page.setFont(font5)
        self.trace_page.setStyleSheet(u"QTreeView {\n"
                                      "	font: 10pt \"Monospace\";\n"
                                      "    show-decoration-selected: 1;\n"
                                      "border: 2px solid #8f8f91;\n"
                                      "background-color: rgb(51, 51, 51);\n"
                                      "color:white;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item {\n"
                                      "     border: 1px solid #d9d9d9;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:hover {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                      "    border: 1px solid #bfcde4;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected {\n"
                                      "    border: 1px solid #567dbc;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:active{\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView::item:selected:!active {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                      "}")

        # print(line)

        #   TODO:call to function addBugItems after tabBar selection

        self.gridLayout_11.addWidget(self.trace_page, 0, 0, 1, 1)

        icon7 = QIcon()
        icon7.addFile(u"images/trace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.trace_tab, icon7, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ignoreButton = QPushButton(self.centralwidget)
        self.ignoreButton.setObjectName(u"ignoreButton")
        self.ignoreButton.setMinimumSize(QSize(0, 0))
        self.ignoreButton.setMaximumSize(QSize(100, 50))
        self.ignoreButton.setStyleSheet(u"QPushButton:hover\n"
                                        "{\n"
                                        "color:white;\n"
                                        "border-radius: 1px;\n"
                                        "background:rgb(216, 0, 0);\n"
                                        "/* border: 2px solid #00007f;*/\n"
                                        " min-width: 4px;\n"
                                        "}\n"
                                        "QPushButton\n"
                                        "{\n"
                                        "background:rgb(204, 204, 204);\n"
                                        "}")
        icon8 = QIcon()
        icon8.addFile(u"images/arrow_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ignoreButton.setIcon(icon8)
        self.ignoreButton.setIconSize(QSize(32, 32))

        self.ignoreButton.clicked.connect(self.addIgnoredItem)

        self.verticalLayout.addWidget(self.ignoreButton)

        self.ignoreLabel_2 = QLabel(self.centralwidget)
        self.ignoreLabel_2.setObjectName(u"ignoreLabel_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ignoreLabel_2.sizePolicy().hasHeightForWidth())
        self.ignoreLabel_2.setSizePolicy(sizePolicy5)
        self.ignoreLabel_2.setMaximumSize(QSize(100, 20))
        self.ignoreLabel_2.setFont(font4)
        self.ignoreLabel_2.setStyleSheet(u"color:white;")
        self.ignoreLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ignoreLabel_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.delete_error_rep = QPushButton(self.centralwidget)
        self.delete_error_rep.setObjectName(u"delete_error_rep")
        self.delete_error_rep.setStyleSheet(u"QPushButton:hover\n"
                                            "{\n"
                                            "color:white;\n"
                                            "border-radius: 1px;\n"
                                            "background:rgb(72, 145, 218);\n"
                                            "/* border: 2px solid #00007f;*/\n"
                                            " min-width: 4px;\n"
                                            "}\n"
                                            "QPushButton\n"
                                            "{\n"
                                            "background:rgb(204, 204, 204);\n"
                                            "}")
        icon9 = QIcon()
        icon9.addFile(u"images/memorize_pic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_error_rep.setIcon(icon9)
        self.delete_error_rep.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.delete_error_rep)

        self.memorize_label = QLabel(self.centralwidget)
        self.memorize_label.setObjectName(u"memorize_label")
        self.memorize_label.setFont(font4)
        self.memorize_label.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.memorize_label)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.memorize_allexchange = QPushButton(self.centralwidget)
        self.memorize_allexchange.setObjectName(u"memorize_allexchange")
        self.memorize_allexchange.setStyleSheet(u"QPushButton:hover\n"
                                                "{\n"
                                                "color:white;\n"
                                                "border-radius: 1px;\n"
                                                "background:rgb(72, 145, 218);\n"
                                                "/* border: 2px solid #00007f;*/\n"
                                                " min-width: 4px;\n"
                                                "}\n"
                                                "QPushButton\n"
                                                "{\n"
                                                "background:rgb(204, 204, 204);\n"
                                                "}")
        self.memorize_allexchange.setIcon(icon9)
        self.memorize_allexchange.setIconSize(QSize(32, 32))
        self.memorize_allexchange.clicked.connect(self.memorizeAllExchange)
        self.verticalLayout_5.addWidget(self.memorize_allexchange)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color:white;")

        self.verticalLayout_5.addWidget(self.label_7)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.restoreButton = QPushButton(self.centralwidget)
        self.restoreButton.setObjectName(u"restoreButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.restoreButton.sizePolicy().hasHeightForWidth())
        self.restoreButton.setSizePolicy(sizePolicy6)
        self.restoreButton.setMinimumSize(QSize(54, 0))
        self.restoreButton.setMaximumSize(QSize(100, 50))
        self.restoreButton.setStyleSheet(u"QPushButton:hover\n"
                                         "{\n"
                                         "color:white;\n"
                                         "border-radius: 1px;\n"
                                         "background:rgb(0, 203, 0);\n"
                                         "/* border: 2px solid #00007f;*/\n"
                                         " min-width: 4px;\n"
                                         "}\n"
                                         "QPushButton\n"
                                         "{\n"
                                         "background:rgb(204, 204, 204);\n"
                                         "}")
        icon10 = QIcon()
        icon10.addFile(u"images/arrow_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon10)
        self.restoreButton.setIconSize(QSize(32, 32))

        self.restoreButton.clicked.connect(self.restoreBug)
        self.verticalLayout_2.addWidget(self.restoreButton)

        self.restoreLabel = QLabel(self.centralwidget)
        self.restoreLabel.setObjectName(u"restoreLabel")
        sizePolicy5.setHeightForWidth(self.restoreLabel.sizePolicy().hasHeightForWidth())
        self.restoreLabel.setSizePolicy(sizePolicy5)
        self.restoreLabel.setMaximumSize(QSize(1000, 30))
        self.restoreLabel.setFont(font4)
        self.restoreLabel.setStyleSheet(u"color:white;")
        self.restoreLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.restoreLabel)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.label.setFont(font6)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
                                 "   \n"
                                 "\n"
                                 "color:white;\n"
                                 "border-radius: 1px;\n"
                                 "background:rgb(0, 0, 0);\n"
                                 "border: 2px solid rgb(85, 170, 255);\n"
                                 " min-width: 40px;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label)

        self.unwanted_log_info = QTreeWidget(self.centralwidget)
        font7 = QFont()
        font7.setPointSize(8)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setFont(2, font7);
        __qtreewidgetitem3.setText(0, u"number of occurrences")
        self.unwanted_log_info.setHeaderItem(__qtreewidgetitem3)
        self.unwanted_log_info.setObjectName(u"unwanted_log_info")
        self.unwanted_log_info.setStyleSheet(u"QTreeView {\n"
                                             "	font: 11pt \"Monospace\";\n"
                                             "    show-decoration-selected: 1;\n"
                                             "border: 2px solid #8f8f91;\n"
                                             "background-color: rgb(51, 51, 51);\n"
                                             "color:white;\n"
                                             "}\n"
                                             "\n"
                                             "QTreeView::item {\n"
                                             "     border: 1px solid #d9d9d9;\n"
                                             "    border-top-color: transparent;\n"
                                             "    border-bottom-color: transparent;\n"
                                             "}\n"
                                             "\n"
                                             "QTreeView::item:hover {\n"
                                             "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
                                             "    border: 1px solid #bfcde4;\n"
                                             "}\n"
                                             "\n"
                                             "QTreeView::item:selected {\n"
                                             "    border: 1px solid #567dbc;\n"
                                             "}\n"
                                             "\n"
                                             "QTreeView::item:selected:active{\n"
                                             "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                             "}\n"
                                             "\n"
                                             "QTreeView::item:selected:!active {\n"
                                             "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                             "}")

        # unwantedDataID = Database.getBugExchangeIDByExchangeID(BugExchange , ApiUtilities.EXCHANGE_ID)
        #
        # print(unwantedDataID)
        # print("unwantedDataID")
        # self.bugData=[]
        # self.bugExchangeID = []
        #
        # for data in unwantedDataID:
        #     bugExchangeElement = BugExchange(data[0] , data[1])
        #     self.bugExchangeID.append(bugExchangeElement)
        #     item=list(Database.getByID(Bug , bugExchangeElement.getBugID()))
        #     item.pop(0)
        #     self.bugData.append(item )
        #
        #     print(item)
        #
        #     item = QTreeWidgetItem(item)
        #     self.unwanted_log_info.addTopLevelItem(item)
        #
        #     print("--------------------------------------------------------")
        #


        self.verticalLayout_3.addWidget(self.unwanted_log_info)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy7)
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setStyleSheet(u"\n"
                                   "/* linear gradient from white to green */\n"
                                   "QFrame{\n"
                                   "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                   "                stop:0 white, stop: 0.4 gray, stop:1 rgb(206, 206, 206))\n"
                                   "}\n"
                                   "\n"
                                   "/* linear gradient from white to green */\n"
                                   "QFrame {\n"
                                   "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                   "                stop:0 white, stop: 0.4 rgba(10, 20, 30, 40),\n"
                                   "                stop:1 rgb(0, 200, 230, 200))\n"
                                   "}\n"
                                   "\n"
                                   "/* conical gradient from white to green */\n"
                                   "QFrame {\n"
                                   "    background: qconicalgradient(cx:0.5, cy:0.5, angle:30,\n"
                                   "                stop:0 white, stop:1 rgb(206, 206, 206))\n"
                                   "}\n"
                                   "\n"
                                   "/* radial gradient from white to green */\n"
                                   "QFrame {\n"
                                   "    background: qradialgradient(cx:0, cy:0, radius: 1,\n"
                                   "                fx:0.5, fy:0.5, stop:0 white, stop:1 rgb(206, 206, 206))\n"
                                   "}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.quit_button = QPushButton(self.frame_3)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setEnabled(True)
        self.quit_button.setMinimumSize(QSize(82, 30))
        self.quit_button.setMaximumSize(QSize(90, 16777215))
        self.quit_button.setFont(font3)
        self.quit_button.setStyleSheet(u"QPushButton:hover\n"
                                       "{\n"
                                       "color:#333;\n"
                                       "border-radius: 6px;\n"
                                       "background:red;\n"
                                       "\n"
                                       " min-width: 80px;\n"
                                       "}\n"
                                       "QPushButton {\n"
                                       "    border: 1px solid #8f8f91;\n"
                                       "    border-radius: 6px;\n"
                                       "   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                       "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                       "    min-width: 80px;\n"
                                       " \n"
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
                                       "}")
        icon11 = QIcon()
        icon11.addFile(u"images/turn_off_on_power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_button.setIcon(icon11)
        self.quit_button.setIconSize(QSize(32, 32))

        self.gridLayout_5.addWidget(self.quit_button, 0, 5, 1, 1)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        analyze.setCentralWidget(self.centralwidget)

        self.retranslateUi(analyze)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(analyze)

    # setupUi

    def retranslateUi(self, analyze):
        analyze.setWindowTitle(QCoreApplication.translate("analyze", u"Results", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("analyze", u"  Submit Form", None))
        self.label_5.setText("")
        self.select_folder.setText(QCoreApplication.translate("analyze", u"Select Folder", None))
        # TODO: remplir les contenus
        self.folder_path_label.setText("")
        self.log_file_path_label.setText(QCoreApplication.translate("analyze", u"file path", None))
        self.log_file_path_editLine.setText("")
        self.log_file_path_editLine.setPlaceholderText("Enter the file path on the server")

        # if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(
            QCoreApplication.translate("analyze", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(
            QCoreApplication.translate("analyze", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem = self.warning_page.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warning_tab),
                                  QCoreApplication.translate("analyze", u"WARNING", None))
        ___qtreewidgetitem1 = self.fail_page.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fail_tab),
                                  QCoreApplication.translate("analyze", u"FAIL", None))
        ___qtreewidgetitem2 = self.error_page.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("analyze", u"number of occurrences", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.error_tab),
                                  QCoreApplication.translate("analyze", u"ERROR", None))
        ___qtreewidgetitem3 = self.information_page.headerItem()
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.information_tab),
                                  QCoreApplication.translate("analyze", u"INFORMATION", None))
        ___qtreewidgetitem4 = self.debug_page.headerItem()
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("analyze", u"number of occurrences", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debug_tab),
                                  QCoreApplication.translate("analyze", u"DEBUG", None))
        ___qtreewidgetitem5 = self.trace_page.headerItem()
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("analyze", u"number of occurrences", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trace_tab),
                                  QCoreApplication.translate("analyze", u"TRACE", None))
        # if QT_CONFIG(tooltip)
        self.ignoreButton.setToolTip(QCoreApplication.translate("analyze",
                                                                u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clic here to save the selected error in the database and delete it from the log file </span></p></body></html>",
                                                                None))
        # endif // QT_CONFIG(tooltip)
        self.ignoreButton.setText("")
        self.ignoreLabel_2.setText(QCoreApplication.translate("analyze", u"Ignore  ", None))
        # if QT_CONFIG(tooltip)
        self.delete_error_rep.setToolTip(QCoreApplication.translate("analyze",
                                                                    u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clic here to delete repetition of the selected error</span></p></body></html>",
                                                                    None))
        # endif // QT_CONFIG(tooltip)
        self.delete_error_rep.setText("")
        self.memorize_label.setText(QCoreApplication.translate("analyze", u"Delete error repetition", None))
        # if QT_CONFIG(tooltip)
        self.memorize_allexchange.setToolTip(QCoreApplication.translate("analyze",
                                                                        u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clic here to memorize the selected error for all stock exchanges</span></p></body></html>",
                                                                        None))
        # endif // QT_CONFIG(tooltip)
        self.memorize_allexchange.setText("")
        self.label_7.setText(QCoreApplication.translate("analyze", u"Memorize for all exchanges", None))
        # if QT_CONFIG(tooltip)
        self.restoreButton.setToolTip(QCoreApplication.translate("analyze",
                                                                 u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clic here to restore the selected error from database and show it in the log file</span></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.restoreButton.setText("")
        self.restoreLabel.setText(QCoreApplication.translate("analyze", u"Restore", None))
        self.label.setText(QCoreApplication.translate("analyze", u"Errors to ignore", None))
        ___qtreewidgetitem6 = self.unwanted_log_info.headerItem()
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("analyze", u"Message", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("analyze", u"Level", None));
        self.quit_button.setText(QCoreApplication.translate("analyze", u"Quit", None))


        self.hiddenWarningItemIndices = []
        self.hiddenFailItemIndices = []
        self.hiddenErrorItemIndices = []
        self.hiddenInformationItemIndices = []
        self.hiddenDebugItemIndices = []
        self.hiddenTraceItemIndices = []
        self.getUnwatedBug()
        self.showUnwantedBug()





    # retranslateUi


    def addBugItems(self, bugPage, bugType):
        file = bugFile(bugType)
        print(self.bugData)
        for line in file.readlines():
            while (line.startswith(" ")):
                line = line[1::]

            line = line.split(" ", 2)
            # print(self.bugData)

            print(line)
            if  line not in self.bugData:
                print(line)

                bug = QTreeWidgetItem(line)
                bugPage.addTopLevelItem(bug)

    @Slot()
    def getDirectory(self):
        dialog = QFileDialog
        self.folder_path = dialog.getExistingDirectory(None, "Select Folder To Store Files")

    @Slot()
    def getDirectoryPath(self):
        self.folder_path_label.setText(self.folder_path)
        return self.folder_path

    @Slot()
    def submit(self):
        ApiUtilities.LOCAL_FOLDER_PATH = self.folder_path_label.text()
        ApiUtilities.LOG_FILE_PATH = self.log_file_path_editLine.text()
        logFilePathList = self.log_file_path_editLine.text().split("/")
        ApiUtilities.PATH = ""

        for i in range(len(logFilePathList) - 1):
            ApiUtilities.PATH += logFilePathList[i] + '/'

        FetchBugs.fetchBugs()
        self.addBugItems(self.warning_page, "Warning")
        self.addBugItems(self.fail_page, "Fail")
        self.addBugItems(self.error_page, "Error")
        self.addBugItems(self.information_page, "Information")
        self.addBugItems(self.debug_page, "Debug")
        self.addBugItems(self.trace_page, "Trace")

    @Slot()
    def addIgnoredItem(self):


        if self.tabWidget.currentIndex() == 0:
            item ,itemIndex , selectedBug = self.addIgnoredPageItem(self.warning_page)
            self.hiddenWarningItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)

        elif self.tabWidget.currentIndex() == 1:
            item, itemIndex,selectedBug  = self.addIgnoredPageItem(self.fail_page)
            self.hiddenFailItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)


        elif self.tabWidget.currentIndex() == 2:
            item, itemIndex , selectedBug = self.addIgnoredPageItem(self.error_page)
            self.hiddenErrorItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)


        elif self.tabWidget.currentIndex() == 3:
            item, itemIndex , selectedBug = self.addIgnoredPageItem(self.information_page)
            self.hiddenInformationItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)


        elif self.tabWidget.currentIndex() == 4:
            item, itemIndex ,selectedBug = self.addIgnoredPageItem(self.debug_page)
            self.hiddenInformationItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)


        else:
            item, itemIndex , selectedBug = self.addIgnoredPageItem(self.trace_page)
            self.hiddenTraceItemIndices.append(itemIndex)
            if self.hiddenErrorItemIndices.count(itemIndex) < 2:
                self.unwanted_log_info.addTopLevelItem(item)

    def addIgnoredPageItem(self,bugPage):
        global selectedBug, selectedBug, itemIndex, selectedBugItem
        selectedBugItem = None
        selectedBug = None
        itemIndex = None
        selectedBugItem = None
        data = Database.getAll(Bug())
        # hide ignoredItem from bugPage
        selectedBugList = []
        for i in range(3):
            try:
                selectedBugList.append(bugPage.currentItem().data(i, 2))
            except Exception:
                print(Exception)

        selectedBug = Bug(None , selectedBugList[0] , selectedBugList[1] , selectedBugList[2])
        print("selectedBug")
        print("--------------------------------------------------------------------------------------------")
        data = Database.getAll(Bug)
        print(data)
        if Database.itemExist(selectedBug) ==0:
            Database.insert(selectedBug)
        dataInsterted = Database.getBug(selectedBug)
        selectedBugID = dataInsterted[0]
        # insert bug_id , exchange_id in table bug_exchanges
        Database.insert(BugExchange(selectedBugID , ApiUtilities.EXCHANGE_ID) )


        selectedBugItem = QTreeWidgetItem(selectedBugList)
        bugPage.currentItem().setHidden(True)
        itemIndex=bugPage.currentIndex().row()


        return selectedBugItem , itemIndex ,selectedBug
    @Slot()
    def restoreBug(self):
      try:
        selectedItemToRestore = self.unwanted_log_info.currentItem()
        if selectedItemToRestore.data(1,2) == "(W)" :
            self.restoreBugProcess(self.warning_page , selectedItemToRestore)

        elif selectedItemToRestore.data(1,2) == "(F)" :
            self.restoreBugProcess(self.fail_page , selectedItemToRestore)


        elif selectedItemToRestore.data(1, 2) == "(E)":
            self.restoreBugProcess(self.error_page , selectedItemToRestore)


        elif selectedItemToRestore.data(1, 2) == "(D)":
            self.restoreBugProcess(self.debug_page , selectedItemToRestore)


        elif selectedItemToRestore.data(1, 2) == "(I)":
            self.restoreBugProcess(self.information_page , selectedItemToRestore)

        elif selectedItemToRestore.data(1, 2) == "(T)":
            self.restoreBugProcess(self.trace_page, selectedItemToRestore)
      except Exception:
          print(Exception)

    def restoreBugProcess(self , bugPage ,selectedItemToRestore ):

        restoredItem = [selectedItemToRestore.data(0, 2), selectedItemToRestore.data(1, 2),
                        selectedItemToRestore.data(2, 2)]
        restoredItem = QTreeWidgetItem(restoredItem)
        bugPage.addTopLevelItem(restoredItem)

        self.unwanted_log_info.currentItem().setHidden(True)

        bug = Bug(repetition=selectedItemToRestore.data(0,2) ,level=selectedItemToRestore.data(1,2) , description=selectedItemToRestore.data(2,2))
        print(Database.getBug(bug))
        bug.setId(Database.getBug(bug)[0])
        bugExchange = BugExchange(bug.getID() , ApiUtilities.EXCHANGE_ID)
        Database.bugExchangedelete(bugExchange)
        exist = Database.exist(bug)
        if exist == 0:
            Database.delete(bug)

    def getUnwatedBug(self):

        unwantedDataID = Database.getBugExchangeIDByExchangeID(BugExchange , ApiUtilities.EXCHANGE_ID)

        print(unwantedDataID)
        print("unwantedDataID")
        self.bugData=[]
        self.bugExchangeID = []

        for data in unwantedDataID:
            bugExchangeElement = BugExchange(data[0] , data[1])
            self.bugExchangeID.append(bugExchangeElement)
            try:
                item=list(Database.getByID(Bug , bugExchangeElement.getBugID()))
                item.pop(0)

                self.bugData.append(item )

                print(item)
            except Exception:
                print(Exception)
            self.showUnwantedBug

            print("--------------------------------------------------------")

    @Slot()
    def showUnwantedBug(self):
        self.unwanted_log_info.clear()
        for item in self.bugData:
            if self.tabWidget.currentIndex() ==0 and item[1] == "(W)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)

            elif self.tabWidget.currentIndex() == 1 and item[1] == "(F)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)

            elif self.tabWidget.currentIndex() == 2 and item[1] == "(E)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)

            elif self.tabWidget.currentIndex() == 3 and item[1] == "(I)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)

            elif self.tabWidget.currentIndex() == 4 and item[1] == "(D)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)
            elif self.tabWidget.currentIndex() == 5 and item[1] == "(T)":
                item = QTreeWidgetItem(item)
                self.unwanted_log_info.addTopLevelItem(item)
    @Slot()
    def memorizeAllExchange(self):
        bugExchangeData=set(Database.getAll(BugExchange))
        exchangeData = Database.getAll(Exchange)
        for exchangeDataElement in exchangeData:
            for bugExchangeDataElement in bugExchangeData:
                bugExchange = BugExchange(bugExchangeDataElement[0] , exchangeDataElement[0])
                if  bugExchange.toList()  not  in bugExchangeData:
                    Database.insert(bugExchange)
# Error: analyze.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.
#
# analyze.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget2'.
#
#
# while executing 'c:\users\yosri abdedayem\pycharmprojects\pythonproject\venv\lib\site-packages\PySide2\uic -g python analyze.ui'
