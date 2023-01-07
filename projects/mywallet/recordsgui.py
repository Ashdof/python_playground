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
# from tkcalendar import DateEntry

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")
apl = ApplicationLogic()


frmRecords = tk.Tk()
frmRecords.title("Records Display")
frmRecords.geometry("710x320")
# frmRecords.resizable(width=False, height=False)   # Frame size manipulation

#   =============================     GUI LAYOUT      ==================================

#   LABELS

lblTitle = tk.Label(frmRecords, text="View list of categories and transactions")
lblTitle.grid(row=0, column=0, columnspan=10, padx=2, pady=2, sticky=tk.W)

lblSummary = tk.Label(frmRecords, text="Total records found: ")
lblSummary.grid(row=20, column=0, columnspan=4, padx=2, pady=2, sticky=tk.W)

lblSummaryAmount = tk.Label(frmRecords, text=" 0 ") # invoke summary amount function here
lblSummaryAmount.grid(row=20, column=6, padx=2, pady=2, sticky=tk.W)

#   OTHER WIDGETS

cat_list = ["Income Categories", "Expense Categories", "Income Transactions", "Expense Transactions"]

cmbRecords = ttk.Combobox(frmRecords, value=cat_list, width=70)
cmbRecords.set("Select record to display")
cmbRecords.grid(row=1, column=0, columnspan=7, padx=2, pady=2, sticky=tk.W)

btnGetRecords = tk.Button(frmRecords, text=" Get Records ", command="")
btnGetRecords.grid(row=1, column=8, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

# , yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set

tblRecords = ttk.Treeview(frmRecords)
tblRecords.grid(row=2, column=0, rowspan=18, columnspan=10, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

frmRecords.mainloop()