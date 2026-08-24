from models.ip import set_operations

def frozen_set():
    frozen_features = frozenset({"sunroof", "leather seats", "navigation system", "heated seats", "backup camera", "bluetooth connectivity", "cruise control", "alloy wheels"})
    return frozen_features

def car_model_set():
    """Return the model groups as separate frozensets."""

    car_models=[]
    standard_models = frozenset({
        "BMW 2 Series",
        "BMW 3 Series",
        "BMW 4 Series",
        "BMW X1",
        "BMW X3",
    })

    premium_models = frozenset({
        "BMW 5 Series",
        "BMW 7 Series",
        "BMW X5",
        "BMW X7",
    })

    car_models.append(standard_models)
    car_models.append(premium_models)

    return car_models


def car_prize():
    """Return prices using each model frozenset as a dictionary key."""
    price_dict = {}

    for frozen_data in car_model_set():
        price_dict[frozen_data] = 100000 + (len(frozen_data) * 50000)

    return price_dict
