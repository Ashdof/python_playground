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
            catecode = input("\n\tCategory code: ")

            if catecode in faults:
                print("\t{} is allowed".format(catecode))

            elif catecode == "":
                print("\tSave category mode cancelled")
                done = True
                break
            else:
                catename = input("\tCategory name: ")

                if catename == "" or catename == " ":
                    print("\tBlanks not allowed for category names")
                
                record._commitcategory(catecode, catename)
                print("\t{} category saved".format(catename))
                
                print("\t____________________________________________")
                done = True
    

    def _getrecords(self):
        """Display Records

        Description:
            This method presents the user with options from which records can be display
        
        """
        
        done = False

        print("\n\tSelect the number for a corresponding record to display\n")
        print("\t1: Categories\n\t2: Income List\n\t3: Income Summary\n\t4: Expense List\n\t5. Expense Summary ")
        
        while not done:
            val = input("\n\tNumber ?>: ")

            if val == "":
                print("\tDisplay process cancelled")
                done = True
                
            else:
                match val:
                    case "1":
                        record.display_list_records()
                        done = True

                    # case "2":
                    #     record.display_names_and_codes()
                    #     done = True

                    # case "3":
                    #     record.display_names_prof_contacts()
                    #     done = True

                    # case "4":
                    #     record.display_names_and_numbers()
                    #     done = True

                    # case "5":
                    #     record.display_names_email_addresses()
                    #     done = True