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
from tkinter import Tk, Frame, Menu, ttk, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED

from dbclass import Walletdbmanager
from applogic import ApplicationLogic

# Pass path to the database file
db = Walletdbmanager("./mywallet.db")

apl = ApplicationLogic() 

class DisplayRecords(Frame):

    def __init__(self):
        super().__init__()
        self._toolBar()
    
    
    def _toolBar(self):
        menubar = Menu(self.master)

        toolBar = Frame(self.master, bd=1, relief=RAISED)

        self.img = Image.open("img/close.png")
        exit_img = ImageTk.PhotoImage(self.img)

        btnExit = Button(toolBar, image=exit_img, relief=FLAT, command=self._closeWindow)
        btnExit.image = exit_img
        btnExit.pack(side = LEFT, padx=2, pady=2)

        toolBar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()



    def _closeWindow(self):
        self.quit()
    

    def _guiWidgets(self):
        pass


def main():
    frmRecords = Tk()
    frmRecords.geometry("800x400")
    frmRecords.title("Records Display")
    frmRecords.resizable(width=False, height=False)   # Frame size manipulation

    records = DisplayRecords()

    frmRecords.mainloop()


if __name__ == '__main__':

    main()