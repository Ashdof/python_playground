"""
    Programme:      Game Database Class
    DATE:           04-Nov-2022
    DEVELOPER:      EMMANUEL ENCHILL
    DESCRIPTION:    THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND FRONTEND CLASS THAT INTERACTS WITH THE USER.
"""

#usr/bin/python

import sqlite3
from texttable import Texttable

class gamedbmanager:

    def __init__(self, db_path):
        """Initialise the class with the path to the database file
        
        db_path     Path to the database file
        """
        self._db_path = db_path
  

    def db_connection(self):
        """Database Connection
        
        Create a connection to the database 
        """
        try:
            conn = sqlite3.connect(self._db_path)
            return conn
        except sqlite3.Error as e:
            print("Failed to connect: ", e)


    def create_table(self):
        """Create Table in database file"""
        try:
            conn = self.db_connection()
            query = '''CREATE TABLE IF NOT EXISTS gamerecords(
                id INTEGER NOT NULL,
                curdate TEXT NOT NULL,
                rounds INTEGER NOT NULL,
                score NUMBER NOT NULL,
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
    

    def save_record(self, _date, _rounds, _score):
        """Save Record

        Commit the record to the database
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO gamerecords (curdate, rounds, score) VALUES (?, ?, ?)"
            data_tuple = (_date, _rounds, _score)
            cursor.execute(query, data_tuple)

            conn.commit()
            cursor.close()

            print("Record saved!")

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                conn.close()
    

    def display_detail_records(self):
        """Display Records
        
        Display all information in the specified table 
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM gamerecords"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Game Number", "Date", "Game Stage", "Total Score"])
            table.set_cols_dtype(['t', 't', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2], record[3]])

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                conn.close()
    

    def get_number_of_records(self):
        """Number of records
        
        Get the number of records in the table
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM gamerecords"
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