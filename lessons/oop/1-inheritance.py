#!/usr/bin/python3

class School:
    """ Model a typical school """

    def __init__(self, school_name, school_motto, school_location):
        self.__school_name = school_name
        self.__school_motto = school_motto
        self.__school_location = school_location

    @property
    def _schoolName(self):
        return self.__school_name

    @_schoolName.setter
    def _schoolName(self, schoolName):
        if schoolName == "" or schoolName == " ":
            raise ValueError("Name of school cannot be blank")
        elif not isinstance(schoolName, str):
            raise TypeError("Name of school must be a string of characters")
        else:
            self.__school_name = schoolName

    @property
    def _schoolMotto(self):
        return self.__school_motto

    @_schoolMotto.setter
    def _schoolMotto(self, schoolMotto):
        if schoolMotto == "" or schoolMotto == " ":
            raise ValueError("School motto cannot be blank")
        elif not isinstance(schoolMotto, str):
            raise TypeError("Motto of school must be a string of characters")
        else:
            self.__school_motto = schoolMotto

    @property
    def _schoolLocation(self):
        return self.__school_location

    @_schoolLocation.setter
    def _schoolLocation(sekf, schoolLocation):
        if schoolLocation == "" or schoolLocation == " ":
            raise ValueError("Location of school cannot be blank")
        elif not isinstance(schoolLocation, str):
            raise TypeError("Location of school must be a string of characters")
        else:
            self.__school_location = schoolLocation


    def __str__(self):
        return "Name of school: {}\nMotto of school: {}\nLocation of school: {}".format(self.__school_name, self.__school_motto, self.__school_location)


class ClassRoom(School):
    """ Model a typical classroom of a school """

    def __init__(self, school, motto, location, className, classLevel, classPopulation):
        super().__init__(school, motto, location)
        self.__className = className
        self.__classLevel = classLevel
        self.__classPopulation = classPopulation

    @property
    def _className(self):
        return self.__className

    @_className.setter
    def _className(self, className):
        if className == "" or className == " ":
            raise ValueError("Name of class cannot be blank")
        elif not isinstance(className, str):
            raise TypeError("Name of class must be a string of characters")
        else:
            self.__className = className

    @property
    def _classLevel(self):
        return self.__classLevel

    @_classLevel.setter
    def _classLevel(self, stage):
        if stage == "" or stage == " ":
            raise ValueError("Level of class cannot be blank")
        elif not isinstance(stage, int):
            raise TypeError("Level of class must be an integer value")
        else:
            self.__classLevel = stage

    @property
    def _classPopulation(self):
        return self.__classPopulation

    @_classPopulation.setter
    def _classPopulation(self, numberOfPupils):
        if numberOfPupils == "" or numberOfPupils == " ":
            raise ValueError("Number of pupils cannot be blank")
        elif not isinstance(numberOfPupils, int):
            raise TypeError("Number of pupils must be an integer value")
        else:
            self.__classPopulation = numberOfPupils

    def __str__(self):
        return "Name of class: {}\nLevel of class: {}\nPopulation of class: {}".format(self.__className, self.__classLevel, self.__classPopulation)



if __name__ == '__main__':

    done = False
    
    while not done:
        try:
            nameOfSchool = input("Name of school: ")
            if nameOfSchool == "":
                done = True
                break
            else:
                mottoOfSchool = input("Motto of school: ")
                locOfSchool = input("Location of school: ")
                nameOfClass = input("Name of class: ")
                levelOfClass = input("Level of class: ")
                popOfClass = input("Population of class: ")

                classroom = ClassRoom(nameOfSchool, mottoOfSchool, locOfSchool, nameOfClass, levelOfClass, popOfClass)
                print(classroom.__str__())
        except e:
            print("Error: ", e)
