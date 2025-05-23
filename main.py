
# For importing Package data from CSV.
from package_helper import load_package_data
# For importing distance data from CSV and calculating distances.
from distance_helper import load_distance_data, get_distance

# HashMap to store and look up packages
from hashmap import ChainingHashTable

from datetime import datetime

from truck import Truck

# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)

# Load the matrix and index
distance_matrix, address_index = load_distance_data("data/distance_matrix.csv")

start_time = datetime.strptime("08:00", "%H:%M")
truck = Truck(1, start_time)

print(truck.time.strftime("%I:%M %p"))  # Should print "08:30 AM"