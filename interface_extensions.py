# test coment
# comdoBox for choise of machine number (for table 1) on line408
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.addItem("   1")
        self.comboBox.addItem("   2")
        self.comboBox.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")

# comdoBox for choise of machine number (for table 1) on line428
        self.locale = QLocale(QLocale.English, QLocale.UnitedStates)  
        self.validator_Double = QDoubleValidator()       
        self.validator_Double.setLocale(self.locale)
        self.LengthEnter1.setValidator(self.validator_Double)


# comdoBox for choise of machine number (for table 1) on line445
        self.validator_Int = QIntValidator()       
        self.validator_Int.setRange(1, 999)
        self.DiametrEnter1.setValidator(self.validator_Int)
        

# comdoBox for choise of machine number (for table 1) on line474
        self.NumPackEnter1.setValidator(self.validator_Int)

# comdoBox for choise of machine number (for table 1) on line662
        self.WeightEnter1.setValidator(self.validator_Double)

# comdoBox for choise of machine number (for table 1) on line674
        self.comboBox_workerEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_workerEnter.setEditable(False)
        self.comboBox_workerEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")


# comdoBox for choise of machine number (for table 1) on line1198
        self.comboBox_shiftEnter.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_shiftEnter.setEditable(False)
        self.comboBox_shiftEnter.addItem("   day")
        self.comboBox_shiftEnter.addItem("   night")
        self.comboBox_shiftEnter.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")








# comdoBox for choise of machine number (for table 1) on line795
        self.comboBox3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox3.setEditable(False)
        self.comboBox3.addItem("   1")
        self.comboBox3.addItem("   2")
        self.comboBox3.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")

# comdoBox for choise of machine number (for table 1) on line815
        self.LengthEnter3.setValidator(self.validator_Double)


# comdoBox for choise of machine number (for table 1) on line829
        self.DiametrEnter3.setValidator(self.validator_Int)
        

# comdoBox for choise of machine number (for table 1) on line856
        self.NumPackEnter3.setValidator(self.validator_Int)

# comdoBox for choise of machine number (for table 1) on line1038
        self.WeightEnter3.setValidator(self.validator_Double)

# comdoBox for choise of machine number (for table 1) on line1047
        self.comboBox_workerEnter3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_workerEnter3.setEditable(False)
        self.comboBox_workerEnter3.setStyleSheet("QComboBox { text-align: center; }"
                                    "QComboBox::item:selected { background-color: #1b1b27; color: white; }"
                                    "QComboBox::item:!selected { background-color: #1b1b27; color: grey; }")








