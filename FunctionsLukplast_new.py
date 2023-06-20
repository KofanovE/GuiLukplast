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
        shift = self.ui.shift.text()
        master = self.ui.master.text()
        lyb_1 = self.ui.lyb_1.text()
        lyb_2 = self.ui.lyb_2.text()
        lyb_3 = self.ui.lyb_3.text()

        # create sql statement
        insert_shift_data_sql = f"""
        INSERT INTO ShiftTable (DATE, TIME, SHIFT, MASTER, LYB_1, LYB_2, LYB_3) VALUES (CURRENT_DATE, 
                CURRENT_TIME, '{shift}', '{master}', '{lyb_1}', '{lyb_2}', '{lyb_3}');
        """

        # execute sql statement
        if not conn.cursor().execute(insert_shift_data_sql):
            print("Could not insert shift data")
        else:
            conn.commit()
            # clear form input
            self.ui.shiftEnter.setText("")
            self.ui.masterEnter.setText("")
            self.ui.lay1Enter.setText("")
            self.ui.lay1Enter.setText("")
            self.ui.lay1Enter.setText("")
            # load new user from DB to table view
            AppFunctions.displayShift(self, AppFunctions.getCurrentShift(dbFolder))


    
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
        

    
    #3. if there is a OneTaskPosition1 table - all data delete
    def delLastShiftInfo(self, dbFolder):
        pass
    #4. add new task of corect shift to OneTaskPosition1
    def addNewTask(self, dbFolder):
        pass
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
        for item in row:
            print("!!!" + itemCount)
            print(item)
            itemCount += 1
        


    #10. display current informations of current task:
    def displayTask(self, rows):
        pass


    
