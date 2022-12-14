"""
    Programme:      ProNetwork
    DATE:           16TH SEPTEMBER, 2022
    DEVELOPER:      EMMANUEL ENCHILL
    DESCRIPTION:    THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND FRONTEND CLASS THAT INTERACTS WITH THE USER.
"""

#usr/bin/python

import sqlite3
from texttable import Texttable

class prodbmanager:
    
    def __init__(self, db_path):
        """Initialise the class with the path to the database file
        
        db_path     Path to the database file
        """
        self._db_path = db_path
    

    def __init__(self, db_path=""):
        """Initialise the class without any arguments"""
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
            query = '''CREATE TABLE IF NOT EXISTS myprocons(
                id INTEGER PRIMARY KEY AUTO INCREMENT
                lastname TEXT NOT NULL,
                firstname TEXT NOT NULL,
                code TEXT NOT NULL,
                profession TEXT NOT NULL,
                emailaddress TEXT NOT NULL,
                phone TEXT NOT NULL); '''
            
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
    
  
    def save_record(self, _lastname, _firstname, _uniquecode, _profession, _email, _phone_number):
        """Save Record

        Commit the record to the database table
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO myprocons (lastname, firstname, code, profession, emailaddress, phone) VALUES (?, ?, ?, ?, ?, ?)"
            data_tuple = (_lastname, _firstname, _uniquecode, _profession, _email, _phone_number)
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


    def edit_record(self, _lastname, _firstname, _namecode, _profession, _email, _phone_number):
        """Update A Record
        
        Edit a record by the code
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()

            query = "UPDATE myprocons SET lastname = ?, firstname = ?, code = ?, profession = ?, emailaddress = ?, phone = ? WHERE code = ? "
            data = (_lastname, _firstname, _namecode, _profession, _email, _phone_number, _namecode)

            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            
            qty = conn.total_changes
            if qty == 0:
                return 1
            else:
                return 0

            
        except sqlite3.Error as e:
            print("Failed to update record: ", e)

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
            query = "SELECT * FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Code", "Profession", "Email", "Phone number"])
            table.set_cols_dtype(['t', 't', 't', 't', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2], record[3], record[4], record[5]])
                # table.set_deco(Texttable.HEADER)

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                conn.close()
    
    def display_names_and_numbers(self):
        """Display Records
        
        Last name
        First name
        Phone number
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, phone FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Phone number"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])
                table.set_deco(Texttable.HEADER)

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch record: ", e)
        finally:
            if conn:
                conn.close()
    

    def display_names_and_codes(self):
        """Display Records
        
        Last name
        First name
        Code
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, code FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Code"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])
                table.set_deco(Texttable.HEADER)

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch record: ", e) 
        finally:
            if conn:
                conn.close()


    def display_names_prof_contacts(self):
        """Display Records
        
        Last name
        First name
        Profession
        Phone number
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, profession, phone FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Profession", "Phone number"])
            table.set_cols_dtype(['t', 't', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2], record[3]])
                table.set_deco(Texttable.HEADER)

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch record: ", e)
        finally:
            if conn:
                conn.close()

    
    def display_names_email_addresses(self):
        """Display Records

        Last name
        First name
        Email address
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, emailaddress FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Email Address"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])
                table.set_deco(Texttable.HEADER)
            
            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch record: ", e)
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
            query = "SELECT * FROM myprocons"
            cursor.execute(query)
            records = cursor.fetchall()

            total = len(records)

            cursor.close()
            return total
            
        except sqlite3.Error as e:
            print("Failed to fetch record: ", e)
        finally:
            if conn:
                conn.close()


    def delete_record(self, unicode):
        """Delete Record

        Delete a record by the code
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM myprocons WHERE code = ?"
           
            cursor.execute(query, (unicode,))
            conn.commit()
            cursor.close()

            qty = conn.total_changes
            if qty == 0:
                return (1)
            else:
                return (0)

        except sqlite3.Error as e:
            print("Failed to delete record: ", e)
            
        finally:
            if conn:
                conn.close()
    

    def get_codes(self):
        """Select codes from database

        Get a list of all codes from the database
        """
        try:
            uniq_codes = []

            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT code FROM myprocons"

            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                uniq_codes.append(record)
            
            cursor.close()
            
            return uniq_codes
            
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)

        finally:
            if conn:
                conn.close()


    def getfullnames(self):
        """Return the fullnames of all records in the database
        """
        _fullnames = []

        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname FROM myprocons"
            
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                lname = record[0]
                fname = record[1]

                _fullnames.append(lname + " " + fname)
            
            cursor.close()

            return _fullnames
        except sqlite3.Error as e:
            print("Failed to fetch records", e)
        finally:
            if conn:
                conn.close()