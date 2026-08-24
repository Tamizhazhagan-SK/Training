from models.connected_nav import ConnectedNavigation
from models.standard_nav import StandardNavigationSystem
from models.variant import Variant


def create_navigation(variant, navigation_data):
	"""Create a navigation implementation for a vehicle variant.

	High-level vehicles receive connected navigation. Entry-level vehicles
	receive standard navigation, while mid-level vehicles receive standard
	navigation with the supplied richer map data.
	"""
	if isinstance(variant, str):
		variant = Variant(variant)

	if variant == Variant.HIGH:
		return ConnectedNavigation(navigation_data)

	if variant in (Variant.MID, Variant.LOW):
		if variant == Variant.MID and isinstance(navigation_data, dict):
			navigation_data = {**navigation_data, "live_traffic": False}
		return StandardNavigationSystem(
			map_data=navigation_data,
			name="Standard Navigation",
			description="Offline route guidance"
		)

	raise ValueError(f"Unsupported vehicle variant: {variant}")


def create_navigation_app(variant_type):
	"""Create navigation for a variant using default map data."""
	navigation_data = {
		"map_data": f"{variant_type.value} map data"
	}
	return create_navigation(variant_type, navigation_data)



if __name__ == "__main__":
	variant = Variant.HIGH
	navigation_app = create_navigation_app(variant)

	route = navigation_app.calc_route("Point A", "Point B")
	current_location = navigation_app.get_current_location("Point A", "Point B")
	navigation_app.update_map("Updated Map Data")

	print(f"Route: {route}")
	print(f"Current Location: {current_location}")

del navigation_app  # Explicitly delete the navigation_app instance to trigger the destructor


