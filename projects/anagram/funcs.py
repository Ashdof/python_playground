import random
import datetime
from dbclass import gamedbmanager

dbfile = 'gamedb.db'
db = gamedbmanager(dbfile)
ddate = datetime.datetime.now()
game_date = str(ddate.year) + "-" + str(ddate.month) + "-" + str(ddate.day)

class anagram:

    def __init__(self, filepath):
        """Initialise class variables
        
        filepath:   path to the file or name of the file
        """
        self.__filepath = filepath
    
    def get_filepath(self):
        """Get Filepath

        Returns the path of the file
        """
        return self.__filepath


    def gameloop(self):

        rounds = 0
        score = 0
        done = False
        
        quits = ["q", "quit", 'Q', "Quit", "QUIT"]
        best = ["Awesome!", "Wow!", "Bingo!", "Genius!"]
        better = ["Very good!", "Better!", "Do more!", "Congrats!"]
        good = ["Good!", "Correct!", "Keep up!", "Lucky!"]

        while not done:
            
            asem = self.get_word()
            quest = self.shuffle_word(asem)
            print("\nNew word: ", quest)

            rounds += 1

            for i in range(3, 0, -1):

                """Invoke the guessword method"""
                guess = self.guessword(i)

                if guess in quits:
                    """Save record to database, print game summary quit"""
                    db.save_record(game_date, rounds, score)
                    print("\nSummary: ")
                    print(self.__str__(rounds, score))
                    print("\nGame Mode cancelled")
                    done = True
                    break

                elif guess == "s":
                    """Reshuffle the word

                    This block reshuffles the word but should retain the counter (i) at the same
                    number at which the shuffle_word method was invoked. It needs more work

                    """
                    print("Reshuffled: ", self.shuffle_word(asem))

                elif i == 3 and guess == asem:
                    """Score highest mark for correct guess at the first attempt"""
                    print(random.choice(best))
                    print("Score: ", 5)
                    score += 5
                    
                    break

                elif i == 2 and guess == asem:
                    """Score medium mark for correct guess at the second attempt"""
                    print(random.choice(better))
                    print("Score: ", 3)
                    score += 3

                    break

                elif i == 1 and guess == asem:
                    """Score lowest mark for correct guess at the third attempt"""
                    print(random.choice(good))
                    print("Score: ", 1)
                    score += 1

                elif i == 1 and guess != asem:
                    """Score nothing and print correct word"""
                    print("Correct word: ", asem)
                    print("Score: ", 0)
                    score += 0


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

    
    def mangram(self):
        """Displays the manual when invoked
        
        Read the information from file and display it on the scree
        """
        man = open("mangram", "r")

        for line in man:
            print(line, end='')
        man.close()


#===============    DATABASE ACCESS SECTION     ==================================

    def _getrecords_(self):
        """Display Records
        
        User is presented with options to choose from
        """
        
        done = False

        print("\nSelect the number for a corresponding record to display\n")
        print("1: Detail Record")
        
        while not done:
            val = input("\nNumber ?>: ")

            if val == "":
                print("Display Mode cancelled")
                done = True
                
            else:
                match val:
                    case "1":
                        db.display_detail_records()
                        done = True

                    # case "2":
                    #     db.display_names_and_codes()
                    #     done = True

                    # case "3":
                    #     db.display_names_prof_contacts()
                    #     done = True

                    # case "4":
                    #     db.display_names_and_numbers()
                    #     done = True

                    # case "5":
                    #     db.display_names_email_addresses()
                    #     done = True