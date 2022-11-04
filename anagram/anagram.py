import funcs as acts

gamewords = 'game_words'

val = acts.anagram(gamewords)
score = val.get_score()

print("Score: ", score)