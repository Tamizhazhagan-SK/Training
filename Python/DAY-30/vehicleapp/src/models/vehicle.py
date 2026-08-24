class Vehicle:
    """A base class representing a generic vehicle.

    Attributes:
        _vin (str): The Vehicle Identification Number.
        _model (str): The model name of the vehicle.
    """

    # Double underscore prefix is used to indicate that these attributes are intended to be private 
    # and should not be accessed directly from outside the class. 
    # This is a convention in Python to promote encapsulation and data hiding.
    def __init__(self, vin, model, adas=None, navigation=None): #battery_kwh):
        """Initialize the Vehicle instance.

        Parameters:
            vin (str): The Vehicle Identification Number.
            model (str): The model name of the vehicle.
            adas (ADAS): The ADAS system for the vehicle.
        """
        self._vin = vin
        self._model = model
        self._adas = adas
        self._navigation = navigation

        # self.__vin = vin
        # self.__model = model
        #self.validate_battery_kwh(battery_kwh)
        #self.__battery_kwh = battery_kwh

    def power(self):
        return f"The vehicle {self._model} with VIN {self._vin} is powered on"

    def get_adas(self):
        """Get the vehicle identity and its ADAS system.
        Returns:
            dict: The VIN, model, and ADAS system of the vehicle.
        """
        return {
            "vin": self._vin,
            "model": self._model,
            "adas": self._adas,
        }

    def get_navigation(self):
        """Return the vehicle's configured navigation system."""
        return self._navigation

    

        #user friendly string representation of the object
    def __str__(self):
        """Return a user-friendly string representation of the vehicle."""
        adas = self._adas.activate_adas() if self._adas else "Not installed"
        return f"VIN: {self._vin}, Model: {self._model}, ADAS: {adas}" #, Battery: {self.__battery_kwh} kWh"

    #developer friendly string representation of the object
    def __repr__(self):
        """Return a developer-friendly string representation to recreate the object."""
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