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

#   =============================     GUI LAYOUT      ==================================

#   LABELS

lblTitle = tk.Label(frmRecords, text="View list of categories and transactions")
lblTitle.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

lblSummary = tk.Label(frmRecords, text="Total records found: ")
lblSummary.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)

lblSummaryAmount = tk.Label(frmRecords, text=" 0 ") # invoke summary amount function here
lblSummaryAmount.grid(row=3, column=1, padx=2, pady=2, sticky=tk.W)



frmRecords.mainloop()