# comdoBox for choise of machine number (for table 1) on line400
        self.comboBox = QComboBox(self.frameTable1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(75, 30))
        self.comboBox.setMaximumSize(QSize(75, 30))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.addItem("   1")
        self.comboBox.addItem("   2")
        self.comboBox.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")
