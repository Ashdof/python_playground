""" =======================     MY ANAGRAM GAME APPLICATION     ===================================
    FILE:           GAME DATABASE CLASS
    DATE:           04-Nov-2022
    LAST UPDATED:   21-DEC-2022
    DEVELOPER:      EMMANUEL ENCHILL

    DESCRIPTION:    THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND GAME LOGIC CLASS THAT INTERACTS WITH THE USER.
"""

#!/usr/bin/python3

import sqlite3
from texttable import Texttable

class walletdbmanager:

    def __init__(self, db_path):
        """Initialise the class with the path to the database file
        
        Arguments:
            db_path (string):  path to the database file

        """
        self.__db_path = db_path
  

    def db_connection(self):
        """Database Connection
        
        Description:
            Create a connection to the database

        Returns:
            A connection to the database or an sql error if it fails
        """
        try:
            conn = sqlite3.connect(self.__db_path)
            return conn

        except sqlite3.Error as e:
            print("Failed to connect: ", e)


    def create_table(self):
        """Create Table in database file
        
        Descriptn:
            This method creates a table in the database file with the name specified
            by its argument

        Args:
            table_name (str): name of the table to create
        """
        try:
            conn = self.db_connection()
            query = '''CREATE TABLE IF NOT EXISTS categories(
                id INTEGER NOT NULL,
                category_code TEXT NOT NULL,
                category_name TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            ); '''
            
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print("Table creation sucessful.")

            cursor.close()

        except sqlite3.Error as e:
            print("Failed to create table: ", e)

        finally:
            if conn:
                conn.close()
    

    def _commitcategory(self, _code, _category_name):
        """Save Record

        Description:
            Commit the records to the database

        Arguments:
            _date (date): the date for the game play
            _rounds (int): an integer value that represents the game stage
            _score (int): an integer value that represents the score of the game

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO categories (category_code, category_name) VALUES (?, ?)"
            data_tuple = (_code, _category_name)
            cursor.execute(query, data_tuple)

            conn.commit()
            cursor.close()

            print("Record saved!")

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                conn.close()
    

    # def display_detail_records(self):
    #     """Display Records
        
    #     Description:
    #         Display all information in the specified table

    #     """
    #     try:
    #         conn = self.db_connection()
    #         cursor = conn.cursor()
    #         query = "SELECT * FROM gamerecords"
    #         cursor.execute(query)
    #         records = cursor.fetchall()

    #         table = Texttable()
    #         table.header(["Game Number", "Date", "Game Stage", "Total Score"])
    #         table.set_cols_dtype(['t', 't', 't', 't'])

    #         for record in records:
    #             table.add_row([record[0], record[1], record[2], record[3]])

    #         print("\n", table.draw())
    #         print("\nNumber of records found: ", self.get_number_of_records())

    #         cursor.close()
    #     except sqlite3.Error as e:
    #         print("Failed to fetch records: ", e)
    #     finally:
    #         if conn:
    #             conn.close()
    

    # def get_number_of_records(self):
    #     """Number of records
        
    #     Description:
    #         Get the number of records in the table
        
    #     Returns:
    #         The number of records
            
    #     """
    #     try:
    #         conn = self.db_connection()
    #         cursor = conn.cursor()
    #         query = "SELECT * FROM gamerecords"
    #         cursor.execute(query)
    #         records = cursor.fetchall()

    #         total = len(records)

    #         cursor.close()
    #         return total
            
    #     except sqlite3.Error as e:
    #         print("Failed to fetch records: ", e)
    #     finally:
    #         if conn:
    #             conn.close()