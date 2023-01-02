""" =======================     MYWALLET APPLICATION     ===================================
    FILE:           MYWALLET DATABASE CLASS
    DATE CREATED:   29-Dec-2022
    LAST UPDATED:   29-DEC-2022
    DEVELOPER:      EMMANUEL ENCHILL

    DESCRIPTION:    THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND THE DATA ENTRY CLASS THAT INTERACTS WITH THE USER.
"""

#!/usr/bin/python3

import sqlite3
from texttable import Texttable

class Walletdbmanager:

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
            Commit the category record to the database

        Arguments:
            _code (str): the code for a specified category
            _category_name (str): the name of the category

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO categories (category_code, category_name) VALUES (?, ?)"
            data_tuple = (_code, _category_name)
            cursor.execute(query, data_tuple)

            conn.commit()
            cursor.close()

            # print("Record saved!")

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                conn.close()
    

    def display_list_records(self):
        """Display Category Records
        
        Description:
            Display all information in the categories table

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            # query = "SELECT * FROM categories"
            query = "SELECT category_name FROM categories"
            cursor.execute(query)
            records = cursor.fetchall()
            # cursor.close()

            return records

            # NOTES: 
            # CREATE A SEPARATE CLASS THAT PURPOSEFULLY CREATES A TABLE. 
            # THE METHODS OF THE CLASS SHOULD BE DEDICATED TO A SPECIFIC
            # TABLE, ITS PARAMETER BEING THE NAME OF THE TABLE.
             
            # table = Texttable()
            # table.header(["Number", "Category Code", "Category Name"])
            # table.set_cols_dtype(['t', 't', 't'])

            # for record in records:
            #     table.add_row([record[0], record[1], record[2]])

            # print("\n", table.draw())
            # print("\nNumber of records found: {}".format(self.get_number_of_records("categories")))

            # cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                cursor.close()
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
    

    def get_number_of_records(self, table_name):
        """Number of records
        
        Description:
            Get the number of records in the specified table

        Args:
            table_name (str): name of the table
        
        Returns:
            The total number of records
            
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM '"+table_name+"' "
            cursor.execute(query)
            records = cursor.fetchall()

            total = len(records)

            cursor.close()
            return total
            
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                conn.close()