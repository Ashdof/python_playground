"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   08-JAN-2023
    LAST UPDATED:           08-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE RECORDS GUI.

"""

#!/usr/bin/python3

from PIL import Image, ImageTk
import tkinter as tk

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

apl = ApplicationLogic() 

class DisplayRecords(tk.Frame):
    """Class to model a record displaying graphical user interface"""

    def __init__(self):
        """Initialise the class upon invocation"""
        super().__init__()
        self._guiWidgets()


    def _closeWindow(self):
        """Quit the current active window"""
        self.quit()
    

    def _guiWidgets(self):
        """Define Widgets
        
        Description:
            This method defines the widgets on the form

        """

        #   =================   LABELS  
        lblTitle = tk.Label(self.master, text="View list of categories and transactions")
        lblTitle.grid(row=0, column=0, columnspan=10, padx=2, pady=2, sticky=tk.W)


def main():
    frmRecords = tk.Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    records = DisplayRecords()

    frmRecords.mainloop()


if __name__ == '__main__':

    main()