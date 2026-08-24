class ElectricSystem:
    """
    Represents the electric system of a vehicle.
    """

    def __init__(self, voltage, capacity):
        """
        Initializes the ElectricSystem with battery capacity and voltage.

        :param battery_capacity: The capacity of the battery in kWh.
        :param voltage: The voltage of the electric system in volts.
        """
        self.battery_capacity = capacity
        self.voltage = voltage
        

    def calculate_energy(self) -> float:
        """
        Calculates the total energy stored in the battery.

        :return: Total energy in watt-hours (Wh).
        """
        return self.battery_capacity * 1000  # Convert kWh to Wh