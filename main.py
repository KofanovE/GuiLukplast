########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

from FunctionsLukplast_new import AppFunctions


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()


        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        
        #QAppSettings.updateAppSettings(self)

        # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        
        #settings = QSettings() 
        #settings.setValue("THEME", "Default-Theme")
        
        # RE APPLY THE NEW SETINGS
        # CompileStyleSheet might also work
        # CompileStyleSheet.applyCompiledSass(self)
        
        #QAppSettings.updateAppSettings(self)



        #Database folder and name
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/LukplastDB.db'))

        
        #Run main functions to cteate database and table
        AppFunctions.main(dbFolder)
        
        #Display data from ShiftTable
        AppFunctions.displayShift(self, AppFunctions.getCurrentShift(self, dbFolder))


        AppFunctions.getTaskStatus1(self, AppFunctions.getCurrentTask(self, dbFolder))
        if AppFunctions.taskStatus1:
            self.ui.closeTable1Btn.setVisible(False)
            self.ui.addPos1Btn.setVisible(False)
        else:
            self.ui.addTable1Btn.setVisible(False)
            AppFunctions.displayTask(self, AppFunctions.getCurrentTask(self, dbFolder))
            AppFunctions.displayPositions(self, AppFunctions.getCurrentPosition(self, dbFolder))
            
        

        #Add new shift data
        self.ui.addShiftBtn.clicked.connect(lambda: AppFunctions.addNewShift(self, dbFolder))

        #Add new task to TaskTable
        self.ui.addTable1Btn.clicked.connect(lambda: AppFunctions.addNewTask(self, dbFolder))

        #Close task for TaskTable
        self.ui.closeTable1Btn.clicked.connect(lambda: AppFunctions.closeTask1(self, dbFolder))

        
        self.ui.addPos1Btn.clicked.connect(lambda: AppFunctions.addNewPosition(self, dbFolder))
        
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
