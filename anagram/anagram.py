import datetime
import funcs as acts
from dbclass import gamedbmanager as db

gamewords = 'game_words'
dbfile = 'gamedb.db'

done = False
game_round = 0
total_score = 0
game_date = datetime.datetime.now()
cmds = ["_play_", "_man_", "_done_"]

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
        val = acts.anagram(gamewords)
        score = val.getscore()