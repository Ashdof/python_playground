import funcs as acts
from dbclass import gamedbmanager

gamewords = 'game_words'
dbfile = 'gamedb.db'

val = acts.anagram(gamewords)
dbmanager = gamedbmanager(dbfile).create_table()

# score = val.get_score()

# print("Score: ", score)