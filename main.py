# Required for handling start time
from datetime import datetime
# HashMap to store and look up packages
from hashmap import ChainingHashTable

# Core classes
from truck import Truck
from package import Package


# CSV loading logic
from package_helper import load_package_data  # or basic_load_packages if you're still using that

import package_helper

# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_data.load_package_data("data/package_data.csv", package_map)

# Test print line for breakpoint

print(package_map.search(15))

print("Done loading.")

