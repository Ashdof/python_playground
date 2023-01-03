"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   NEW INCOME GUI
    DATE:                   02-JAN-2023
    LAST UPDATED:           02-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE NEW INCOME REGISTRY GUI.

"""

#!/usr/bin/python3


from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")
apl = ApplicationLogic()


root = Tk()
root.title("New Income")
root.geometry("350x240")

def close():
    """Function to exit the gui"""
    print("[X] Application closed")
    root.destroy()

def main():
    """Main method

    Description"
        All the widgets and their layout on the graphical user interface are
        defined in this method. All other methods which perform other related tasks
        are also invoked in this method. Invoking this method therefore displays the
        gui on the screen
        
    """
    
    #   LABELS
    lblTitle = Label(root, text="Record new income")
    lblTitle.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=W)

    lblDate= Label(root, text="Date: ")
    lblDate.grid(row=1, column=0, padx=2, pady=2, sticky=W)

    lblCategory = Label(root, text="Category: ")
    lblCategory.grid(row=2, column=0, padx=2, pady=2, sticky=W)

    lblAmount = Label(root, text="Amount: ")
    lblAmount.grid(row=3, column=0, padx=2, pady=2, sticky=W)

    lblDetails = Label(root, text="Details: ")
    lblDetails.grid(row=4, column=0, padx=2, pady=2, sticky=NW)

    #   ENTRIES

    calDate = DateEntry(width=30, background='darkblue', foreground='white', borderwidth=1)
    calDate.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky=W)

    comboType = ttk.Combobox(root, value=apl.getCategoryRecords(), width=30)
    comboType.set("Select income type")
    comboType.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=W)

    txtAmount = Entry(root, width=30)
    txtAmount.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=N+S+W+E)

    txtDetails = Text(root, width=30, height=5)
    txtDetails.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky=N+S+W+E)

    #   BUTTONS

    btnCancel = Button(root, text=" Cancel ", command=close)
    btnCancel.grid(row=5, column=1, padx=2, pady=2, sticky=N+S+W+E)

    btnSave = Button(root, text=" Save ", command=apl.saveIncomeData)
    btnSave.grid(row=5, column=2, padx=2, pady=2, sticky=N+S+W+E)

    root.mainloop()


if __name__ == '__main__':

    main()