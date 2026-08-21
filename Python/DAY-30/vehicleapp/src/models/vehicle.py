class Vehicle:

    # Double underscore prefix is used to indicate that these attributes are intended to be private 
    # and should not be accessed directly from outside the class. 
    # This is a convention in Python to promote encapsulation and data hiding.
    def __init__(self, vin, model): #battery_kwh):
        self._vin = vin
        self._model = model

        # self.__vin = vin
        # self.__model = model
        #self.validate_battery_kwh(battery_kwh)
        #self.__battery_kwh = battery_kwh

        #user friendly string representation of the object
    def __str__(self):
        return f"VIN: {self._vin}, Model: {self._model}" #, Battery: {self.__battery_kwh} kWh"

    #developer friendly string representation of the object
    def __repr__(self):
        return f"Vehicle(vin='{self._vin}', model='{self._model}')"#, battery_kwh={self.__battery_kwh})"

    # #user friendly string representation of the object
    # def __str__(self):
    #     return f"VIN: {self.__vin}, Model: {self.__model}" #, Battery: {self.__battery_kwh} kWh"

    # #developer friendly string representation of the object
    # def __repr__(self):
    #     return f"Vehicle(vin='{self.__vin}', model='{self.__model}')"#, battery_kwh={self.__battery_kwh})"

    # @property
    # def get_battery_kwh(self):
    #     return self.__battery_kwh

    # @get_battery_kwh.setter
    # def set_battery_kwh(self, value):
    #     self.validate_battery_kwh(value)
    #     self.__battery_kwh = value

    # def validate_battery_kwh(self, value):
    #     if value < 0:
    #         return False
    #     return True             