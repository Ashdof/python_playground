import funcs as acts

gamewords = 'game_words'

val = acts.anagram(gamewords)
state = val.guess_word()
print("Status: ", state)