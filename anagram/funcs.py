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


    def getscore(self):
        """Score a Guess
        Invokes the guess_word() function and awards marks based on the return value
        of the function
        """

        i = 3
        score = 0
        asem = self.get_word()
        quest = self.shuffle_word(asem).lower().strip()
        
        success = ["Correct!", "Congrats!", "Awesome!", "Wow!", "Bingo!", "Genius!"]

        print("New word: ", quest)
        for i in range(3, 0, -1):
            guess = self.guessword(i)

            if guess == asem:
                print(random.choice(success))
                score += 3
                break
            else:
                score += 0

        print("Score: ", score)
        
        return score
    
    def guessword(self, attempt):
        """Guess the correct word
        Accepts user input

        @attempt: an integer value to count number of attempts made
        """

        guess = input("Attempt {}: ".format(attempt)).lower()

        return guess



    # def guess_word(self):
    #     """Guess the Correct Word
    #     Present a shuffled word to be guessed by the user. If guess right, return 1
    #     else return -1
    #     """

    #     asem = self.get_word()
    #     quest = self.shuffle_word(asem).lower().strip()

    #     print("\nSolve: ", quest)
    
    #     for i in range(3, 0, -1):
    #         print("\nAttempt {}: ".format(i))
    #         guess = input().lower()

    #         if i == 1 and guess !=  asem:
    #             print("Sorry, you couldn't solve this!")
    #             print("The correct word is: ", asem)
    #             return -1

    #         elif guess == asem:
    #             print("Congrats!")                
    #             return 1


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