"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   08-JAN-2023
    LAST UPDATED:           08-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE RECORDS GUI.

"""

#!/usr/bin/python3

from PIL import Image, ImageTk
import tkinter as tk

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

apl = ApplicationLogic() 

class DisplayRecords(tk.Frame):

    def __init__(self):
        super().__init__()


    def _closeWindow(self):
        self.quit()
    

    def _guiWidgets(self):
        pass


def main():
    frmRecords = tk.Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    records = DisplayRecords()

    frmRecords.mainloop()


if __name__ == '__main__':

    main()