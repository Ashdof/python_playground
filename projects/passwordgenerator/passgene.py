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
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
        "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
        "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
        "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
data = "0123456789!@#$%^&*_;:,.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the length of the passowrd to generate")

while not done:   
    value = input("Length? > ")

    if value == "done":
        print("\nAPPLICATION EXIT")
        done = True
        exit(0)

    elif value not in nums:
        print("Enter an integer value\n")
        
    else:
        pwd = ""
        length = int(value)

        if type(length) not in (int, ):
            print("Enter an integer value\n")

        for i in range(length):
            pwd += random.choice(data)

        print("Your password: {}\n".format(pwd))