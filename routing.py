from collections import defaultdict
from distance_helper import get_distance
from datetime import timedelta

HUB_ADDRESS = "4001 South 700 East"

def group_packages_by_address(packages):
    """
    Groups a list of package objects by address.
    Returns:
        dict[str, list[Package]] — address -> [Package, Package, ...]
    """
    grouped = defaultdict(list)
    for pkg in packages:
        grouped[pkg.address].append(pkg)
    return grouped

def nearest_neighbor_route(addresses, start_location):
    """
    Determines a greedy nearest-neighbor route over a list of addresses.

    Args:
        addresses (list[str]): delivery stops (unique addresses)
        start_location (str): starting point (e.g. "HUB")

    Returns:
        list[str]: ordered list of addresses to visit
    """
    route = []
    unvisited = addresses[:]
    current = start_location

    while unvisited:
        next_stop = min(unvisited, key=lambda addr: get_distance(current, addr))
        route.append(next_stop)
        unvisited.remove(next_stop)
        current = next_stop

    return route



def simulate_route(truck, start_time):
    """
    Simulates the delivery route for a truck using a nearest neighbor strategy.

    Args:
        truck (Truck): The truck object with a list of packages loaded.
        start_time (datetime): The starting departure time for the truck.

    Returns:
        datetime: The truck’s return time after completing its delivery route.
    """
    # 1. Initialize truck state
    truck.time = start_time
    truck.current_location = HUB_ADDRESS
    total_distance = 0

    # 2. Group packages by address
    grouped = group_packages_by_address(truck.packages)
    addresses = list(grouped.keys())

    # 3. Generate delivery route
    route = nearest_neighbor_route(addresses, truck.current_location)

    # 4. Loop through each address and deliver packages
    for stop in route:
        distance = get_distance(truck.current_location, stop)
        truck.update_time(distance)
        total_distance += distance

      #  print(f"[DEBUG] Truck {truck.truck_id}: +{distance} miles to {stop}")

        for pkg in grouped[stop]:
            pkg.delivery_time = truck.time
            truck.deliver_package(pkg, 0)  # ✅ Don't add distance again

        truck.current_location = stop

    # 5. Return to hub
    return_to_hub = get_distance(truck.current_location, HUB_ADDRESS)
    print(return_to_hub)
    truck.update_time(return_to_hub)
    total_distance += return_to_hub
    truck.current_location = HUB_ADDRESS
    truck.mileage += total_distance

    # 6. Return time for possible use in Truck 3 scheduling
    return truck.time
