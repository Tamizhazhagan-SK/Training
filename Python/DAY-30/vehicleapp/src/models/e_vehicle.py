from models.vehicle import Vehicle
from models.e_system import ElectricSystem

class ElectricVehicle(Vehicle, ElectricSystem):
    """A class representing an electric vehicle, inheriting from Vehicle.

    This class adds battery capacity along with properties, validation, 
    and string representations tailored for electric cars.

    Attributes:
        __battery_kwh (float): The capacity of the vehicle's battery in kWh.
    """

    def __init__(self, vin, model, battery_kwh, voltage, capacity, adas=None, navigation=None):
        """Initialize the ElectricVehicle instance.

        Parameters:
            vin (str): The Vehicle Identification Number.
            model (str): The model name of the vehicle.
            battery_kwh (float): The battery capacity in kWh (must be positive).
        """
        ElectricSystem.__init__(self, voltage=voltage, capacity=capacity)  # Initialize ElectricSystem with provided values
        super().__init__(vin, model, adas, navigation)
        self.validate_battery_kwh(battery_kwh)
        self.__battery_kwh = battery_kwh

    def __str__(self):
        """Return a user-friendly string representation of the electric vehicle."""
        return f"{super().__str__}, Battery: {self.__battery_kwh} kWh"

    def __repr__(self):
        """Return a developer-friendly string representation to recreate the electric vehicle object."""
        return f"ElectricVehicle(vin='{self._vin}', model='{self._model}', battery_kwh={self.__battery_kwh})"

    def power(self):
        return f"The vehicle {self._model} with VIN {self._vin} is powered on and voltage: {self.voltage}V, capacity: {self.battery_capacity}Ah"


    @property
    def get_battery_kwh(self):
        """float: Get or set the battery capacity in kWh."""
        return self.__battery_kwh

    @get_battery_kwh.setter
    def set_battery_kwh(self, value):
        self.validate_battery_kwh(value)
        self.__battery_kwh = value

    def validate_battery_kwh(self, value):
        """Validate that the given battery capacity is a positive value.

        Parameters:
            value (float): The battery capacity value to check.

        Raises:
            ValueError: If the value is less than or equal to zero.
        """
        if value <= 0:
            raise ValueError("Battery capacity must be a positive value.")