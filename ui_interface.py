# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceSlIIOi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 662)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #homeBtn, #mainBodyContent, QLineEdit{\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #mainBody, #topTable1, #botTable1{\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#pushButton{\n"
"	border: 2px solid #00bfff;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"#addUserBtn, #addPos1Btn{\n"
"	background-color: #00bfff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#homeBtn{\n"
"	border-left: 3px solid #00bfff;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"#topTable1, #botTable1{\n"
"	border-radius: 16px;	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.menuBtn)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(1)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(893, 559))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 0))
        self.leftMenu.setMaximumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 529))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 10)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.reportsBtn = QPushButton(self.frame_3)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.reportsBtn)

        self.accountBtn = QPushButton(self.frame_3)
        self.accountBtn.setObjectName(u"accountBtn")
        self.accountBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.accountBtn)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.aboutBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_11 = QVBoxLayout(self.widget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.topTable1 = QFrame(self.widget_5)
        self.topTable1.setObjectName(u"topTable1")
        self.topTable1.setFrameShape(QFrame.StyledPanel)
        self.topTable1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topTable1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.topTable1)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_8.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.topTable1)

        self.tableWidget = QTableWidget(self.widget_5)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)

        self.botTable1 = QFrame(self.widget_5)
        self.botTable1.setObjectName(u"botTable1")
        self.botTable1.setFrameShape(QFrame.StyledPanel)
        self.botTable1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.botTable1)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 5, 10, 5)
        self.addPos1Btn = QPushButton(self.botTable1)
        self.addPos1Btn.setObjectName(u"addPos1Btn")
        self.addPos1Btn.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(14)
        self.addPos1Btn.setFont(font3)
        self.addPos1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addPos1Btn.setIcon(icon3)
        self.addPos1Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.addPos1Btn)

        self.lineEdit_4 = QLineEdit(self.botTable1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.botTable1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_8.addWidget(self.lineEdit_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addWidget(self.botTable1)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_12 = QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.widget_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.tableWidget_2 = QTableWidget(self.widget_6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_12.addWidget(self.tableWidget_2)

        self.frame_9 = QFrame(self.widget_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_12.addWidget(self.frame_9)


        self.horizontalLayout_6.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.homePage)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_13 = QVBoxLayout(self.widget_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_10 = QFrame(self.widget_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.tableWidget_3 = QTableWidget(self.widget_7)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_13.addWidget(self.tableWidget_3)

        self.frame_11 = QFrame(self.widget_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_13)


        self.verticalLayout_13.addWidget(self.frame_11)


        self.horizontalLayout_5.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_14 = QVBoxLayout(self.widget_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_12 = QFrame(self.widget_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_15)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.tableWidget_4 = QTableWidget(self.widget_8)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_14.addWidget(self.tableWidget_4)

        self.frame_13 = QFrame(self.widget_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_14)


        self.verticalLayout_14.addWidget(self.frame_13)


        self.horizontalLayout_5.addWidget(self.widget_8)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.label_3 = QLabel(self.reportsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 20, 111, 61))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        self.label_3.setFont(font4)
        self.mainPages.addWidget(self.reportsPage)
        self.accountsPage = QWidget()
        self.accountsPage.setObjectName(u"accountsPage")
        self.label_4 = QLabel(self.accountsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 10, 111, 61))
        self.label_4.setFont(font4)
        self.mainPages.addWidget(self.accountsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_5 = QLabel(self.settingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 0, 111, 61))
        self.label_5.setFont(font4)
        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_6 = QLabel(self.helpPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 10, 111, 61))
        self.label_6.setFont(font4)
        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_7 = QLabel(self.aboutPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 20, 111, 61))
        self.label_7.setFont(font4)
        self.mainPages.addWidget(self.aboutPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rigthMenu = QWidget(self.mainBody)
        self.rigthMenu.setObjectName(u"rigthMenu")
        self.rigthMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.rigthMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rigthMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u":/icons/Icons/edit.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_9.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.addUserBtn = QPushButton(self.widget_2)
        self.addUserBtn.setObjectName(u"addUserBtn")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.addUserBtn.setFont(font5)
        self.addUserBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addUserBtn.setIcon(icon4)
        self.addUserBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.addUserBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rigthMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 893, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lukplast", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"New smene", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.accountBtn.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TopTable1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"weight", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"worker", None));
        self.addPos1Btn.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"weight", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"worker", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TopTable2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BottomTable2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TopTable3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"BottomTable3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TopTable4", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BottomTable4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.addUserBtn.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
    # retranslateUi

