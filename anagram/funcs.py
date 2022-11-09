import random

class anagram:

    def __init__(self, filepath):
        """Initialise class variables
        
        filepath:   path to the file or name of the file
        """
        self._filepath = filepath
    
    def get_filepath(self):
        """Get Filepath

        Returns the path of the file
        """
        return self._filepath


    def gameloop(self):

        rounds = 0
        score = 0
        done = False
        
        quits = ["q", "quit", 'Q', "Quit", "QUIT"]
        success = ["Correct!", "Congrats!", "Awesome!", "Wow!", "Bingo!", "Genius!"]

        while not done:
            
            asem = self.get_word()
            quest = self.shuffle_word(asem)
            print("\nNew word: ", quest)

            rounds += 1

            for i in range(3, 0, -1):
                guess = self.guessword(i)

                if guess in quits:
                    print("\nSummary: ")
                    print(self.__str__(rounds, score))
                    print("\nGame process cancelled")
                    done = True
                    break

                elif i == 3 and guess == asem:
                    print(random.choice(success))
                    print("Score: ", 5)
                    score += 5
                    
                    break

                elif i == 2 and guess == asem:
                    print(random.choice(success))
                    print("Score: ", 3)
                    score += 3

                    break

                elif i == 1 and guess != asem:
                    print("Correct word: ", asem)
                    print("Score: ", 1)
                    score += 1


    def guessword(self, attempt):
        """Guess the correct word
        Accepts user input

        @attempt: an integer value to count number of attempts made
        """

        guess = input("Attempt {}: ".format(attempt)).lower()

        return guess


    def shuffle_word(self, asem):
        """Shuffle Word
        Shuffles a word passed to it as a parameter

        asem:   the parameter
        """
        asemlist = list(asem)
        shuffled = asem
        done = False

        while not done:
            random.shuffle(asemlist)
            shuffled = ''.join(asemlist)

            if shuffled != asem:
                return shuffled


    def get_word(self):
        """
        Selects a word from the list of words at random
        """
        file = self.get_filepath()

        rec = open(file, 'r')
        wordstore = list(rec)
        while True:
            getword = random.choice(wordstore).strip()

            if getword == "":
                continue

            return getword

    
    def __str__(self, _round, _totalscore):
        """Return a string representation of values
        
        @_round: the current stage of the game
        @_totalscore: the total score earned so far
        """

        return "Game stage: {}\nTotal score: {}".format(_round, _totalscore)