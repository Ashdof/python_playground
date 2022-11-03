import funcs as acts

gamewords = 'game_words'

val = acts.anagram(gamewords)

# while not done:
print("Word: {} \nShuffled: {}".format(val.get_word(), val.shuffle_word()))