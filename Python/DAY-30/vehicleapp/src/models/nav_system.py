from abc import ABC, abstractmethod

class NavigationSystem(ABC):
    def __init__(self, map_data):
        self.map_data = map_data

    @abstractmethod
    def calc_route(self, start, end):
        pass

    @abstractmethod
    def get_current_location(self, start, end):
        pass

    @abstractmethod
    def update_map(self, new_map_data):
        pass