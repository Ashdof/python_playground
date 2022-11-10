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
    
    def save_record(self, _date, _score):
        """Save Record

        Commit the record to the database table
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO gamerecords (currentdate, score) VALUES (?, ?)"
            data_tuple = (_date, _score)
            cursor.execute(query, data_tuple)

            conn.commit()
            cursor.close()
            
            qty = conn.total_changes
            if qty < 1:
                return 1
            else:
                return qty

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                conn.close()