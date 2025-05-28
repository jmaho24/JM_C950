
# For importing Package data from CSV.
from package_helper import load_package_data
# For importing distance data from CSV and calculating distances.
from distance_helper import load_distance_data, get_distance

# HashMap to store and look up packages
from hashmap import ChainingHashTable

# For handling time.
from datetime import timedelta, datetime

# Basic classes.
from truck import Truck
from package import Package

# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)

# Load the matrix and index
distance_matrix, address_index = load_distance_data("data/distance_matrix.csv")

start_time_truck1 = datetime.strptime("08:00", "%H:%M")
start_time_truck2 = datetime.strptime("09:05", "%H:%M")

truck1 = Truck(1, start_time_truck1)
truck2 = Truck(1, start_time_truck2)
