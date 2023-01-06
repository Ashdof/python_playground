"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   NEW CATEGORY GUI
    DATE:                   02-JAN-2023
    LAST UPDATED:           05-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE NEW CATEGORY REGISTRY GUI.

"""

#!/usr/bin/python3


import tkinter as tk
from tkinter import ttk

from applogic import ApplicationLogic
from dbclass import Walletdbmanager

apl = ApplicationLogic()
saveCategory = Walletdbmanager("mywallet.db")

root = tk.Tk()
root.title("New Category")
root.geometry("330x230")
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
    blank_text = "Category name cannot be blank"
    blank_combo = "Select a category type"
    blank_area = "Category description cannot be blank"

    lblMsg = tk.Label(root)

    match msg_value:

        case 1:
            lblMsg["text"] = saved
            lblMsg["fg"] = "green"
            
        case 2:
            lblMsg["text"] = error
            lblMsg["fg"] = "red"

        case 3:
            lblMsg["text"] = blank_text
            lblMsg["fg"] = "red"

        case 4:
            lblMsg["text"] = blank_combo
            lblMsg["fg"] = "red"

        case 5:
            lblMsg["text"] = blank_area
            lblMsg["fg"] = "red"

    lblMsg.grid(row=5, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)


def aggregateCategoryData():
    """Aggregate Data

    Description:
        This method collects data entered by the user from the gui widgets,
        checks for invalid entries and if any, invokes the displayMessages()
        method and pass an integer coded value to it which will determine the
        message and its color to be displayed
        
        It then invokes a method in the backend module (applogic module) and
        passes the collected data to it to be saved to the database. The fate
        of whether the data was successfully saved or not will depend on the
        return value from the method invoked from the applogic module
    
    """
    saved, error, blanktext, combo, blankdetails, = 1, 2, 3, 4, 5

    catType = comboType.get()
    catName = txtName.get()
    catDetails = txtDetails.get("1.0", tk.END)

    if catType == "Select category type":
        displayMessages(combo)

    elif catName == "":
        displayMessages(blanktext)
        
    elif str(catDetails).isspace():
        displayMessages(blankdetails)

    else:

        saveCategory._commitcategory(catName, catType, catDetails)
        if saveCategory:
            displayMessages(saved)
            
        else:
            displayMessages(error)


def close():
    """Function to close the gui frame"""

    print("[X] Application closed")
    root.destroy()


#   =============================     GUI LAYOUT      ==================================

#   LABELS
lblTitle = tk.Label(root, text="Create a new category")
lblTitle.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

lblType = tk.Label(root, text="Type: ")
lblType.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)

lblName = tk.Label(root, text="Name: ")
lblName.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)

lblDetails = tk.Label(root, text="Details: ")
lblDetails.grid(row=3, column=0, padx=2, pady=2, sticky=tk.NW)

#   ENTRIES

cat_list = ["Income", "Expense"]

comboType = ttk.Combobox(root, value=cat_list, width=30)
comboType.set("Select category type")
comboType.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)

txtName = tk.Entry(root, width=30)
txtName.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

txtDetails = tk.Text(root, width=30, height=5)
txtDetails.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

#   BUTTONS

btnCancel = tk.Button(root, text=" Cancel ", command=close)
btnCancel.grid(row=4, column=1, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

btnSave = tk.Button(root, text=" Save ", command=aggregateCategoryData)
btnSave.grid(row=4, column=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

root.mainloop()