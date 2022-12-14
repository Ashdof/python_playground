"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   APPLICATION LOGIC
    DATE:                   02-JAN-2023
    LAST UPDATED:           06-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE APPLICATION LOGIC THAT INTERRACTS WITH AND REGULATES THE FLOW OF 
                            COMMUNICATION BETWEEN THE MODULES WITH GUIs, AND THE DATABASE FILE

"""

#!/usr/bin/python3

from dbclass import Walletdbmanager


# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

class ApplicationLogic:
    """Application Logic Class
    
    Description:
        The methods in this class are the backend logic of the application
    """

    def __init__(self):
       pass

    def getCategoryNames(self, type_of_category):
        """Get records

        Description:
            This method creates a list with the elements received from calling
            the display_list_records function from the database file
        
        Returns:
            A lists of element created with the names received
        """

        data = []
        records = db._get_category_names(type_of_category)
        for record in records:
            data.append(record)
        
        return data

    def saveIncomeData(self, _date, _type, _amount, _details):
        """Save New Income Data
        
            Description:
                This method takes data from the income category gui and passes them to the
                dbclass module to be committed to the database
            
            Returns:
                1 on success or 0 if it fails
        """

        print("[.] Save button clicked")
        print()
        print("Income Information:")
        print("Date: {}\nIncome type: {}\nAmount: {}\nIncome details: {}".format(_date, _type, _amount, _details))
        print()
        print("[.] This is just a placeholder to test this function")

        return 0
    

    def saveCategoryData(self, categoryType, categoryName, categoryDetails):
        """Save New Category Data
        
            Description:
                This method takes data from the new category gui and passes them to the
                dbclass module to be committed to the database
            
            Returns:
                1 on success or 0 if it fails
        """

        print("[.] Save button clicked")
        print()
        print("Category Information:")
        print("Category type: {}\nCategory name: {}\nCategory details: {}".format(categoryType, categoryName, categoryDetails))
        print()
        print("[.] This is just a placeholder to test the save category data function")

        return 0