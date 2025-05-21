
# For importing Package data from CSV.
from package_helper import load_package_data

# For importing distance data from CSV and calculating distances.
from distance_helper import load_distance_data, get_distance

# HashMap to store and look up packages
from hashmap import ChainingHashTable



# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)

# Load the matrix and index
distance_matrix, address_index = load_distance_data("data/distance_matrix.csv")


test_pairs = [
    ("1330 2100 S", "4001 South 700 East"),
    ("233 Canyon Rd", "2010 W 500 S"),
    ("1060 Dalton Ave S", "2010 W 500 S"),
    ("2010 W 500 S", "4001 South 700 East"),
]

for from_addr, to_addr in test_pairs:
    miles = get_distance(from_addr, to_addr, distance_matrix, address_index)
    print(f"{from_addr} → {to_addr}: {round(miles, 2)} miles")