""" =======================     MYWALLET APPLICATION     ===================================
    FILE:           MYWALLET DATABASE CLASS
    DATE CREATED:   29-Dec-2022
    LAST UPDATED:   09-JAN-2023
    DEVELOPER:      EMMANUEL ENCHILL

    DESCRIPTION:    THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND THE DATA ENTRY CLASS THAT INTERACTS WITH THE USER.
"""

#!/usr/bin/python3

import sqlite3

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
    

    def _commitcategory(self, _category_name, _category_type, _details):
        """Save Record

        Description:
            Commit the category record to the database

        Arguments:
            _category_type (str): the category type
            _category_name (str): the name of the category
            _details (str): a description of the category

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO categories (category_type, category_name, details) VALUES (?, ?, ?)"
            data_tuple = (_category_type, _category_name, _details)
            cursor.execute(query, data_tuple)
            conn.commit()

            if (conn):
                return 0

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def _commitincome(self, _income_date, _income_type, _income_amount, _income_details):
        """Save Income Record

        Description:
            This method commits records of new incomes to the database

        Args:
            _income_date (date): the current date for income receipt
            _income_type (str): the type of income
            _income_amount (float/int): the amount of income
            _income_details (str): a brief description of the record
        """

        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO income_records (income_date, income_type, income_amount, income_details) VALUES (?, ?, ?, ?)"
            data_tuple = (_income_date, _income_type, _income_amount, _income_details)
            cursor.execute(query, data_tuple)
            conn.commit()

            if (conn):
                return 0
        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def _commitexpense(self, _expense_date, _expense_type, _expense_amount, _expense_details):
        """Save Income Record

        Description:
            This method commits records of new expenses to the database

        Args:
            _expense_date (date): the current date for income receipt
            _expense_type (str): the type of income
            _expense_amount (float/int): the amount of income
            _expense_details (str): a brief description of the record
        """

        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO expense_records (expense_date, expense_type, expense_amount, expense_details) VALUES (?, ?, ?, ?)"
            data_tuple = (_expense_date, _expense_type, _expense_amount, _expense_details)
            cursor.execute(query, data_tuple)
            conn.commit()

            if (conn):
                return 0
        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def _commitransactions(self, _transaction_date, _transaction_type, _transaction_category, _transaction_amount, _transaction_details):
        """Save Income Record

        Description:
            This method commits records of new transactions to the database

        Args:
            _transaction_date (date): the current date for the transaction
            _transaction_type (str): the type of the transaction, either Salary,
            Allowance, Entertainment, or Grocery etc.
            _transaction_category (tr): the category of the transaction, either Incomes
            Expenses
            _transaction_amount (float/int): the amount of involved in the transaction
            _transaction_details (str): a brief description of the transaction
        """

        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO wallet_transactions (transaction_date, transaction_type, transaction_category, transaction_amount, transaction_details) VALUES (?, ?, ?, ?, ?)"
            data_tuple = (_transaction_date, _transaction_type, _transaction_category, _transaction_amount, _transaction_details)
            cursor.execute(query, data_tuple)
            conn.commit()

            if (conn):
                return 0
        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def _get_category_names(self, _category_type):
        """Display Category Records
        
        Description:
            Display all information in the categories table

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT category_name FROM categories WHERE category_type = '"+_category_type+"' "
            cursor.execute(query)
            records = cursor.fetchall()

            return records

        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()


    def _get_category_records(self, _category_type):
            """Display Category Records
            
            Description:
                Display all information in the categories table

            """
            try:
                conn = self.db_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM categories WHERE category_type = '"+_category_type+"' "
                cursor.execute(query)
                records = cursor.fetchall()
                
                return records

            except sqlite3.Error as e:
                print("Failed to fetch records: ", e)
            finally:
                if conn:
                    cursor.close()
                    conn.close()
    

    # def _get_transaction_records(self, _transaction_type):
    #         """Display Category Records
            
    #         Description:
    #             This method fetches records from the transactions table based on the
    #             transaction type indicated by the parameter
            
    #         Args:
    #             _transaction_type (str): the type of transaction, example Incomes, Expenses

    #         """
    #         try:
    #             conn = self.db_connection()
    #             cursor = conn.cursor()
    #             query = "SELECT * FROM wallet_transactions WHERE transaction_type = '"+_transaction_type+"' "
    #             cursor.execute(query)
    #             records = cursor.fetchall()
                
    #             return records

    #         except sqlite3.Error as e:
    #             print("Failed to fetch records: ", e)
    #         finally:
    #             if conn:
    #                 cursor.close()
    #                 conn.close()
    

    # def _get_number_of_records_of_types(self, _tranaction_type):
    #     """Number of records
        
    #     Description:
    #         This method computes for the number of records in a table
    #         specified by the parameter

    #     Args:
    #         _tranaction_type (str): the type of transaction, example Incomes, Expenses
        
    #     Returns:
    #         The total number of records of the specified type
            
    #     """
    #     try:
    #         conn = self.db_connection()
    #         cursor = conn.cursor()
    #         query = "SELECT * FROM wallet_transactions WHERE transaction_type = '"+_tranaction_type+"' "
    #         cursor.execute(query)
    #         records = cursor.fetchall()

    #         _sum = len(records)

    #         return _sum
            
    #     except sqlite3.Error as e:
    #         print("Failed to fetch records: ", e)
    #     finally:
    #         if conn:
    #             cursor.close()
    #             conn.close()
    

    # def _get_sum_of_amounts_of_types(self, _tranaction_type):
    #     """Number of records
        
    #     Description:
    #         This method computes for the sum of amounts from the transactions table
    #         where the type of transaction is specified by the parameter

    #     Args:
    #         _tranaction_type (str): the type of transaction, example Incomes, Expenses
        
    #     Returns:
    #         The sum of amounts for the transactions for the specified type
            
    #     """
    #     try:
    #         conn = self.db_connection()
    #         cursor = conn.cursor()
    #         query = "SELECT SUM(transaction_amount) FROM wallet_transactions WHERE transaction_type = '"+_tranaction_type+"' "
    #         cursor.execute(query)
    #         records = cursor.fetchall()

    #         # total = sum(records)

    #         return records
            
    #     except sqlite3.Error as e:
    #         print("Failed to fetch records: ", e)
    #     finally:
    #         if conn:
    #             cursor.close()
    #             conn.close()
    

    # def _get_number_of_records_of_categories(self, _category_type):
    #     """Number of records
        
    #     Description:
    #         This method computes for the number of records in a table
    #         specified by the parameter

    #     Args:
    #         _category_type (str): the type of category, example Salary, Gift, Transportation, Grocery
        
    #     Returns:
    #         The total number of records of the specified category
            
    #     """
    #     try:
    #         conn = self.db_connection()
    #         cursor = conn.cursor()
    #         query = "SELECT * FROM wallet_transactions WHERE transaction_category = '"+_category_type+"' "
    #         cursor.execute(query)
    #         records = cursor.fetchall()

    #         _sum = len(records)

    #         return _sum
            
    #     except sqlite3.Error as e:
    #         print("Failed to fetch records: ", e)
    #     finally:
    #         if conn:
    #             cursor.close()
    #             conn.close()
    

    # def _get_sum_of_amounts_of_categories(self, _category_type):
        # """Number of records
        
        # Description:
        #     This method computes for the sum of amounts from the transactions table
        #     where the type of transaction is specified by the parameter

        # Args:
        #     _category_type (str): the category of transaction, example Salary, Gift, Grocery, Transportation
        
        # Returns:
        #     The sum of amounts for the transactions for the specified category
            
        # """
        # try:
        #     conn = self.db_connection()
        #     cursor = conn.cursor()
        #     query = "SELECT SUM(transaction_amount) FROM wallet_transactions WHERE transaction_category = '"+_category_type+"' "
        #     cursor.execute(query)
        #     records = cursor.fetchall()

        #     # total = sum(records)

        #     return records
            
        # except sqlite3.Error as e:
        #     print("Failed to fetch records: ", e)
        # finally:
        #     if conn:
        #         cursor.close()
        #         conn.close()