import datetime
import funcs as acts
import trial as tries
from dbclass import gamedbmanager as db

gamewords = 'game_words'
dbfile = 'gamedb.db'

done = False
game_round = 0
total_score = 0
game_date = datetime.datetime.now()
cmds = ["play", "_man_", "done"]

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
        val = acts.anagram(gamewords)
        score = val.gameloop()