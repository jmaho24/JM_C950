# Required for handling start time
from datetime import datetime

# For importing Package data from CSV.
import package_helper

# HashMap to store and look up packages
from hashmap import ChainingHashTable

# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
package_helper.load_package_data("data/package_data.csv", package_map)

# Test print line for breakpoint



print("Done loading.")

