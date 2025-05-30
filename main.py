
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

# Instantiate package hashmap with data from CSV.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)


# Step 1: Define Truck 3 start time (after 10:20 AM and Truck 1 return)
start_time1 = datetime.strptime("08:00", "%H:%M")
start_time2 = datetime.strptime("09:05", "%H:%M")
start_time3 = datetime.strptime("10:20", "%H:%M")


# Step 2: Initialize Truck 3
truck1 = Truck(1, start_time1)
truck2 = Truck(2, start_time2)
truck3 = Truck(3, start_time3)

# Step 3: Load Truck 3 packages\
"""
truck1_ids = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
truck2_ids = [2, 3, 6, 10, 11, 12, 17, 18, 19, 21, 22, 25, 28, 32, 36, 38]
truck3_ids = [5, 7, 8, 9, 23, 24, 26, 27, 33, 35, 39]

truck1_ids = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
truck2_ids = [2, 3, 10, 11, 12, 17, 18, 19, 21, 22, 28, 32, 36, 38]
truck3_ids = [4, 5, 7, 8, 9, 23, 24, 26, 27, 33, 35, 39]
"""

truck1_ids = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
truck2_ids = [2, 3, 5, 7, 10, 11, 12, 17, 18, 19, 21, 28, 32, 36, 38]
truck3_ids = [4, 8, 9, 22, 23, 24, 26, 27, 33, 35, 39]

loaded_packages1 = []
loaded_packages2 = []
loaded_packages3 = []



# TRUCK 1: LOAD TRUCK
for pid in truck1_ids:
    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck1.load_package(package)
        loaded_packages1.append(package)


# TRUCK 1: SIMULATE
return_time = simulate_route(truck1, start_time1)

# TRUCK 1: RESULTS
print(f"\n--- TRUCK 1 ROUTE SUMMARY ---")
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck1.mileage:.2f} miles")
print("\nDelivered Packages:")
for p in loaded_packages1:
    print(f"Package {p.pkg_id} delivered at {p.delivery_time}")





# TRUCK 2: LOAD TRUCK
for pid in truck2_ids:

    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck2.load_package(package)
        loaded_packages2.append(package)


# TRUCK 2: SIMULATE
return_time = simulate_route(truck2, start_time2)

# TRUCK 2: RESULTS
print(f"\n--- TRUCK 2 ROUTE SUMMARY ---")
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck2.mileage:.2f} miles")
print("\nDelivered Packages:")
for p in loaded_packages2:
    print(f"Package {p.pkg_id} delivered at {p.delivery_time}")




#Fix Package 9's address (corrected at 10:20 AM)
package_9 = package_map.search(9)
if package_9:
    package_9.address = "410 S State St"
else:
    print("⚠️ Package 9 still not found in map!")

print(f"Package 9 updated address: {package_9.address}")



# TRUCK 3: LOAD TRUCK
for pid in truck3_ids:

    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck3.load_package(package)
        loaded_packages3.append(package)


# TRUCK 3: SIMULATE
return_time = simulate_route(truck3, start_time3)

# TRUCK 3: RESULTS
print(f"\n--- TRUCK 3 ROUTE SUMMARY ---")
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck3.mileage:.2f} miles")
print("\nDelivered Packages:")
for p in loaded_packages3:
    print(f"Package {p.pkg_id} delivered at {p.delivery_time}")


float1 = truck1.mileage + truck2.mileage + truck3.mileage

print(f"⚠️ TOTAL MILEAGE = {float1} ")