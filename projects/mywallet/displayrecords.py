"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   RECORDS GUI
    DATE:                   08-JAN-2023
    LAST UPDATED:           08-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE RECORDS GUI.

"""

#!/usr/bin/python3


from tkinter import Tk, Frame, Menu, ttk

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

apl = ApplicationLogic() 

class DisplayRecords(Frame):

    def __init__(self):
        super().__init__()
        self._menuBar()
    

    def _menuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label=" Exit ", command=self._closeWindow)
        menubar.add_cascade(label = " File ", menu=fileMenu)
    

    def _closeWindow(self):
        self.quit()


def main():
    frmRecords = Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    records = DisplayRecords()

    frmRecords.mainloop()


if __name__ == '__main__':

    main()