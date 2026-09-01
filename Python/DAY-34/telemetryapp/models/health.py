from enum import Enum


class EngineStatus(str, Enum):
    NORMAL = "NORMAL"
    OVERHEATING = "OVERHEATING"


class BatteryStatus(str, Enum):
    GOOD = "GOOD"
    LOW = "LOW"


class FuelStatus(str, Enum):
    GOOD = "GOOD"
    LOW = "LOW"


class OverallStatus(str, Enum):
    HEALTHY = "HEALTHY"
    NEEDS_ATTENTION = "NEEDS_ATTENTION"


class AlertType(str, Enum):
    ENGINE_OVERHEATING = "ENGINE_OVERHEATING"
    LOW_BATTERY = "LOW_BATTERY"
    LOW_FUEL = "LOW_FUEL"


# Thresholds driving alerts and health checks
ENGINE_OVERHEAT_THRESHOLD = 110
LOW_BATTERY_THRESHOLD = 15
LOW_FUEL_THRESHOLD = 10
