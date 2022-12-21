"""
    =======================     MY ANAGRAM GAME APPLICATION     ===================================
    FILE:                   USER INTERFACE CLASS
    DATE:                   04-NOV-2022
    LAST UPDATED:           21-DEC-2022
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS IS A SIMPLE GAME APPLICATION. IT DISPLAYS SHUFFLED WORDS FOR THE USER TO GUESS THE
                            CORRECT SPELLING. IT SAVES GAME RECORDS TO AN SQLite3 DATABASE FILE
                            
    CLASS DESCRIPTION:      THIS CLASS ACTS AS THE FRONTEND OF THE APPLICATION. IT INTERACTS WITH THE USER THROUGH
                            SIMPLE COMMANDS.
"""

#!/usr/bin/python3

import funcs as acts
from dbclass import gamedbmanager

appname = "MyAnagram Game Application"
developer = "Emmanuel Enchill"
pro_info = "Challenge yourself to best the world of word game"
pro_info_1 = "This application is powered by commands. Use the following to \n\tperform most common tasks. Use 'mangram' for more."

line = "__________________________________________________________________"

#================================   display on screen  ============================

print("\t\t", appname)
print("\t", pro_info)
print(line)
print(pro_info_1)
print("\n")
print("Game Mode: 'play'\tDisplay Mode: 'ds'\tApp Manual: 'mangram' ")
print(line)

gamewords = 'game_words'
dbfile = 'gamedb.db'

# Create database file and table if not exist
db = gamedbmanager(dbfile)
# db.create_table()

done = False
game_round = 0
total_score = 0
cmds = ["play", "mangram", "ds", "done"]

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
            case "play":
                print("\n\t\t\tGame Mode")
                print("\t\tNavigate the Game Mode: ")
                print("\tShuffle: 's'\tQuit: 'q'\tPass: 'Enter' ")
                print("\t____________________________________________")
                val = acts.anagram(gamewords).gameloop()
            case "ds":
                val = acts.anagram(gamewords)._getrecords_()
            case "mangram":
                val = acts.anagram(game_round).mangram()