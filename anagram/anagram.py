import funcs as acts

gamewords = 'game_words'

val = acts.anagram(gamewords)
nsem = val.get_word()
# while not done:
print("Word: {} \nShuffled: {}".format(nsem, val.shuffle_word(nsem)))