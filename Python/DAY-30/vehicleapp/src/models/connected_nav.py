from models.nav_system import NavigationSystem

class ConnectedNavigation(NavigationSystem):
    """Represents a connected navigation system.

    Attributes:
        __name (str): The name of the navigation system.
        __version (str): The version of the navigation system.
    """

    def __init__(self, navigation_data):
        """Initialize the ConnectedNavigation instance.

        Parameters:
            name (str): The name of the navigation system.
            version (str): The version of the navigation system.
        """

        super().__init__(navigation_data)
        self.navigation = navigation_data

    #destructor for the instance
    def __del__(self):
        """Destructor for the ConnectedNavigation instance."""
        print(f"ConnectedNavigation instance '{self.navigation}' is being destroyed.")    

    def calc_route(self, start, end):
        # Implement route calculation logic here
        return f"Calculating route from {start} to {end} using connected navigation."

    def get_current_location(self, start, end):
        # Implement logic to get current location here
        return f"Current location is between {start} and {end}."

    def update_map(self, new_map_data):
        # Implement map update logic here
        self.map_data = new_map_data
        return "Map data updated."

    