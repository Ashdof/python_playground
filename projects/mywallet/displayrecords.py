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
from tkinter import ttk

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
        lblTitle.grid(row=0, column=0, columnspan=10, padx=5, pady=2, sticky=tk.W)

        #   ================    COMBOBOX 
        cat_list = ["Income Categories", "Expense Categories", "Income Transactions", "Expense Transactions"]

        cmbRecords = ttk.Combobox(self.master, value=cat_list, width=70)
        cmbRecords.set("Select record to display")
        cmbRecords.grid(row=1, column=0, columnspan=9, padx=5, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

        btnGetRecords = tk.Button(self.master, text=" Get Records ", command="")
        btnGetRecords.grid(row=1, column=10, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)


def main():
    frmRecords = tk.Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    records = DisplayRecords()

    frmRecords.mainloop()


if __name__ == '__main__':

    main()