"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   APPLICATION LOGIC
    DATE:                   02-JAN-2023
    LAST UPDATED:           02-JAN-2023
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

    def getrecords(self):
        """Get records

        Description:
            This method creates a list with the elements received from calling
            the display_list_records function from the database file
        
        Returns:
            A lists of element created with the names received
        """

        data = []
        records = db.display_list_records() 
        for record in records:
            data.append(record)
        
        return data