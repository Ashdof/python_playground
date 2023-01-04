"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   NEW CATEGORY GUI
    DATE:                   02-JAN-2023
    LAST UPDATED:           03-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE NEW CATEGORY REGISTRY GUI.

"""

#!/usr/bin/python3
# from tkinter import tkinter as tk
import tkinter as tk
from tkinter import ttk

from applogic import ApplicationLogic

apl = ApplicationLogic()



root = tk.Tk()
root.title("New Category")
root.geometry("330x210")
root.resizable(width=False, height=False)   # Frame size manipulation

def saveData():
    
    catType = comboType.get()
    catName = txtName.get()
    catDetails = txtDetails.get()

    save = apl.saveCategoryData(catType, catName, catDetails)
    if save == 0:
        print("[.] Data saved!")

def main():
    """Main method

    Description"
        All the widgets and their layout on the graphical user interface are
        defined in this method. All other methods which perform other related tasks
        are also invoked in this method. Invoking this method therefore displays the
        gui on the screen
        
    """

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

    btnSave = tk.Button(root, text=" Save ", command=saveData)
    btnSave.grid(row=4, column=2, padx=2, pady=2, sticky=tk.N+tk.S+tk.W+tk.E)

    root.mainloop()



def close():
    """Function to close the gui frame"""
    print("[X] Application closed")
    root.destroy()


if __name__ == '__main__':

    main()