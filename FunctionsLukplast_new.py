## IMPORTS

import os
import sys

# Import SQLite
import sqlite3
from sqlite3 import Error


# Import QtableWidgetItem (for creating new table cells)
from PySide2.QtWidgets import QTableWidgetItem


# Function class
class AppFunctions():

   
    """docstring for AppFunctions"""

    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg
        self.idShift = 0
        self.idTask1 = 0
        self.taskStatus1 = 0


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
                                          WORKER,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (TASK_ID)                                            

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
        conn = AppFunctions.create_connection(dbFolder)

        # create tables
        if conn is not None:
            # create user table
            AppFunctions.create_table(conn, create_ShiftTable)
            AppFunctions.create_table(conn, create_TaskTable)
            AppFunctions.create_table(conn, create_AllPositions)
            AppFunctions.create_table(conn, create_OneTaskPosition1)
            
        else:
            print('Error! Cannot create the database connection')


        


      
    #1 create new shift
    def addNewShift(self, dbFolder):

        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        shift = self.ui.shiftEnter.text()
        master = self.ui.masterEnter.text()
        lyb_1 = self.ui.lay1Enter.text()
        lyb_2 = self.ui.lay2Enter.text()
        lyb_3 = self.ui.lay3Enter.text()
        
        # create sql statement
        insert_shift_data_sql = f"""
        INSERT INTO ShiftTable (DATE, TIME, SHIFT, MASTER, LYB_1, LYB_2, LYB_3) VALUES (CURRENT_DATE, CURRENT_TIME, '{shift}', '{master}', '{lyb_1}', '{lyb_2}', '{lyb_3}');
        """

      
        
        del_last_shift_data = f"""
        DELETE FROM OneTaskPosition1
        """
        if conn is not None:
            # create user table
            conn.cursor().execute(insert_shift_data_sql)
            conn.cursor().execute(del_last_shift_data)
            conn.commit()
            # clear form input
            self.ui.shiftEnter.setText("")
            self.ui.masterEnter.setText("")
            self.ui.lay1Enter.setText("")
            self.ui.lay2Enter.setText("")
            self.ui.lay3Enter.setText("")
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

        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        
        machine = self.ui.MachineNum1.text()
        length = self.ui.LengthEnter1.text()
        diametr = self.ui.DiametrEnter1.text()
        num_in_pack = self.ui.NumPackEnter1.text()
        type_pype = self.ui.TypeEnter1.text()
        


        # create sql statement        
        insert_task_data_sql = f"""
        INSERT INTO TaskTable (DATE, TIME, ID_SHIFT, MACHINE, LENGTH, DIAMETR, NUM_IN_PACK, TYPE, SUM_WEIGHT, SUM_LENGTH, CLOSED)
        VALUES (CURRENT_DATE, CURRENT_TIME, '{AppFunctions.idShift}', '{machine}', '{length}', '{diametr}', '{num_in_pack}', '{type_pype}', '{0}', '{0}', '{0}');
        """


        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_data_sql)
            conn.commit()
            # clear form input
            self.ui.MachineNum1.setText("")
            self.ui.LengthEnter1.setText("")
            self.ui.DiametrEnter1.setText("")
            self.ui.NumPackEnter1.setText("")
            self.ui.TypeEnter1.setText("")
            AppFunctions.displayTask(self, AppFunctions.getCurrentTask(self, dbFolder))
            AppFunctions.getTaskStatus1(self, AppFunctions.getCurrentTask(self, dbFolder))
            self.ui.addTable1Btn.setVisible(False)
            self.ui.closeTable1Btn.setVisible(True)
            self.ui.addPos1Btn.setVisible(True)
            
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
        
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        weight = self.ui.WeightEnter1.text()
        worker = self.ui.WorkerEnter1.text()
        
        # create sql statement
        insert_position_data_sql = f"""
        INSERT INTO OneTaskPosition1(ID_TASK, DATE, TIME, WEIGHT, WORKER) VALUES ('{AppFunctions.idTask1}', CURRENT_DATE, CURRENT_TIME, '{weight}', '{worker}');
        """
        
        if conn is not None:
            # create user table
            conn.cursor().execute(insert_position_data_sql)
            conn.commit()
            # clear form input
            self.ui.WeightEnter1.setText("")
            self.ui.WorkerEnter1.setText("")
            AppFunctions.displayPositions(self, AppFunctions.getCurrentPosition(self, dbFolder))
            
        else:
            print("Could not insert position data")
                        
            # load new user from DB to table view
            AppFunctions.displayPositions(self, AppFunctions.getCurrentPosition(self, dbFolder))





    
    #7. add last new position from OneTaskPosition1 to AllPosition table.
    def addPostionToAllPositionsTable(self, dbFolder):
        pass

    
    #8. display all positons of current task
    def displayPositions(self, rows):

        for row in rows:
            # get number of rows
            rowPosition = self.ui.tableWidget.rowCount()

            # skip rows that have alreade been loaded to table
            if rowPosition + 1 > row[0]:
                continue
            
            itemCount = 0
            # create new table row
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # add items to row
            for item in row:
                write_flag = 0
                
                if itemCount == 0:
                    itemPosition = itemCount
                    write_flag = 1
                    
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
                    print(itemCount, item, itemPosition)

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
                elif itemCount == 5:
                    self.ui.worker1Show.setText(item)
                elif itemCount == 6:
                    self.ui.worker2Show.setText(item)
                elif itemCount == 7:
                    self.ui.worker3Show.setText(item)                 
                itemCount += 1
        


    #10. display current informations of current task:
    def displayTask(self, row):
        
        itemCount = 0
        # add items to row
        for items in row:
                
            for item in items:
                if itemCount == 0:
                    AppFunctions.idTask1 = item
                    self.ui.TaskNum1.setText(str(item))
                    self.ui.TaskNum1.setReadOnly(True)
                elif itemCount == 4:
                    self.ui.MachineNum1.setText(str(item))
                    self.ui.MachineNum1.setReadOnly(True)
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
        get_last_task = """
                            SELECT * FROM TaskTable ORDER BY ROWID DESC LIMIT 1;
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

        self.ui.MachineNum1.setText("")
        self.ui.MachineNum1.setReadOnly(False)
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

        self.ui.addTable1Btn.setVisible(True)
        self.ui.closeTable1Btn.setVisible(False)
        self.ui.addPos1Btn.setVisible(False)



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
        for items in row:
            AppFunctions.taskStatus1 = items[11]
            AppFunctions.idTask1 = items[0]


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
            
        

        
        
        
    
