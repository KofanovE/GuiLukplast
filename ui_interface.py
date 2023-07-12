# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceNKmCRJ.ui'
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
        MainWindow.resize(1245, 882)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #homeBtn, #mainBodyContent, QLineEdit, QComboBox{\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #mainBody, #topTable1, #botTable1, #footer, #frame_7, #frame_14, #frame_15, #frame_16{\n"
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
"#addTable1Btn{\n"
"	background-color: #00bfff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#closeTable1Btn{\n"
"	background-color: #00bfff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#addPos1Btn{\n"
"	background-color: #708238;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
""
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
"}\n"
"\n"
"#frameTable1{\n"
"	background-color: #5A5A5A;\n"
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frameShift = QFrame(self.header)
        self.frameShift.setObjectName(u"frameShift")
        self.frameShift.setFrameShape(QFrame.StyledPanel)
        self.frameShift.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frameShift)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.frameShift)
        self.label_20.setObjectName(u"label_20")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_20.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_20)

        self.masterShow = QLineEdit(self.frameShift)
        self.masterShow.setObjectName(u"masterShow")
        self.masterShow.setMinimumSize(QSize(75, 30))
        self.masterShow.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_17.addWidget(self.masterShow)

        self.label_21 = QLabel(self.frameShift)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_21)

        self.worker1Show = QLineEdit(self.frameShift)
        self.worker1Show.setObjectName(u"worker1Show")
        self.worker1Show.setMinimumSize(QSize(75, 30))
        self.worker1Show.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_17.addWidget(self.worker1Show)

        self.label_22 = QLabel(self.frameShift)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_22)

        self.worker2Show = QLineEdit(self.frameShift)
        self.worker2Show.setObjectName(u"worker2Show")
        self.worker2Show.setMinimumSize(QSize(75, 30))
        self.worker2Show.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_17.addWidget(self.worker2Show)

        self.label_23 = QLabel(self.frameShift)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.worker3Show = QLineEdit(self.frameShift)
        self.worker3Show.setObjectName(u"worker3Show")
        self.worker3Show.setMinimumSize(QSize(75, 30))
        self.worker3Show.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_17.addWidget(self.worker3Show)


        self.horizontalLayout.addWidget(self.frameShift)

        self.horizontalSpacer_3 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

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
        font2 = QFont()
        font2.setPointSize(1)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame)


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
        self.AllTopTables = QWidget(self.homePage)
        self.AllTopTables.setObjectName(u"AllTopTables")
        self.horizontalLayout_6 = QHBoxLayout(self.AllTopTables)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LeftTopTable = QWidget(self.AllTopTables)
        self.LeftTopTable.setObjectName(u"LeftTopTable")
        self.verticalLayout_11 = QVBoxLayout(self.LeftTopTable)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.topTable1 = QFrame(self.LeftTopTable)
        self.topTable1.setObjectName(u"topTable1")
        self.topTable1.setFrameShape(QFrame.StyledPanel)
        self.topTable1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topTable1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.topTable1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.TaskNum1 = QLineEdit(self.topTable1)
        self.TaskNum1.setObjectName(u"TaskNum1")
        self.TaskNum1.setMinimumSize(QSize(75, 30))
        self.TaskNum1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_7.addWidget(self.TaskNum1)

        self.frameTable1 = QFrame(self.topTable1)
        self.frameTable1.setObjectName(u"frameTable1")
        self.frameTable1.setFrameShape(QFrame.StyledPanel)
        self.frameTable1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frameTable1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.frameTable1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.comboBox = QComboBox(self.frameTable1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(75, 30))
        self.comboBox.setMaximumSize(QSize(75, 30))
        self.comboBox.setPlaceholderText(u"Num")
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.addItem("   1")
        self.comboBox.addItem("   2")
        self.comboBox.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")

        self.horizontalLayout_15.addWidget(self.comboBox)

        self.label_16 = QLabel(self.frameTable1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.LengthEnter1 = QLineEdit(self.frameTable1)
        self.LengthEnter1.setObjectName(u"LengthEnter1")
        self.LengthEnter1.setMinimumSize(QSize(75, 30))
        self.LengthEnter1.setMaximumSize(QSize(75, 30))
        self.locale = QLocale(QLocale.English, QLocale.UnitedStates)  
        self.validator_Double = QDoubleValidator()       
        self.validator_Double.setLocale(self.locale)
        self.LengthEnter1.setValidator(self.validator_Double)

        self.horizontalLayout_15.addWidget(self.LengthEnter1)

        self.label_17 = QLabel(self.frameTable1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_17)

        self.DiametrEnter1 = QLineEdit(self.frameTable1)
        self.DiametrEnter1.setObjectName(u"DiametrEnter1")
        self.DiametrEnter1.setMinimumSize(QSize(75, 30))
        self.DiametrEnter1.setMaximumSize(QSize(75, 30))
        self.validator_Int = QIntValidator()       
        self.validator_Int.setRange(1, 999)
        self.DiametrEnter1.setValidator(self.validator_Int)

        self.horizontalLayout_15.addWidget(self.DiametrEnter1)

        self.label_18 = QLabel(self.frameTable1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_18)

        self.TypeEnter1 = QLineEdit(self.frameTable1)
        self.TypeEnter1.setObjectName(u"TypeEnter1")
        self.TypeEnter1.setMinimumSize(QSize(75, 30))
        self.TypeEnter1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_15.addWidget(self.TypeEnter1)

        self.label_24 = QLabel(self.frameTable1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_24)

        self.NumPackEnter1 = QLineEdit(self.frameTable1)
        self.NumPackEnter1.setObjectName(u"NumPackEnter1")
        self.NumPackEnter1.setMinimumSize(QSize(75, 30))
        self.NumPackEnter1.setMaximumSize(QSize(75, 30))
        self.NumPackEnter1.setValidator(self.validator_Int)

        self.horizontalLayout_15.addWidget(self.NumPackEnter1)


        self.horizontalLayout_7.addWidget(self.frameTable1)

        self.addTable1Btn = QPushButton(self.topTable1)
        self.addTable1Btn.setObjectName(u"addTable1Btn")
        self.addTable1Btn.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(14)
        self.addTable1Btn.setFont(font3)
        self.addTable1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addTable1Btn.setIcon(icon3)
        self.addTable1Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.addTable1Btn)

        self.closeTable1Btn = QPushButton(self.topTable1)
        self.closeTable1Btn.setObjectName(u"closeTable1Btn")
        self.closeTable1Btn.setMinimumSize(QSize(0, 0))
        self.closeTable1Btn.setFont(font3)
        self.closeTable1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeTable1Btn.setIcon(icon4)
        self.closeTable1Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.closeTable1Btn)


        self.verticalLayout_11.addWidget(self.topTable1)

        self.widget_3 = QWidget(self.LeftTopTable)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.tableWidget = QTableWidget(self.widget_3)
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

        self.horizontalLayout_23.addWidget(self.tableWidget)

        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(220, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_4 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 30))
        self.label_30.setMaximumSize(QSize(100, 30))
        self.label_30.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.Count_Show_1 = QLineEdit(self.frame_7)
        self.Count_Show_1.setObjectName(u"Count_Show_1")
        self.Count_Show_1.setMinimumSize(QSize(75, 30))
        self.Count_Show_1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_19.addWidget(self.Count_Show_1)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_5 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.label_33 = QLabel(self.frame_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(100, 30))
        self.label_33.setMaximumSize(QSize(100, 30))
        self.label_33.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_33)

        self.SumLength_Show_1 = QLineEdit(self.frame_14)
        self.SumLength_Show_1.setObjectName(u"SumLength_Show_1")
        self.SumLength_Show_1.setMinimumSize(QSize(75, 30))
        self.SumLength_Show_1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_20.addWidget(self.SumLength_Show_1)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_6 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_6)

        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(100, 30))
        self.label_31.setMaximumSize(QSize(100, 30))
        self.label_31.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_31)

        self.SumWeight_Show_1 = QLineEdit(self.frame_16)
        self.SumWeight_Show_1.setObjectName(u"SumWeight_Show_1")
        self.SumWeight_Show_1.setMinimumSize(QSize(75, 30))
        self.SumWeight_Show_1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_21.addWidget(self.SumWeight_Show_1)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_7 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_7)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 30))
        self.label_32.setMaximumSize(QSize(100, 30))
        self.label_32.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_32)

        self.CountPack_Show_1 = QLineEdit(self.frame_15)
        self.CountPack_Show_1.setObjectName(u"CountPack_Show_1")
        self.CountPack_Show_1.setMinimumSize(QSize(75, 30))
        self.CountPack_Show_1.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_22.addWidget(self.CountPack_Show_1)


        self.verticalLayout_15.addWidget(self.frame_15)


        self.horizontalLayout_23.addWidget(self.frame_6)


        self.verticalLayout_11.addWidget(self.widget_3)

        self.botTable1 = QFrame(self.LeftTopTable)
        self.botTable1.setObjectName(u"botTable1")
        self.botTable1.setFrameShape(QFrame.StyledPanel)
        self.botTable1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.botTable1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.WeightEnter1 = QLineEdit(self.botTable1)
        self.WeightEnter1.setObjectName(u"WeightEnter1")
        self.WeightEnter1.setValidator(self.validator_Double)

        self.horizontalLayout_8.addWidget(self.WeightEnter1)

        self.comboBox_workerEnter = QComboBox(self.botTable1)
        self.comboBox_workerEnter.setObjectName(u"comboBox_workerEnter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.comboBox_workerEnter.sizePolicy().hasHeightForWidth())
        self.comboBox_workerEnter.setSizePolicy(sizePolicy1)
        self.comboBox_workerEnter.setMinimumSize(QSize(0, 30))
        self.comboBox_workerEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_workerEnter.setEditable(False)
        self.comboBox_workerEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")

        self.horizontalLayout_8.addWidget(self.comboBox_workerEnter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.addPos1Btn = QPushButton(self.botTable1)
        self.addPos1Btn.setObjectName(u"addPos1Btn")
        self.addPos1Btn.setMinimumSize(QSize(0, 0))
        self.addPos1Btn.setFont(font3)
        self.addPos1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addPos1Btn.setIcon(icon5)
        self.addPos1Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.addPos1Btn)


        self.verticalLayout_11.addWidget(self.botTable1)


        self.horizontalLayout_6.addWidget(self.LeftTopTable)

        self.widget_6 = QWidget(self.AllTopTables)
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
        font4 = QFont()
        font4.setPointSize(12)
        self.label_10.setFont(font4)

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
        self.label_11.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_12.addWidget(self.frame_9)


        self.horizontalLayout_6.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.AllTopTables)

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
        self.label_12.setFont(font4)

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
        self.label_13.setFont(font4)

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
        self.label_15.setFont(font4)

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
        self.label_14.setFont(font4)

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
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        font5.setStrikeOut(False)
        self.label_3.setFont(font5)
        self.mainPages.addWidget(self.reportsPage)
        self.accountsPage = QWidget()
        self.accountsPage.setObjectName(u"accountsPage")
        self.label_4 = QLabel(self.accountsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 10, 111, 61))
        self.label_4.setFont(font5)
        self.mainPages.addWidget(self.accountsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_5 = QLabel(self.settingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 0, 111, 61))
        self.label_5.setFont(font5)
        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_6 = QLabel(self.helpPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 10, 111, 61))
        self.label_6.setFont(font5)
        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_7 = QLabel(self.aboutPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 20, 111, 61))
        self.label_7.setFont(font5)
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
        self.comboBox_shiftEnter = QComboBox(self.frame_5)
        self.comboBox_shiftEnter.setObjectName(u"comboBox_shiftEnter")
        sizePolicy1.setHeightForWidth(self.comboBox_shiftEnter.sizePolicy().hasHeightForWidth())
        self.comboBox_shiftEnter.setSizePolicy(sizePolicy1)
        self.comboBox_shiftEnter.setMinimumSize(QSize(0, 30))
        self.comboBox_shiftEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_shiftEnter.setEditable(False)
        self.comboBox_shiftEnter.addItem("   day")
        self.comboBox_shiftEnter.addItem("   night")
        self.comboBox_shiftEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")

        self.verticalLayout_9.addWidget(self.comboBox_shiftEnter)

        self.masterEnter = QLineEdit(self.frame_5)
        self.masterEnter.setObjectName(u"masterEnter")

        self.verticalLayout_9.addWidget(self.masterEnter)

        self.lay1Enter = QLineEdit(self.frame_5)
        self.lay1Enter.setObjectName(u"lay1Enter")

        self.verticalLayout_9.addWidget(self.lay1Enter)

        self.lay2Enter = QLineEdit(self.frame_5)
        self.lay2Enter.setObjectName(u"lay2Enter")

        self.verticalLayout_9.addWidget(self.lay2Enter)

        self.lay3Enter = QLineEdit(self.frame_5)
        self.lay3Enter.setObjectName(u"lay3Enter")

        self.verticalLayout_9.addWidget(self.lay3Enter)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.addShiftBtn = QPushButton(self.widget_2)
        self.addShiftBtn.setObjectName(u"addShiftBtn")
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.addShiftBtn.setFont(font6)
        self.addShiftBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addShiftBtn.setIcon(icon3)
        self.addShiftBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.addShiftBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rigthMenu)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_16 = QHBoxLayout(self.footer)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.footer)
        self.label_19.setObjectName(u"label_19")
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.label_19.setFont(font7)

        self.horizontalLayout_16.addWidget(self.label_19, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lukplast", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Master", None))
        self.masterShow.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Worker 1", None))
        self.worker1Show.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Worker 2", None))
        self.worker2Show.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Worker 3", None))
        self.worker3Show.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.TaskNum1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12345", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.LengthEnter1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.DiametrEnter1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.TypeEnter1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Num", None))
        self.NumPackEnter1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"8", None))
        self.addTable1Btn.setText("")
        self.closeTable1Btn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"weight", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"worker", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.Count_Show_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Sum Length", None))
        self.SumLength_Show_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Sum Weight", None))
        self.SumWeight_Show_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Count Packs", None))
        self.CountPack_Show_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.WeightEnter1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"weight", None))
        self.comboBox_workerEnter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Worker name", None))
        self.addPos1Btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TopTable22", None))
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
        self.comboBox_shiftEnter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"shift", None))
        self.masterEnter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Master", None))
        self.lay1Enter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Layborer 1", None))
        self.lay2Enter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Layborer 2", None))
        self.lay3Enter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Layborer 3", None))
        self.addShiftBtn.setText(QCoreApplication.translate("MainWindow", u"Add Shift", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Lukplast. Copyright 2023", None))
    # retranslateUi

