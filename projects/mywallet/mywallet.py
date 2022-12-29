"""
    =======================     MYWALLET APPLICATION     ===================================
    FILE:                   USER INTERFACE CLASS
    DATE:                   29-DEC-2022
    LAST UPDATED:           29-DEC-2022
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS A SIMPLE PERSONAL FINANCE MANAGEMENT APPLICATION

    CLASS DESCRIPTION:      THIS CLASS ACTS AS THE FRONTEND OF THE APPLICATION. IT INTERACTS WITH THE USER THROUGH
                            SIMPLE COMMANDS.
"""

#!/usr/bin/python3

from dbclass import walletdbmanager
import dataentry as de

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
print("New: '_add_'\tEdit: '_ed_'\tDelete: '_del_'\tDisplay: '_ds_'\tManual: 'manwallet'")
print(line)

dbfile = 'gamedb.db'

# Create database file and table if not exist
db = walletdbmanager(dbfile)
db.create_table()