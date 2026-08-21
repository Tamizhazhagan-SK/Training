from models.vehicle import Vehicle

class ElectricVehicle(Vehicle):
    def __init__(self, vin, model, battery_kwh):
        super().__init__(vin, model)
        self.validate_battery_kwh(battery_kwh)
        self.__battery_kwh = battery_kwh

    def __str__(self):
        return f"VIN: {self._vin}, Model: {self._model}, Battery: {self.__battery_kwh} kWh"

    def __repr__(self):
        return f"ElectricVehicle(vin='{self._vin}', model='{self._model}', battery_kwh={self.__battery_kwh})"


    @property
    def get_battery_kwh(self):
        return self.__battery_kwh

    @get_battery_kwh.setter
    def set_battery_kwh(self, value):
        self.validate_battery_kwh(value)
        self.__battery_kwh = value

    def validate_battery_kwh(self, value):
        if value <= 0:
            raise ValueError("Battery capacity must be a positive value.")           