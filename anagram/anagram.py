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
        # invoke save_record function here
        print("\nGame Summary\n=============================")
        print("Game rounds: {}\nTotal score: {}".format(game_round, total_score))
        print("\nAPPLICATION EXIT")
        done = True
        exit(0)

    else:
        val = acts.anagram(gamewords)
        score = val.get_score()
        total_score += score
        game_round += 1

# print("Score: ", score)