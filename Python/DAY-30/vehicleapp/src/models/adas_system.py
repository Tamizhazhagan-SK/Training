class ADAS:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"ADAS: {self._name}"

    def __repr__(self):
        return f"ADAS(name='{self._name}')"

    def activate_adas(self):
        return f"ADAS system {self._name} activated."

    def deactivate_adas(self):
        return f"ADAS system {self._name} deactivated."