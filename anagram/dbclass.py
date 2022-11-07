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


    def create_tbl(self):
        """Create Table in database file"""
        try:
            conn = self.db_connection()
            query = '''CREATE TABLE IF NOT EXISTS gamerecords(
                id INTEGER PRIMARY KEY AUTO INCREMENT
                curdate DATE NOT NULL,
                score NUMBER NOT NULL
                ); '''
            
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print("Table creation was sucessful.")

            cursor.close()

        except sqlite3.Error as e:
            print("Failed to create table: ", e)

        finally:
            if conn:
                conn.close()