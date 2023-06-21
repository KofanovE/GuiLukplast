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
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (ID_TASK)                                            

                                    );
                            """

        create_OneTaskPosition1 = """ CREATE TABLE IF NOT EXISTS OneTaskPosition1(
                                          ID_TASK INTEGER,
                                          ID_POSITION INTEGER PRIMARY KEY AUTOINCREMENT,
                                          DATE TEXT,
                                          TIME TEXT,
                                          WEIGHT,
                                          WORKER,
                                          CONSTRAINT ID_TASK FOREIGN KEY (ID_TASK) REFERENCES TaskTable (ID_TASK)
                                          
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
        INSERT INTO TaskTable (DATE, TIME, ID_SHIFT, MASTER, LYB_1, LYB_2, LYB_3) VALUES (CURRENT_DATE, 
                CURRENT_TIME, '{shift}', '{master}', '{lyb_1}', '{lyb_2}', '{lyb_3}');
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
        INSERT INTO ShiftTable (DATE, TIME, ID_SHIFT, MACHINE, LENGTH, DIAMETR, NUM_IN_PACK, TYPE, SUM_WEIGHT, SUM_LENGTH, CLOSED)
        VALUES (CURRENT_DATE, CURRENT_TIME, '{AppFunctions.idShift}', '{machine}', '{length}', '{diametr}', '{num_in_pack}', '{type_pype}', '{0}', '{0}', , '{0}');
        """

        #!!!!!!!!!!!!!!!!!!
        # I stopped here. Next step - create showing of ID task
        #!!!!!!!!!!!!!!!!!!


        if conn is not None:
            # create user table
            conn.cursor().execute(insert_task_data_sql)
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


    
    #5. add last task to TaskTable
    def addTaskToTaskTable(self, dbFolder):
        pass        
    #6. add new position to OneTaskPosition1.
    def addNewPosition(self, dbFolder):
        pass
    #7. add last new position from OneTaskPosition1 to AllPosition table.
    def addPostionToAllPositionsTable(self, dbFolder):
        pass
    #8. display all positons of current task
    def displayPositions(self, rows):
        pass
    
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
    def displayTask(self, rows):
        pass


    
