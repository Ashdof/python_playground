"""
    =======================     MyWallet APPLICATION     ===================================
    FILE:                   DATA ENTRY CLASS
    DATE:                   29-DEC-2022
    LAST UPDATED:           29-DEC-2022
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE CATEGORIES CLASS

"""

#!/usr/bin/python3

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
    
    