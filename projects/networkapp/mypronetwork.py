"""
    =======================     MY PROFESSIONAL NETWORK CONTACT APPLICATION     ===================================
    DATE:                   16TH SEPTEMBER, 2022
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS IS A SIMPLE CONTACT MANAGEMENT APPLICATION. ITS MAIN PURPOSE IS TO STORE THE INFORMATION
                            OF PEOPLE IN MY PROFESSIONAL NETWORK IN A DATABASE FILE CREATED WITH sqlite3
    CLASS DESCRIPTION:      THIS CLASS ACTS AS THE FRONTEND OF THE APPLICATION. IT INTERACTS WITH THE USER THROUGH THE COMMAND
                            LINE BY COMMANDS FROM THE USER AND QUERIES THE DATABASE THROUGH THE PRONETWORK CLASS WHICH ACTS AS 
                            A GLUE. 
"""

import userdirect as ud

appname = "MyProNetwork Application"
developer = "Emmanuel Enchill"
pro_info = "Keep track of your professional network"
pro_info_1 = "This application is powered by commands. Use the following to \n\tperform most common tasks. Use _manpro_ for more."

line_1 = "__________________________________________________________________"

#================================   display on screen  ============================

print("\t\t", appname)
print("\t", pro_info)
print(line_1)
print(pro_info_1)
print("\n")
print("New: _add_\tEdit: _ed_\tDelete: _del_\tDisplay: _ds_")
print(line_1)

done = False
cmds = ["_add_", "_adds_", "_ed_", "_eds_", "_del_", "_dels_", "_ds_", "_dss_", "_manpro_", "_done_"]

while not done:
    print("\nWhat do you want to do? ")
    activity = input("?> ")
    
    if activity not in cmds:
        print("Command not found")

    elif activity == "_done_":
        print("\nAPPLICATION EXIT")
        done = True
        exit(0)

    else:
        match activity:
            case "_add_":
                ud.UserDirect()._commit_to_database_()
            case "_adds_":
                ud.UserDirect()._commit_multi_records()
            case "_ds_":
                ud.UserDirect()._getrecords_()
            case "_dss_":
                ud.UserDirect()._get_multi_records_()
            case "_del_":
                ud.UserDirect()._deleterecord_()
            case "_dels_":
                ud.UserDirect()._delete_multiple_records()
            case "_ed_":
                ud.UserDirect()._editrecord_()
            case "_manpro_":
                ud.UserDirect()._manpro_() 