"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   DATA ENTRY CLASS
    DATE:                   29-DEC-2022
    LAST UPDATED:           29-DEC-2022
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE DATA ENRTY CLASS

"""

#!/usr/bin/python3
import dbclass as db

dbpath = "mywallet.db"
record = db.walletdbmanager(db_path=dbpath)

__line = "_______________________________________"

class NewDataEntry:

    """Record new data
    
    Description:
        The nethods in this class are for recording new data and saving them to the database
    """

    def __init__(self, file_path):
        """Initialise the class with a path to the database file"""
        self.__file_path = file_path
    
    def _getfilepath(self):
        """Return the file path"""

        return self.__file_path
    
    def _savenewcategory(self):
        """Save a new category

        Description:
            This method invokes the _commitcategory() function from the dbclass module to save a new
            category data into the database

        """

        faults = [" ", "@", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")"]
        done = False

        while not done:
            catecode = input("\nCategory code: ")

            if catecode in faults:
                print("{} is allowed".format(catecode))

            elif catecode == "":
                print("Save category mode cancelled")
                done = True
                break
            else:
                catename = input("Category name: ")

                if catename == "" or catename == " ":
                    print("Blanks not allowed for category names")
                
                result = record._commitcategory(catecode, catename)
                if result == 0:
                    print("{} category saved".format(catename))
                else:
                    print("{} category cannot be saved".format(catename))
                
                done = True
                print(__line)