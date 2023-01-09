#!/usr/bin/python3

class Vehicle:
    """ A model of a vehicle """

    def __init__(self, vehicleName, vehicleColor):
        self.__vehicleName = vehicleName
        self.__vehicleColor = vehicleColor

    @property
    def _vehicleColor(self):
        return self.__vehicleColor

    @_vehicleColor.setter
    def _vehicleColor(self, color):
        if color == " " or color == "":
            raise ValueError("Color value not provided!")
        elif not isinstance(color, str):
            raise TypeError("Color value must be a string of characters")
        else:
            self.__vehicleColor = color

    @property
    def _vehicleName(self):
        return self.__vehicleName


class Car(Vehicle):
    """ Inherit from Vehicle to model a car """

    def __init__(self, carName, carColor, carModel):
        super().__init__(carName, carColor)
        self.__carModel = carModel

    def __str__(self):
        return "Name: {}\nModel: {}\nColor: {}".format(self._vehicleName, self._vehicleColor, self.__carModel)


if __name__ == '__main__':

    vech = Car("Ford Mustang", "GT350", "Sky Blue")
    print(vech.__str__())
