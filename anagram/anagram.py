import funcs as acts
from dbclass import gamedbmanager

gamewords = 'game_words'
dbfile = 'gamedb.db'

# Create database file and table if not exit
db = gamedbmanager(dbfile)
# db.create_table()

done = False
game_round = 0
total_score = 0
cmds = ["play", "_man_", "ds", "done"]

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
                val = acts.anagram(gamewords).gameloop()
            case "ds":
                val = acts.anagram(gamewords)._getrecords_()