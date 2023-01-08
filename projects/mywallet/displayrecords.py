"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   08-JAN-2023
    LAST UPDATED:           08-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE RECORDS GUI.

"""

#!/usr/bin/python3


import tkinter as tk
from tkinter import ttk

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

apl = ApplicationLogic() 


def main():
    frmRecords = tk.Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    frmRecords.grid_rowconfigure(1, weight=1)
    frmRecords.grid_columnconfigure(0, weight=1)

    frmRecords.mainloop()


if __name__ == '__main__':

    main()