"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   USER INTERFACE CLASS
    DATE:                   29-DEC-2022
    LAST UPDATED:           02-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS A SIMPLE PERSONAL FINANCE MANAGEMENT APPLICATION

    CLASS DESCRIPTION:      THIS CLASS ACTS AS THE FRONTEND OF THE APPLICATION. IT INTERACTS WITH THE USER THROUGH
                            SIMPLE COMMANDS.
"""

#!/usr/bin/python3

from gui.applogic.walletdbdir.dbclass import Walletdbmanager
from gui.applogic.dataentry import NewDataEntry

appname = "MyWallet Application"
pro_info = "Track your personal finances; monitor every penny"
pro_info_1 = "This application is powered by commands. Use the following to \n\tperform most common tasks. Use 'manwallet' for more."

line = "__________________________________________________________________"

#================================   display on screen  ============================

print("\t\t", appname)
print("\t", pro_info)
print(line)
print(pro_info_1)
print("\n")
print("New: add\tEdit: ed\tDelete: del\tDisplay: ds\tManual: 'manwallet'")
print(line)

dbfile = 'mywallet.db'
done = False

# Create database file and table if not exist
db = Walletdbmanager(dbfile)
# db.create_table()

dataEntery = NewDataEntry(dbfile)

cmds = ["add", "ds", "done", "manwallet"]

while not done:
    print("\nWhat do you want to do? ")
    activity = input("?> ")

    if activity not in cmds:
        print("Command not found")

    elif activity == "done":
        print("\nAPPLICATION EXIT")
        done = True
        exit(0)

    else:
        match activity:
            case "add":
                print("\n\t\tAdd New Category Data")
                print("\tCategory: 'c'\tQuit: 'q' ")
                print("\t____________________________________________")
                dataEntery._savenewcategory()
                
            case "ds":
                print("\n\t\tAdd New Category Data")
                print("\tCategory: 'c'\tQuit: 'q' ")
                print("\t____________________________________________")
                dataEntery._getrecords()

            # case "mangram":
                # val = acts.anagram(game_round).mangram()