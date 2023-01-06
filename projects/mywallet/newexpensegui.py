"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   NEW EXPENSE GUI
    DATE:                   06-JAN-2023
    LAST UPDATED:           06-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE NEW EXPENSE REGISTRY GUI.

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


root = tk.Tk()
root.title("New Expense")
root.geometry("350x260")
root.resizable(width=False, height=False)   # Frame size manipulation

def displayMessages(msg_value):
    """Display Messages

    Description:
        This method, when invoked takes a value via its parameter
        and displays a message. The parameter is a number which will
        determine the message to display.
        
        It creates a new label and based on the message be displayed
        color codes the message and adds the new label to the gui grid
        just below the button widgets
    
    Args:
        msg_value (int): an integer value that determines the message to
        to be displayed

    """
    saved = "Record saved!"
    error = "Record could not be saved"
    wrong_type = "Category is not selected"
    blank_amount = "Amount cannot be blank"
    type_error = "Amount cannot be letters"
    blank_details = "Expense description cannot be blank"

    lblMsg = tk.Label(root)

    match msg_value:

        case 1:
            lblMsg["text"] = saved
            lblMsg["fg"] = "green"
            
        case 2:
            lblMsg["text"] = error
            lblMsg["fg"] = "red"

        case 3:
            lblMsg["text"] = wrong_type
            lblMsg["fg"] = "red"

        case 4:
            lblMsg["text"] = blank_amount
            lblMsg["fg"] = "red"
        
        case 5:
            lblMsg["text"] = type_error
            lblMsg["fg"] = "red"
        
        case 6:
            lblMsg["text"] = blank_details
            lblMsg["fg"] = "red"

    lblMsg.grid(row=6, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)


def aggregateExpenseData():
    """Aggregate Income Data

    Description:
        This method collects data entered by the user from the gui widgets,
        checks for invalid entries and if any, invokes the displayMessages()
        method and passes an integer coded value to it which will determine the
        message and its color to be displayed
        
        It then invokes a method in the backend module (applogic module) and
        passes the collected data to it to be saved to the database. The fate
        of whether the data was successfully saved or not will depend on the
        return value from the method invoked from the applogic module
    
    """
    saved, error, wrong_type, blank_amount, type_error, blank_details, = 1, 2, 3, 4, 5, 6

    _expenseDate = calDate.get()
    _expenseType = comboType.get()
    _expenseAmount = txtAmount.get()
    _expenseDetails = txtDetails.get("1.0", tk.END)

    if _expenseType == "Select income type":
        displayMessages(wrong_type)

    elif _expenseAmount == "":
        displayMessages(blank_amount)
    
    # elif type(_incomeAmount) not in (int, float):
    #     displayMessages(type_error)
        
    elif str(_expenseDetails).isspace():
        displayMessages(blank_details)

    else:

        save = db._commitexpense(_expenseDate, _expenseType, _expenseAmount, _expenseDetails)
        if save == 0:
            displayMessages(saved)
        else:
            displayMessages(error)


def close():
    """Function to exit the gui"""
    print("[X] Application closed")
    root.destroy()


#   =============================     GUI LAYOUT      ==================================

#   LABELS
lblTitle = tk.Label(root, text="Record new expense")
lblTitle.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

lblDate= tk.Label(root, text="Date: ")
lblDate.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)

lblCategory = tk.Label(root, text="Category: ")
lblCategory.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)

lblAmount = tk.Label(root, text="Amount: ")
lblAmount.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)

lblDetails = tk.Label(root, text="Details: ")
lblDetails.grid(row=4, column=0, padx=2, pady=2, sticky=tk.NW)

#   ENTRIES

calDate = DateEntry(width=30, background='darkblue', foreground='white', borderwidth=1, set="Select date")
calDate.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)

comboType = ttk.Combobox(root, value=apl.getCategoryRecords("Expense"), width=30) 
comboType.set("Select expense type")
comboType.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)

txtAmount = tk.Entry(root, width=30)
txtAmount.insert(0, 0.00)
txtAmount.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

txtDetails = tk.Text(root, width=30, height=5)
txtDetails.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

#   BUTTONS

btnCancel = tk.Button(root, text=" Cancel ", command=close)
btnCancel.grid(row=5, column=1, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

btnSave = tk.Button(root, text=" Save ", command=aggregateExpenseData)
btnSave.grid(row=5, column=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

root.mainloop()