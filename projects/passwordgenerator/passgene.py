"""
    =======================     PASSWORD GENERATOR APPLICATION     ===================================
    FILE:                   USER INTERFACE CLASS
    DATE:                   28-DEC-2022
    LAST UPDATED:           28-DEC-2022
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS IS A SIMPLE PASSWORD GENERATOR APPLICATION.

"""

#!/usr/bin/python3

import random

appname = "Password Generator"
pro_info = "Generate passwords with a push of a button"
pro_info_1 = "This application is powered by commands. Enter'done' to quit the application"

line = "__________________________________________________________________"

#================================   display on screen  ============================

print("\t\t", appname)
print("\t", pro_info)
print(line)
print(pro_info_1)
print("\n")

done = False
cmds = ["done", ]
data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_;':\",.abcdefghijklmnopqrstuvwxyz"
print("Enter the length of the passowrd to generate")

while not done:   
    value = input("Length? > ")

    if value == "done":
        print("\nAPPLICATION EXIT")
        done = True
        exit(0)

    elif value != "done" and not isinstance(value, int):
            print("Enter an integer value\n")

    else:
        pwd = ""
        #length = int(value)

        for i in range(value):
            pwd += random.choice(data)
    
        print("Your password: {}".format(pwd))