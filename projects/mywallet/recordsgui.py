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
frmRecords.resizable(width=False, height=False)   # Frame size manipulation

frmRecords.grid_rowconfigure(1, weight=1)
frmRecords.grid_columnconfigure(0, weight=1)


def displayRecords():
    cmbSelect = cmbRecords.get()
    if cmbSelect == "Income Categories":
        type = "Income"
    elif cmbSelect == "Expense Categories":
        type = "Expense"

    income_cats = apl.getCategoryRecords(type)
    
    i = 0
    while i < len(income_cats):
        tblRecords.insert(parent='', index='end', iid=None, text='', values=(i,income_cats[i]))
        i += 1


#   =============================     GUI LAYOUT      ==================================

#   LABELS

lblTitle = tk.Label(frmRecords, text="View list of categories and transactions")
lblTitle.grid(row=0, column=0, columnspan=10, padx=2, pady=2, sticky=tk.W)

lblSummary = tk.Label(frmRecords, text="Total records found: ")
lblSummary.grid(row=20, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

lblSummaryAmount = tk.Label(frmRecords, text=" 0 ") # invoke summary amount function here
lblSummaryAmount.grid(row=20, column=3, padx=2, pady=2, sticky=tk.W)

#   OTHER WIDGETS

cat_list = ["Income Categories", "Expense Categories", "Income Transactions", "Expense Transactions"]

cmbRecords = ttk.Combobox(frmRecords, value=cat_list, width=70)
cmbRecords.set("Select record to display")
cmbRecords.grid(row=1, column=0, columnspan=7, padx=2, pady=2, sticky=tk.W)

btnGetRecords = tk.Button(frmRecords, text=" Get Records ", command=displayRecords)
btnGetRecords.grid(row=1, column=8, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

# , yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set

tblRecords = ttk.Treeview(frmRecords)
tblRecords.grid(row=2, column=0, rowspan=18, columnspan=10, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

tblRecords["columns"] = ["id", "category", "amount", "details"]

# format our column
tblRecords.column("#0", width=0,  stretch=tk.NO)
tblRecords.column("id", anchor=tk.W, width=10)
tblRecords.column("category", anchor=tk.W, width=30)
tblRecords.column("amount", anchor=tk.W, width=30)
tblRecords.column("details", anchor=tk.W, width=120)

#Create Headings 
tblRecords.heading("#0", text="", anchor=tk.W)
tblRecords.heading("id", text="Id", anchor=tk.W)
tblRecords.heading("category", text="Category", anchor=tk.W)
tblRecords.heading("amount", text="Amount", anchor=tk.W)
tblRecords.heading("details", text="Details", anchor=tk.W)



# tblRecords.insert(parent='',index='end',iid=0,text='', values=('1','Ninja','101','Oklahoma', 'Moore'))

frmRecords.mainloop()