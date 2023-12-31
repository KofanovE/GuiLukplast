## IMPORTS

import os
import sys

# Import SQLite
import sqlite3
from sqlite3 import Error


# Import QtableWidgetItem (for creating new table cells)
from PySide2.QtWidgets import QTableWidgetItem


sumLength = sumWeight =  0
sumLength3 = sumWeight3 =  0


# Function class
class AppFunctions():
   
    """docstring for AppFunctions"""
    taskStatus3 = 0
    idTask3 = 0
    taskStatus3 = 0        
    numInPack3 = 0
    lengthTask3 = 0

    

    def __init__(self, arg):

        
        super().__init__()

        
        self.arg = arg
        self.master_list = []
        self.layborer_list = []
        self.idShift = 0

        # third table
        

        # first table
        self.idTask1 = 0
        self.taskStatus1 = 0        
        self.numInPack = 0
        self.lengthTask = 0

        


        


        



    ## Create database connection
    def create_connection(db_file):

        """ create a database connection to a SQLite database"""
        
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        # Return connection
        return conn

    ## Create table
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


    ## Main function
    def main(dbFolder):

        
        
        # Create table if it does not exist
        create_ShiftTable = """ CREATE TABLE IF NOT EXISTS ShiftTable (
                                     ID_SHIFT INTEGER PRIMARY KEY AUTOINCREMENT,
                                     DATE TEXT,
                                     TIME TEXT,
                                     SHIFT TEXT,
                                     MASTER TEXT,
                                     LYB_1 TEXT,
                                     LYB_2 TEXT,
                                     LYB_3 TEXT

                            
                                );
                            """

        
        create_TaskTable = """ CREATE TABLE IF NOT EXISTS TaskTable (
                                    TASK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    DATE TEXT,
                                    TIME TEXT,
                                    ID_SHIFT INTEGER,
                                    MACHINE INTEGER,
                                    LENGTH INTEGER,
                                    DIAMETR INTEGER,
                                    NUM_IN_PACK INTEGER,
                                    TYPE TEXT,
                                    SUM_WEIGHT REAL,
                                    SUM_LENGTH REAL,
                                    CLOSED INTEGER,
                                    NUM_TABLE INTEGER,
                                    CONSTRAINT ID_SHIFT FOREIGN KEY (ID_SHIFT) REFERENCES ShiftTable (ID_SHIFT)
                                    
                                );
                            """

        create_AllPositions = """ CREATE TABLE IF NOT EXISTS AllPositions (
                                          ID_ALL_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,  
                                          ID_TASK INTEGER,
                                          ID_POSITION INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT REAL,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID),
                                          CONSTRAINT ID_POSITION FOREIGN KEY (ID_POSITION) REFERENCES OneTaskPosition1 (ID_POSITION)

                                    );
                            """

        create_OneTaskPosition1 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition1(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """

        create_OneTaskPosition3 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition3(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """

        create_OneTaskPosition4 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition4(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """
        
        create_Team = """ CREATE TABLE IF NOT EXISTS Team(
                                          ID_PERSON INTEGER PRIMARY KEY AUTOINCREMENT,
                                          FIRST_NAME TEXT,
                                          SECOND_NAME TEXT,                                         
                                          FUNCTION_1 TEXT,
                                          FUNCTION_2 TEXT,
                                          BIRTH_DATE TEXT,
                                          PHONE_1 TEXT,
                                          T_1 TEXT,
                                          V_1 TEXT,
                                          W_1 TEXT,
                                          PHONE_2 TEXT,
                                          T_2 TEXT,
                                          V_2 TEXT,
                                          W_2 TEXT,
                                          PHONE_RELAT TEXT,
                                          REGIST_ADDR TEXT,
                                          RESID_ADDR TEXT,
                                          PASPORT_CODE TEXT,
                                          CHARACTERISTIC TEXT,
                                          REGISTR_DATE TEXT,
                                          DISMIS_DATE TEXT
                                          
                                          
                                    );
                                 """


        
        

       
        
        conn = AppFunctions.create_connection(dbFolder)

        # create tables
        if conn is not None:
            # create user table
            AppFunctions.create_table(conn, create_ShiftTable)
            AppFunctions.create_table(conn, create_TaskTable)
            AppFunctions.create_table(conn, create_AllPositions)
            AppFunctions.create_table(conn, create_OneTaskPosition1)
            AppFunctions.create_table(conn, create_OneTaskPosition3)
            AppFunctions.create_table(conn, create_OneTaskPosition4)
            AppFunctions.create_table(conn, create_Team)

                     

            
        else:
            print('Error! Cannot create the database connection')


        

      
    #1 create new shift
    def addNewShift(self, dbFolder):

        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values

        
        
        if self.ui.comboBox_shiftEnter.currentIndex() == 0:
            shift = "day"
        elif self.ui.comboBox_shiftEnter.currentIndex() == 1:
            shift = "night"
        else:
            shift = "Not choised"
        
        master = self.ui.masterEnter.text()
        lyb_1 = self.ui.lay1Enter.text()
        lyb_2 = self.ui.lay2Enter.text()
        lyb_3 = self.ui.lay3Enter.text()
        
        # create sql statement
        insert_shift_data_sql = f"""
        INSERT INTO ShiftTable (DATE, TIME, SHIFT, MASTER, LYB_1, LYB_2, LYB_3) VALUES (CURRENT_DATE, CURRENT_TIME, '{shift}', '{master}', '{lyb_1}', '{lyb_2}', '{lyb_3}');
        """

      
        
        del_last_shift_data = f"""
        DROP TABLE IF EXISTS OneTaskPosition1;
        """

        create_OneTaskPosition1 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition1(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """
        create_OneTaskPosition3 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition3(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """

        create_OneTaskPosition4 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition4(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """
        if conn is not None:
            # create user table
            conn.cursor().execute(insert_shift_data_sql)
            conn.cursor().execute(del_last_shift_data)
            conn.cursor().execute(create_OneTaskPosition1)
            conn.cursor().execute(create_OneTaskPosition3)
            conn.cursor().execute(create_OneTaskPosition4)
            conn.commit()
            # clear form input
            self.ui.comboBox_shiftEnter.setCurrentIndex(-1)
            self.ui.masterEnter.setText("")
            self.ui.lay1Enter.setText("")
            self.ui.lay2Enter.setText("")
            self.ui.lay3Enter.setText("")
            self.ui.comboBox_workerEnter.clear()
            self.ui.comboBox_workerEnter3.clear()
            AppFunctions.displayShift(self, AppFunctions.getCurrentShift(self, dbFolder))
            
        else:
            print("Could not insert shift data")
                        
            # load new user from DB to table view
            AppFunctions.displayShift(self, AppFunctions.getCurrentShift(self, dbFolder))


    
    #2. get information from last row of ShiftTable
    def getCurrentShift(self, dbFolder):
        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)

        get_last_shift = """
                            SELECT * FROM ShiftTable ORDER BY ROWID DESC LIMIT 1;
                        """
        try:
            c = conn.cursor()
            c.execute(get_last_shift)
            # return all table rows
            return c
        except Error as e:
            print(e)
        

    """
    #3. if there is a OneTaskPosition1 table - all data delete
    def delLastShiftInfo(self, dbFolder):
        pass
    """


    
    #4. add new task of corect shift to OneTaskPosition1
    def addNewTask(self, dbFolder):

        global sumWeight, sumLength
        

        sumWeight = sumLength = 0
        
 

        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        
        # get form values
        machine = 1
        length = self.ui.LengthEnter1.text()
        diametr = self.ui.DiametrEnter1.text()
        num_in_pack = self.ui.NumPackEnter1.text()
        type_pype = self.ui.TypeEnter1.text()
        


        # create sql statement        
        insert_task_data_sql = f"""
        INSERT INTO TaskTable (DATE, TIME, ID_SHIFT, MACHINE, LENGTH, DIAMETR, NUM_IN_PACK, TYPE, SUM_WEIGHT, SUM_LENGTH, CLOSED, NUM_TABLE) 
        VALUES (CURRENT_DATE, CURRENT_TIME, '{AppFunctions.idShift}', '{machine}', '{length}', '{diametr}', '{num_in_pack}', '{type_pype}', '{sumWeight}', '{sumLength}', '{0}', '{1}');
        """

        del_last_shift_data = f"""
        DROP TABLE IF EXISTS  OneTaskPosition1;
        """

        create_OneTaskPosition1 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition1(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """ 

        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_data_sql)
            conn.cursor().execute(del_last_shift_data)
            conn.cursor().execute(create_OneTaskPosition1)
            conn.commit()
            
            # clear form input
            self.ui.LengthEnter1.setText("")
            self.ui.DiametrEnter1.setText("")
            self.ui.NumPackEnter1.setText("")
            self.ui.TypeEnter1.setText("")
            
            AppFunctions.displayTask(self, AppFunctions.getCurrentTask(self, dbFolder))
            AppFunctions.getTaskStatus1(self, AppFunctions.getCurrentTask(self, dbFolder))
            self.ui.WeightEnter1.setReadOnly(False)
            self.ui.addTable1Btn.setVisible(False)
            self.ui.closeTable1Btn.setVisible(True)
            self.ui.addPos1Btn.setVisible(True)           
            self.ui.tableWidget.clearContents()
            
        else:
            print("Could not insert shift data")           
            
            # load new user from DB to table view
            AppFunctions.displayTask(self, AppFunctions.getCurrentTask(self, dbFolder))
            AppFunctions.getTaskStatus1(self, AppFunctions.getCurrentTask(self, dbFolder))


    

    """
    #5. add last task to TaskTable
    def addTaskToTaskTable(self, dbFolder):
        pass        

    """

    #6. add new position to OneTaskPosition1.
    def addNewPosition(self, dbFolder):

        global sumWeight, sumLength
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        weight = self.ui.WeightEnter1.text()        
        worker = self.ui.comboBox_workerEnter.currentText()
        
        
        sumWeight += float(weight)
        sumL = AppFunctions.numInPack * AppFunctions.lengthTask
        sumLength += sumL
        
        
        # create sql statement
        insert_position_data_sql = f"""
        INSERT INTO OneTaskPosition1(ID_TASK, DATE, TIME, WEIGHT, WORKER) VALUES ('{AppFunctions.idTask1}', CURRENT_DATE, CURRENT_TIME, '{weight}', '{worker}');
        """

        insert_last_position_to_global = f"""
        INSERT INTO AllPositions (ID_TASK, ID_POSITION, DATE, TIME, WEIGHT, WORKER) SELECT ID_TASK, ID_POSITION, DATE, TIME, WEIGHT, WORKER FROM OneTaskPosition1 ORDER BY ROWID DESC LIMIT 1;
        """
        
        insert_sum_to_task = f"""
        UPDATE TaskTable SET SUM_WEIGHT = ('{sumWeight}'), SUM_LENGTH = ('{sumLength}') WHERE TASK_ID = ('{AppFunctions.idTask1}') ;
        """
        
        if conn is not None:
            # create user table
            conn.cursor().execute(insert_position_data_sql)
            conn.cursor().execute(insert_last_position_to_global)        
            conn.cursor().execute(insert_sum_to_task)
            conn.commit()
            # clear form input
            AppFunctions.displayPositions(self, AppFunctions.getCurrentPosition(self, dbFolder))
            
        else:
            print("Could not insert position data")
                        
            # load new user from DB to table view
            AppFunctions.displayPositions(self, AppFunctions.getCurrentPosition(self, dbFolder))

        self.ui.WeightEnter1.setText("")



    """
    #7. add last new position from OneTaskPosition1 to AllPosition table.
    def addPostionToAllPositionsTable(self, dbFolder):
        pass
    """
    
    #8. display all positons of current task
    def displayPositions(self, rows):

        global sumWeight, sumLength
        
        self.ui.SumLength_Show_1.setText(str(round(sumLength, 2)))
        self.ui.SumWeight_Show_1.setText(str(round(sumWeight, 2)))

        for row in rows:
            # get number of rows
            rowPosition = self.ui.tableWidget.rowCount()
            print("1.")
            print("rowPosition = ", rowPosition)
            print("row", row)

            # skip rows that have alreade been loaded to table
            if rowPosition + 1 > row[0]:
                print('ahtung')
                continue
            
            itemCount = 0
            # create new table row
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # add items to row
            for item in row:
                write_flag = 0
                print(itemCount, item)
                
                if itemCount == 0:
                    itemPosition = itemCount
                    self.ui.CountPack_Show_1.setText(str(item))
                    self.ui.Count_Show_1.setText(str(item * AppFunctions.numInPack))
                    write_flag = 1
                    print('sos', item, item*AppFunctions.numInPack)
                    
                elif itemCount == 3:
                    itemPosition = 1
                    write_flag = 1
                    
                elif itemCount == 4:
                    itemPosition = 2
                    write_flag = 1
                    
                elif itemCount == 5:
                    itemPosition = 3
                    write_flag = 1
                if write_flag:
                    self.qtablewidgetitem = QTableWidgetItem()
                    self.ui.tableWidget.setItem(rowPosition, itemPosition, self.qtablewidgetitem)
                    self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition, itemPosition)
                    self.qtablewidgetitem.setText(str(item))
                itemCount = itemCount + 1
                
            rowPosition = rowPosition + 1


    
    #9. display shift informations:
    def displayShift(self, row):
        itemCount = 0
        # add items to row
        for items in row:
            for item in items:
                if itemCount == 0:
                    AppFunctions.idShift = item
                elif itemCount == 4:
                    self.ui.masterShow.setText(item)
                    if item:
                        self.ui.num_workers = 0
                        self.ui.comboBox_workerEnter.addItem(item)
                        self.ui.comboBox_workerEnter3.addItem(item)   
                elif itemCount == 5:
                    self.ui.worker1Show.setText(item)
                    if item:
                        self.ui.num_workers = 1
                        self.ui.comboBox_workerEnter.addItem(item)
                        self.ui.comboBox_workerEnter3.addItem(item)
                elif itemCount == 6:
                    self.ui.worker2Show.setText(item)
                    if item:
                        self.ui.num_workers = 2
                        self.ui.comboBox_workerEnter.addItem(item)
                        self.ui.comboBox_workerEnter3.addItem(item)
                elif itemCount == 7:
                    self.ui.worker3Show.setText(item)
                    if item:
                        self.ui.num_workers = 3
                        self.ui.comboBox_workerEnter.addItem(item)
                        self.ui.comboBox_workerEnter3.addItem(item)
                itemCount += 1
        


    #10. display current informations of current task:
    def displayTask(self, row):
        
        itemCount = 0
        self.ui.comboBox_workerEnter.setEnabled(True)
        # add items to row
        for items in row:
                
            for item in items:
                if itemCount == 0:
                    AppFunctions.idTask1 = item
                    self.ui.TaskNum1.setText(str(item))
                    self.ui.TaskNum1.setReadOnly(True)
                elif itemCount == 4:
                    if str(item) == "1":
                        index_to_select = 0
                    else:
                        index_to_select = 1                
                    self.ui.comboBox.setCurrentIndex(index_to_select)
                    self.ui.comboBox.setEnabled(False)
                elif itemCount == 5:
                    self.ui.LengthEnter1.setText(str(item))
                    self.ui.LengthEnter1.setReadOnly(True)
                elif itemCount == 6:
                    self.ui.DiametrEnter1.setText(str(item))
                    self.ui.DiametrEnter1.setReadOnly(True)
                elif itemCount == 8:
                    self.ui.TypeEnter1.setText(str(item))
                    self.ui.TypeEnter1.setReadOnly(True)
                elif itemCount == 7:
                    self.ui.NumPackEnter1.setText(str(item))
                    self.ui.NumPackEnter1.setReadOnly(True) 
                itemCount += 1
        

    #11. get current task information for current table
    def getCurrentTask(self, dbFolder):        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        get_last_task = f"""
                            SELECT * FROM TaskTable WHERE NUM_TABLE = 1 ORDER BY ROWID DESC LIMIT 1;
                         """
        try:
            c = conn.cursor()
            c.execute(get_last_task)
            # return all table rows
            return c
        except Error as e:
            print(e)

    #12. close task for table1
    def closeTask1(self, dbFolder):

        conn = AppFunctions.create_connection(dbFolder)

        #self.ui.MachineNum1.setText("")
        self.ui.WeightEnter1.setReadOnly(True)
        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox.setEnabled(True)
        self.ui.comboBox_workerEnter.setCurrentIndex(-1)
        self.ui.comboBox_workerEnter.setEnabled(False)
        self.ui.WeightEnter1.setText("")
        self.ui.LengthEnter1.setText("")
        self.ui.LengthEnter1.setReadOnly(False)
        self.ui.DiametrEnter1.setText("")
        self.ui.DiametrEnter1.setReadOnly(False)
        self.ui.NumPackEnter1.setText("")
        self.ui.NumPackEnter1.setReadOnly(False)
        self.ui.TypeEnter1.setText("")
        self.ui.TypeEnter1.setReadOnly(False)
        self.ui.TaskNum1.setText("")
        self.ui.TaskNum1.setReadOnly(False)

        self.ui.SumWeight_Show_1.setText("")
        self.ui.SumLength_Show_1.setText("")
        self.ui.Count_Show_1.setText("")
        self.ui.CountPack_Show_1.setText("")

        self.ui.addTable1Btn.setVisible(True)
        self.ui.closeTable1Btn.setVisible(False)
        self.ui.addPos1Btn.setVisible(False)

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)



        insert_task_close_marker = f"""
        UPDATE TaskTable SET CLOSED = ('{1}') WHERE TASK_ID = ('{AppFunctions.idTask1}') ;
        """

        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_close_marker)
            conn.commit()           
        else:
            print("Could not insert shift data")           


    #13. get closed_status task for table 1
    def getTaskStatus1(self, row):
        global sumWeight, sumLength
        for items in row:
            AppFunctions.taskStatus1 = items[11]
            AppFunctions.idTask1 = items[0]
            AppFunctions.numInPack = items[7]
            AppFunctions.lengthTask = items[5]
            sumWeight = items[9]
            sumLength = items[10]

        
            


    #14. get current postition information for current table
    def getCurrentPosition(self, dbFolder):        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        get_positions = """
                            SELECT * FROM OneTaskPosition1;
                        """
        try:
            c = conn.cursor()
            c.execute(get_positions)
            # return all table rows
            return c
        except Error as e:
            print(e)
            
    #15. get masterList from Team table
    def getMasterList(self, dbFolder):
        # create db connection
        master = 'master'
        conn = AppFunctions.create_connection(dbFolder)
        get_masters = """
                                SELECT SECOND_NAME FROM Team WHERE FUNCTION_1 = 'master';
                      """
        try:
            c = conn.cursor()
            c.execute(get_masters)
            result = c.fetchall()
            values_list = [row[0] for row in result]
            AppFunctions.master_list = values_list
            
        except Error as e:
            print(e)


    #16. get layborerList from Team table
    def getLaborerList(self, dbFolder):
        # create db connection
        laborer = 'laborer'
        conn = AppFunctions.create_connection(dbFolder)
        get_laborers = """
                                SELECT SECOND_NAME FROM Team WHERE FUNCTION_1 = 'laborer' OR FUNCTION_2 = 'laborer';
                      """
        try:
            c = conn.cursor()
            c.execute(get_laborers)
            result = c.fetchall()
            values_list = [row[0] for row in result]
            AppFunctions.laborer_list = values_list
            
        except Error as e:
            print(e)




    """
    Methods of driving the third table
    """





    #4. add new task of corect shift to OneTaskPosition1
    def addNewTask3(self, dbFolder):

        global sumWeight3, sumLength3
        

        sumWeight3 = sumLength3 = 0
        
 

        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        
        # get form values
        machine = 2
        length = self.ui.LengthEnter3.text()
        diametr = self.ui.DiametrEnter3.text()
        num_in_pack = self.ui.NumPackEnter3.text()
        type_pype = self.ui.TypeEnter3.text()
        


        # create sql statement        
        insert_task_data_sql = f"""
        INSERT INTO TaskTable (DATE, TIME, ID_SHIFT, MACHINE, LENGTH, DIAMETR, NUM_IN_PACK, TYPE, SUM_WEIGHT, SUM_LENGTH, CLOSED, NUM_TABLE) 
        VALUES (CURRENT_DATE, CURRENT_TIME, '{AppFunctions.idShift}', '{machine}', '{length}', '{diametr}', '{num_in_pack}', '{type_pype}', '{sumWeight3}', '{sumLength3}', '{0}', '{3}');
        """

        del_last_shift_data = f"""
        DROP TABLE IF EXISTS  OneTaskPosition3;
        """

        create_OneTaskPosition3 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition3(
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          ID_TASK INTEGER,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT TEXT,
                                          WORKER TEXT,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)
                                          
                                          
                                    );
                                 """ 

        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_data_sql)
            conn.cursor().execute(del_last_shift_data)
            conn.cursor().execute(create_OneTaskPosition3)
            conn.commit()
            
            # clear form input
            self.ui.LengthEnter3.setText("")
            self.ui.DiametrEnter3.setText("")
            self.ui.NumPackEnter3.setText("")
            self.ui.TypeEnter3.setText("")
            
            AppFunctions.displayTask3(self, AppFunctions.getCurrentTask3(self, dbFolder))
            AppFunctions.getTaskStatus3(self, AppFunctions.getCurrentTask3(self, dbFolder))
            self.ui.WeightEnter3.setReadOnly(False)
            self.ui.addTable3Btn.setVisible(False)
            self.ui.closeTable3Btn.setVisible(True)
            self.ui.addPos3Btn.setVisible(True)           
            self.ui.tableWidget3.clearContents()
            
        else:
            print("Could not insert shift data")           
            
            # load new user from DB to table view
            AppFunctions.displayTask3(self, AppFunctions.getCurrentTask3(self, dbFolder))
            AppFunctions.getTaskStatus3(self, AppFunctions.getCurrentTask3(self, dbFolder))


    

    """
    #5. add last task to TaskTable
    def addTaskToTaskTable(self, dbFolder):
        pass        

    """

    #6. add new position to OneTaskPosition1.
    def addNewPosition3(self, dbFolder):

        global sumWeight3, sumLength3
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        weight = self.ui.WeightEnter3.text()        
        worker = self.ui.comboBox_workerEnter3.currentText()
        
        
        sumWeight3 += float(weight)
        sumL3 = AppFunctions.numInPack3 * AppFunctions.lengthTask3
        sumLength3 += sumL3
    
        
        
        # create sql statement
        insert_position_data_sql = f"""
        INSERT INTO OneTaskPosition3(ID_TASK, DATE, TIME, WEIGHT, WORKER) VALUES ('{AppFunctions.idTask3}', CURRENT_DATE, CURRENT_TIME, '{weight}', '{worker}');
        """

        insert_last_position_to_global = f"""
        INSERT INTO AllPositions (ID_TASK, ID_POSITION, DATE, TIME, WEIGHT, WORKER) SELECT ID_TASK, ID_POSITION, DATE, TIME, WEIGHT, WORKER FROM OneTaskPosition3 ORDER BY ROWID DESC LIMIT 1;
        """
        
        insert_sum_to_task = f"""
        UPDATE TaskTable SET SUM_WEIGHT = ('{sumWeight3}'), SUM_LENGTH = ('{sumLength3}') WHERE TASK_ID = ('{AppFunctions.idTask3}') ;
        """
        
        if conn is not None:
            # create user table
            conn.cursor().execute(insert_position_data_sql)
            conn.cursor().execute(insert_last_position_to_global)        
            conn.cursor().execute(insert_sum_to_task)
            conn.commit()
            # clear form input
            AppFunctions.displayPositions3(self, AppFunctions.getCurrentPosition3(self, dbFolder))
            
        else:
            print("Could not insert position data")
                        
            # load new user from DB to table view
            AppFunctions.displayPositions3(self, AppFunctions.getCurrentPosition3(self, dbFolder))

        self.ui.WeightEnter3.setText("")



    """
    #7. add last new position from OneTaskPosition1 to AllPosition table.
    def addPostionToAllPositionsTable(self, dbFolder):
        pass
    """
    
    #8. display all positons of current task
    def displayPositions3(self, rows):

        global sumWeight3, sumLength3
        
        self.ui.SumLength_Show3.setText(str(round(sumLength3, 2)))
        self.ui.SumWeight_Show3.setText(str(round(sumWeight3, 2)))

        for row in rows:
            # get number of rows
            rowPosition = self.ui.tableWidget3.rowCount()
            print("3.")
            print("rowPosition = ", rowPosition)
            print("row", row)

            # skip rows that have alreade been loaded to table
            if rowPosition + 1 > row[0]:
                print('ahtung')
                continue
            
            itemCount = 0
            # create new table row
            self.ui.tableWidget3.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget3.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # add items to row
            for item in row:
                write_flag = 0
                print(itemCount, item)
                
                if itemCount == 0:
                    itemPosition = itemCount
                    self.ui.CountPack_Show3.setText(str(item))
                    self.ui.Count_Show3.setText(str(item * AppFunctions.numInPack3))
                    write_flag = 1
                    print('sos', item, item*AppFunctions.numInPack3)
                    
                elif itemCount == 3:
                    itemPosition = 1
                    write_flag = 1
                    
                elif itemCount == 4:
                    itemPosition = 2
                    write_flag = 1
                    
                elif itemCount == 5:
                    itemPosition = 3
                    write_flag = 1
                if write_flag:
                    self.qtablewidgetitem = QTableWidgetItem()
                    self.ui.tableWidget3.setItem(rowPosition, itemPosition, self.qtablewidgetitem)
                    self.qtablewidgetitem = self.ui.tableWidget3.item(rowPosition, itemPosition)
                    self.qtablewidgetitem.setText(str(item))
                itemCount = itemCount + 1
                
            rowPosition = rowPosition + 1


    

        


    #10. display current informations of current task:
    def displayTask3(self, row):
        
        itemCount = 0
        self.ui.comboBox_workerEnter3.setEnabled(True)
        # add items to row
        for items in row:
                
            for item in items:
                if itemCount == 0:
                    AppFunctions.idTask3 = item
                    self.ui.TaskNum3.setText(str(item))
                    self.ui.TaskNum3.setReadOnly(True)
                elif itemCount == 4:
                    if str(item) == "1":
                        index_to_select = 0
                    else:
                        index_to_select = 1                
                    self.ui.comboBox3.setCurrentIndex(index_to_select)
                    self.ui.comboBox3.setEnabled(False)
                elif itemCount == 5:
                    self.ui.LengthEnter3.setText(str(item))
                    self.ui.LengthEnter3.setReadOnly(True)
                elif itemCount == 6:
                    self.ui.DiametrEnter3.setText(str(item))
                    self.ui.DiametrEnter3.setReadOnly(True)
                elif itemCount == 8:
                    self.ui.TypeEnter3.setText(str(item))
                    self.ui.TypeEnter3.setReadOnly(True)
                elif itemCount == 7:
                    self.ui.NumPackEnter3.setText(str(item))
                    self.ui.NumPackEnter3.setReadOnly(True) 
                itemCount += 1
        

    #11. get current task information for current table
    def getCurrentTask3(self, dbFolder):        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        get_last_task = f"""
                            SELECT * FROM TaskTable WHERE NUM_TABLE = 3 ORDER BY ROWID DESC LIMIT 1;
                         """
        try:
            c = conn.cursor()
            c.execute(get_last_task)
            # return all table rows
            return c
        except Error as e:
            print(e)

    #12. close task for table1
    def closeTask3(self, dbFolder):

        conn = AppFunctions.create_connection(dbFolder)

        #self.ui.MachineNum1.setText("")
        self.ui.WeightEnter3.setReadOnly(True)
        self.ui.comboBox3.setCurrentIndex(-1)
        self.ui.comboBox3.setEnabled(True)
        self.ui.comboBox_workerEnter3.setCurrentIndex(-1)
        self.ui.comboBox_workerEnter3.setEnabled(False)
        self.ui.WeightEnter3.setText("")
        self.ui.LengthEnter3.setText("")
        self.ui.LengthEnter3.setReadOnly(False)
        self.ui.DiametrEnter3.setText("")
        self.ui.DiametrEnter3.setReadOnly(False)
        self.ui.NumPackEnter3.setText("")
        self.ui.NumPackEnter3.setReadOnly(False)
        self.ui.TypeEnter3.setText("")
        self.ui.TypeEnter3.setReadOnly(False)
        self.ui.TaskNum3.setText("")
        self.ui.TaskNum3.setReadOnly(False)

        self.ui.SumWeight_Show3.setText("")
        self.ui.SumLength_Show3.setText("")
        self.ui.Count_Show3.setText("")
        self.ui.CountPack_Show3.setText("")

        self.ui.addTable3Btn.setVisible(True)
        self.ui.closeTable3Btn.setVisible(False)
        self.ui.addPos3Btn.setVisible(False)

        self.ui.tableWidget3.clearContents()
        self.ui.tableWidget3.setRowCount(0)



        insert_task_close_marker = f"""
        UPDATE TaskTable SET CLOSED = ('{1}') WHERE TASK_ID = ('{AppFunctions.idTask3}') ;
        """

        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_close_marker)
            conn.commit()           
        else:
            print("Could not insert shift data")           


    #13. get closed_status task for table 1
    def getTaskStatus3(self, row):
        global sumWeight3, sumLength3
        for items in row:
            AppFunctions.taskStatus3 = items[11]
            AppFunctions.idTask3 = items[0]
            AppFunctions.numInPack3 = items[7]
            AppFunctions.lengthTask3 = items[5]
            sumWeight3 = items[9]
            sumLength3 = items[10]


    #14. get current postition information for current table
    def getCurrentPosition3(self, dbFolder):        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        get_positions = """
                            SELECT * FROM OneTaskPosition3;
                        """
        try:
            c = conn.cursor()
            c.execute(get_positions)
            # return all table rows
            return c
        except Error as e:
            print(e)
            








