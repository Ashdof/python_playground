#!/usr/bin/python3

class Robot:
    """ Represents a robot with a name """

    """ A class variable, counting the number of robots """
    population = 0

    def __init__(self, name):
        """ Initialise the data """
        self._name = name

        print('Initialising {}'.format(self._name))

        """ Increment population by 1 whenever a new roboto is created """
        Robot.population += 1;


    def destroy(self):
        """ Destroy robot """
        print("{} is being destroyed".format(self._name))

        # This line is the same as Robot.population
        self.__class__.population -= 1

        if Robot.population == 0:
            print("{} was the last robot.".format(self._name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))


    def salute(self):
        """ Greetings by the robot """

        print("Greetings from {}".format(self._name))


    @classmethod
    def quantity_of_robots(cls):
        """ Quantity of robots left """

        print("There are currently {} robots.".format(cls.population))



#   ======================================================

if __name__ == '__main__':

    name_0 = input("Name of robot 1: ")
    droid_0 = Robot(name_0)
    droid_0.salute()
    droid_0.quantity_of_robots()
    print()

    name_1 = input("Name of robot 2: ")
    droid_1 = Robot(name_1)
    droid_1.salute()
    droid_1.quantity_of_robots()
    print()

    print("Robots can do some work here")

    droid_0.destroy()
    droid_1.destroy()

    Robot.quantity_of_robots()
