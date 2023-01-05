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

apl = ApplicationLogic()

root = tk.Tk()
root.title("New Category")
root.geometry("330x210")
root.resizable(width=False, height=False)   # Frame size manipulation


def aggregateData():
    """Aggregate Data

    Description:
        This method collects data entered by the user from the gui widgets,
        checks for invalid entries and if any, display the error message in
        red text in the title label on the gui. It then invokes a method
        in the backend module (applogic mofule) and passes the collected data
        to it to be saved to the database
    
    """
    
    catType = comboType.get()
    catName = txtName.get()
    catDetails = txtDetails.get("1.0", tk.END)

    save = apl.saveCategoryData(catType, catName, catDetails)
    if save == 0:
        print("[.] Data saved!")

def messages(msg):
    """Display Messages

    Description:
        This method, when invoked takes a message via its parameter
        and displays the text in red
    
    Args:
        msg (str): the message to be displayed to the user

    """

def close():
    """Function to close the gui frame"""

    print("[X] Application closed")
    root.destroy()


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

btnSave = tk.Button(root, text=" Save ", command=aggregateData)
btnSave.grid(row=4, column=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

root.mainloop()
