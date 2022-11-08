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
                    print("Score: ", score)
                    print("Rounds: ", rounds)
                    print("Game process cancelled")
                    done = True
                    break

                elif guess == asem:
                    print(random.choice(success))
                    score += 3
                    print("Score: ", score)
                    break

                elif i == 1 and guess != asem:
                    print("Correct word: ", asem)
                    score += 0
                    print("Score: ", score)



    # def getscore(self):
    #     """Score a Guess
    #     Invokes the guess_word() function and awards marks based on the return value
    #     of the function
    #     """

    #     i = 3
    #     score = 0
    #     asem = self.get_word()
    #     quest = self.shuffle_word(asem).lower().strip()
        
    #     success = ["Correct!", "Congrats!", "Awesome!", "Wow!", "Bingo!", "Genius!"]

    #     print("New word: ", quest)
    #     for i in range(3, 0, -1):
    #         guess = self.guessword(i)

    #         if guess == asem:
    #             print(random.choice(success))
    #             score += 3
    #             print("Score: ", score)
    #             break
    #         elif i == 1 and guess != asem:
    #             print("Correct word: ", asem)
    #             score += 0
    #             print("Score: ", score)
      
    #     return score
    

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