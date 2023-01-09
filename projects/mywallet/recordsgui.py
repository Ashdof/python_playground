"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   07-JAN-2023
    LAST UPDATED:           09-JAN-2023
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


frmRecords = tk.Tk()
frmRecords.title("Records Display")
frmRecords.geometry("710x420")
frmRecords.resizable(width=False, height=False)   # Frame size manipulation

frmRecords.grid_rowconfigure(1, weight=1)
frmRecords.grid_columnconfigure(0, weight=1)


def displayRecords():
    """Display Records

    Description:
        This method invokes other methods to display various types of records
        on the gui. The type of record to display is determined by the selected
        item from the combobox widget
        
    """
    cmbSelect = cmbRecords.get()

    match (cmbSelect):
        case "Income Categories":
            displayCategories(type="Income")

        case "Expense Categories":
            displayCategories(type="Expense")

        case "Income Transactions":
            displayTransactions("Incomes")

        case "Expense Transactions":
            displayTransactions("Expenses")


def displayCategories(type):
    """Display Records of Categories

    Description:
        This method displays records of categories from the database according to
        a specified type. It creates a treeview widget, populates it with the data
        and when invoked, adds the table view to the grid frame on the gui.
    
    Args:
        type (str): the type of categoyr records to display, example: Income, Expense

    """
    # _count = db._get_number_of_records_of_categories(type)
    # _sum = db._get_sum_of_amounts_of_categories(type)

    # lbSummary = tk.Label(frmRecords, text="Count: {}\t\tRecords: {}\t\tTotal: {}".format(_count, type, _sum), fg="green")
    # lbSummary.config(font=("Courier", 11))
    # lbSummary.grid(row=22, column=0, columnspan=12, padx=5, pady=2, sticky=tk.W)

    tblCategoryRecords = ttk.Treeview(frmRecords)
    tblCategoryRecords.grid(row=2, column=0, rowspan=20, columnspan=12, padx=5, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)
    
    tblCategoryRecords["columns"] = ["id", "category", "cat_name", "details"]

    # format our column
    tblCategoryRecords.column("#0", width=0,  stretch=tk.NO)
    tblCategoryRecords.column("id", anchor=tk.W, width=10)
    tblCategoryRecords.column("category", anchor=tk.W, width=30)
    tblCategoryRecords.column("cat_name", anchor=tk.W, width=30)
    tblCategoryRecords.column("details", anchor=tk.W, width=120)

    #Create Headings 
    tblCategoryRecords.heading("#0", text="", anchor=tk.W)
    tblCategoryRecords.heading("id", text="Id", anchor=tk.W)
    tblCategoryRecords.heading("category", text="Category Type", anchor=tk.W)
    tblCategoryRecords.heading("cat_name", text="Category Name", anchor=tk.W)
    tblCategoryRecords.heading("details", text="Category Details", anchor=tk.W)

    _cats = db._get_category_records(type)

    for row in _cats:
        tblCategoryRecords.insert(parent='', index='end', iid=None, text='', values=row)


def displayTransactions(transaction_type):
    """Display Records of Categories

    Description:
        This method displays records of categories from the database according to
        a specified type. It creates a treeview widget, populates it with the data
        and when invoked, adds the table view to the grid frame on the gui.
    
    Args:
        type (str): the type of categoyr records to display, example: Income, Expense

    """
    # _count = db._get_number_of_records_of_types(transaction_type)
    # _sum = db._get_sum_of_amounts_of_types(transaction_type)

    # lbSummary = tk.Label(frmRecords, text="Count: {}\t\tRecords: {}\t\tTotal: {}".format(_count, transaction_type, _sum), fg="green")
    # lbSummary.config(font=("Courier", 11))
    # lbSummary.grid(row=22, column=0, columnspan=12, padx=5, pady=2, sticky=tk.W)

    tblCategoryRecords = ttk.Treeview(frmRecords)
    tblCategoryRecords.grid(row=2, column=0, rowspan=20, columnspan=12, padx=5, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)
    
    tblCategoryRecords["columns"] = ["id", "date", "type", "amount", "details"]

    # format our column
    tblCategoryRecords.column("#0", width=0,  stretch=tk.NO)
    tblCategoryRecords.column("id", anchor=tk.W, width=10)
    tblCategoryRecords.column("date", anchor=tk.W, width=30)
    tblCategoryRecords.column("type", anchor=tk.W, width=30)
    tblCategoryRecords.column("amount", anchor=tk.W, width=30)
    tblCategoryRecords.column("details", anchor=tk.W, width=120)

    #Create Headings 
    tblCategoryRecords.heading("#0", text="", anchor=tk.W)
    tblCategoryRecords.heading("id", text="Id", anchor=tk.W)
    tblCategoryRecords.heading("date", text="Date", anchor=tk.W)
    tblCategoryRecords.heading("type", text="Type", anchor=tk.W)
    tblCategoryRecords.heading("amount", text="Amount", anchor=tk.W)
    tblCategoryRecords.heading("details", text="Details", anchor=tk.W)

    _cats = db._get_transaction_records(transaction_type)

    for row in _cats:
        tblCategoryRecords.insert(parent='', index='end', iid=None, text='', values=row)


#   =============================     GUI LAYOUT      ==================================

#   =================   LABELS  
lblTitle = tk.Label(frmRecords, text="View list of categories and transactions")
lblTitle.grid(row=0, column=0, columnspan=10, padx=5, pady=2, sticky=tk.W)

lbSummary = tk.Label(frmRecords, text="Count: {}\t\tRecords: {}\t\tTotal: {}".format(0, " ", 0.0), fg="green")
lbSummary.config(font=("Courier", 11))
lbSummary.grid(row=22, column=0, columnspan=12, padx=5, pady=2, sticky=tk.W)

#   ================    COMBOBOX 
cat_list = ["Income Categories", "Expense Categories"] # , "Income Transactions", "Expense Transactions"

cmbRecords = ttk.Combobox(frmRecords, value=cat_list, width=70)
cmbRecords.set("Select record to display")
cmbRecords.grid(row=1, column=0, columnspan=9, padx=5, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

#   ================    BUTTON
btnGetRecords = tk.Button(frmRecords, text=" Get Records ", command=displayRecords)
btnGetRecords.grid(row=1, column=10, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

#   ===============     TREEVIEW
tblTemp = ttk.Treeview(frmRecords, height=15)
tblTemp.grid(row=2, column=0, rowspan=20, columnspan=12, padx=5, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

frmRecords.mainloop()