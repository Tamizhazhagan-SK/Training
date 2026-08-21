from models.vehicle import Vehicle

class HybridVehicle(Vehicle):
    def __init__(self, vin, model, battery_kwh, fuel_type):
        super().__init__(vin, model)
        self.validate_battery_kwh(battery_kwh)
        self.__battery_kwh = battery_kwh
        self.__fuel_type = fuel_type

    def __str__(self):
        return f"VIN: {self._vin}, Model: {self._model}, Battery: {self.__battery_kwh} kWh, Fuel Type: {self.__fuel_type}"

    def __repr__(self):
        return f"HybridVehicle(vin='{self._vin}', model='{self._model}', battery_kwh={self.__battery_kwh}, fuel_type='{self.__fuel_type}')"

    @property
    def get_battery_kwh(self):
        return self.__battery_kwh

    @get_battery_kwh.setter
    def set_battery_kwh(self, value):
        self.validate_battery_kwh(value)
        self.__battery_kwh = value

    @property
    def get_fuel_type(self):
        return self.__fuel_type

    @get_fuel_type.setter
    def set_fuel_type(self, value):
        self.__fuel_type = value

    def validate_battery_kwh(self, value):
        if value <= 0:
            raise ValueError("Battery capacity must be a positive value.")