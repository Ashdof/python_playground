"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   07-JAN-2023
    LAST UPDATED:           07-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE RECORDS GUI.

"""

#!/usr/bin/python3


import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")
apl = ApplicationLogic()


frmRecords = tk.Tk()
frmRecords.title("Records Display")
frmRecords.geometry("800x400")
frmRecords.resizable(width=False, height=False)   # Frame size manipulation


frmRecords.mainloop()