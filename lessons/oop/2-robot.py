class Robot:

    def __init__(self, name=None, year=2000):
        self.__name = name;
        self.__year = year


    def salute(self):

        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name;

    def get_name(self):
        return self.__name

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def __repr__(self):
        return "Robot ('" + self.__name + "', '" + str(self.__year) + "')"

    def __str__(self):
        return "Name: '" +self.__name + "', Build year: '"+str(self.__year)+"' "



#   =================================================================

if __name__ == '__main__':

    x = Robot("Ashdof", 1990)
    y = Robot("Amoaful", 1949)

    for rob in [x, y]:
        rob.salute()

        if rob.get_name() == "Amoaful":
            rob.set_year(1995)

        print("I was built in the year "+str(rob.get_year())+"! ")

