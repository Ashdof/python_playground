class Person:

    def __init__(self, name):
        self._name = name


    def say_hi(self):
        print('Hello, my name is', self._name)





#   =============================

if __name__ == '__main__':

    done = False

    while not done:
        name = input('What\'s your name?: ')
        
        if name == "":
            done = True
            break
        else:
            p = Person(name)
            p.say_hi()
