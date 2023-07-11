# comdoBox for choise of machine number (for table 1) on line400
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.addItem("   1")
        self.comboBox.addItem("   2")
        self.comboBox.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")


# comdoBox for choise of machine number (for table 1) on line550
        self.comboBox_workerEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_workerEnter.setEditable(False)
        self.comboBox_workerEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")


# comdoBox for choise of machine number (for table 1) on line777
        self.comboBox_shiftEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_shiftEnter.setEditable(False)
        self.comboBox_shiftEnter.addItem("   day")
        self.comboBox_shiftEnter.addItem("   night")
        self.comboBox_shiftEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")
