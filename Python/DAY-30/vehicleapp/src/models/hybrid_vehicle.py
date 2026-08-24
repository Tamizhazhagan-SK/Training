from models.vehicle import Vehicle

class HybridVehicle(Vehicle):
    """A class representing a hybrid vehicle, inheriting from Vehicle.

    This class adds battery capacity and fuel type attributes along with 
    appropriate properties, validations, and string representations.

    Attributes:
        __battery_kwh (float): The capacity of the vehicle's battery in kWh.
        __fuel_type (str): The type of fuel used by the vehicle.
    """

    def __init__(self, vin, model, battery_kwh, fuel_type, adas=None, navigation=None):
        """Initialize the HybridVehicle instance.

        Parameters:
            vin (str): The Vehicle Identification Number.
            model (str): The model name of the vehicle.
            battery_kwh (float): The battery capacity in kWh (must be positive).
            fuel_type (str): The type of fuel used by the vehicle.
        """
        super().__init__(vin, model, adas, navigation)
        self.validate_battery_kwh(battery_kwh)
        self.__battery_kwh = battery_kwh
        self.__fuel_type = fuel_type

    def __str__(self):
        """Return a user-friendly string representation of the hybrid vehicle."""
        return f"VIN: {self._vin}, Model: {self._model}, Battery: {self.__battery_kwh} kWh, Fuel Type: {self.__fuel_type}"

    def __repr__(self):
        """Return a developer-friendly string representation to recreate the hybrid vehicle object."""
        return f"HybridVehicle(vin='{self._vin}', model='{self._model}', battery_kwh={self.__battery_kwh}, fuel_type='{self.__fuel_type}')"

    @property
    def get_battery_kwh(self):
        """float: Get or set the battery capacity in kWh."""
        return self.__battery_kwh

    @get_battery_kwh.setter
    def set_battery_kwh(self, value):
        self.validate_battery_kwh(value)
        self.__battery_kwh = value

    @property
    def get_fuel_type(self):
        """str: Get or set the fuel type of the hybrid vehicle."""
        return self.__fuel_type

    @get_fuel_type.setter
    def set_fuel_type(self, value):
        self.__fuel_type = value

    def validate_battery_kwh(self, value):
        """Validate that the given battery capacity is a positive value.

        Parameters:
            value (float): The battery capacity value to check.

        Raises:
            ValueError: If the value is less than or equal to zero.
        """
        if value <= 0:
            raise ValueError("Battery capacity must be a positive value.")