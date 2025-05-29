
# For importing Package data from CSV.
from package_helper import load_package_data
# For importing distance data from CSV and calculating distances.
from package import Package
from distance_helper import get_distance

# HashMap to store and look up packages
from hashmap import ChainingHashTable

# For handling time.
from datetime import timedelta, datetime

from routing import simulate_route

# Basic classes.
from truck import Truck
from package import Package

# Instantiate package hashmap.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)


# Step 1: Define Truck 3 start time (after 10:20 AM and Truck 1 return)
start_time = datetime.strptime("10:20", "%H:%M")

# Step 2: Initialize Truck 3
truck = Truck(3, start_time)

# Step 3: Load Truck 3 packages
truck3_ids = [5, 7, 8, 9, 23, 24, 26, 27, 33, 35, 39]
loaded_packages = []

for pid in truck3_ids:
    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck.load_package(package)
        loaded_packages.append(package)

# Step 4: Fix Package 9's address (corrected at 10:20 AM)
package_9 = package_map.search(9)
if package_9:
    package_9.address = "410 S State St"
else:
    print("⚠️ Package 9 still not found in map!")

print(f"Package 9 updated address: {package_9.address}")
# Step 5: Simulate route
return_time = simulate_route(truck, start_time)

# Step 6: Output results
print(f"\n--- TRUCK 3 ROUTE SUMMARY ---")
print(f"Return time: {return_time.strftime('%H:%M')}")
print(f"Total mileage: {truck.mileage:.2f} miles")
print("\nDelivered Packages:")
for p in loaded_packages:
    print(f"Package {p.pkg_id} delivered at {p.delivery_time.strftime('%H:%M')}")