import random

class anagram:

    def __init__(self, filepath):
        self._filepath = filepath
    
    def get_filepath(self):
        return self._filepath

    def get_word(self):
        """Select Word Function
        Selects a word from the list of words at random

        @filepath: path to the file or name of the file
        """
        file = self.get_filepath()

        rec = open(file, 'r')
        wordstore = list(rec)
        while True:
            getword = random.choice(wordstore).strip()

            if getword == "":
                continue

            return getword


    def shuffle_word(self):
        asem = self.get_word()

        asemlist = list(asem)
        shuffled = asem
        done = False

        while not done:
            random.shuffle(asemlist)
            shuffled = ''.join(asemlist)

            if shuffled != asem:
                return shuffled