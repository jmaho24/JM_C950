# Author: John Mahon
# Student ID:001193994
# Title: C950 Task 2
# Submission 1: 6/6/2025

# For handling time.
from datetime import datetime

# HashMap to store and look up packages
from hashmap import ChainingHashTable
# For importing Package data from CSV.
from package_helper import load_package_data
from routing import simulate_route
# Basic classes.
from truck import Truck

current_time = datetime.strptime("08:00 AM", "%I:%M %p")

# Instantiate package hashmap with data from CSV.
package_map = ChainingHashTable()

# Load data from packages into package hashmap.
load_package_data("data/package_data.csv", package_map)


# Step 1: Define Truck start times
start_time1 = datetime.strptime("08:00", "%H:%M").replace(year=2024, month=1, day=1)
start_time2 = datetime.strptime("09:05", "%H:%M").replace(year=2024, month=1, day=1)
start_time3 = datetime.strptime("10:20", "%H:%M").replace(year=2024, month=1, day=1)


# Step 2: Initialize Trucks
truck1 = Truck(1, start_time1)
truck2 = Truck(2, start_time2)
truck3 = Truck(3, start_time3)

# Step 3: Load Truck packages
truck1_ids = [1, 13, 14,12, 15, 16,19, 20, 29, 30, 31, 34, 37, 40]
truck2_ids = [3, 5, 6, 7, 10, 11, 17, 18,25, 21, 28, 32, 36, 38]
truck3_ids = [2,4, 8, 9, 22, 23, 24, 26, 27, 33, 35, 39]

loaded_packages1 = []
loaded_packages2 = []
loaded_packages3 = []


# TRUCK 1 SIMULATION
for pid in truck1_ids:
    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck1.load_package(package)
        loaded_packages1.append(package)

print(f"\n[--- TRUCK 1 ROUTE SUMMARY ---")
# TRUCK 1: SIMULATE
return_time = simulate_route(truck1, start_time1)

# TRUCK 1: RESULTS
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck1.mileage:.2f} miles")
print(f"--- TRUCK 1 ROUTE SUMMARY ---]")
print("\n" * 3)

# TRUCK 2 SIMULATION
for pid in truck2_ids:
    package = package_map.search(pid)

    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        # Update status if it's a delayed package and it's now 9:05
        if package.available_time <= start_time2 and package.status == "Delayed – Not Yet Available":
            package.status = "At Hub"
        truck2.load_package(package)
        loaded_packages2.append(package)

print(f"[--- TRUCK 2 ROUTE SUMMARY ---")
# TRUCK 2: SIMULATE
return_time = simulate_route(truck2, start_time2)

# TRUCK 2: RESULTS
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck2.mileage:.2f} miles")
print(f"--- TRUCK 2 ROUTE SUMMARY ---]")
print("\n" * 3)


#Fix Package 9's address (corrected at 10:20 AM)
package_9 = package_map.search(9)
if package_9:
    package_9.address = "410 S State St"
else:
    print("⚠️ Package 9 still not found in map!")


# TRUCK 3: LOAD TRUCK
for pid in truck3_ids:

    package = package_map.search(pid)
    if not package:
        print(f"⚠️ Package {pid} not found in hash map!")
    else:
        truck3.load_package(package)
        loaded_packages3.append(package)

print(f"[--- TRUCK 3 ROUTE SUMMARY ---")
# TRUCK 3: SIMULATE
return_time = simulate_route(truck3, start_time3)

# TRUCK 3: RESULTS
print(f"Return time: {return_time.strftime('%I:%M %p')}")
print(f"Total mileage: {truck3.mileage:.2f} miles")
print(f"--- TRUCK 3 ROUTE SUMMARY ---]")
print("\n" * 3)


print("\n=== DELIVERY SIMULATION COMPLETE ===\n")

print(f"Truck 1 mileage: {truck1.mileage:.2f} miles")
print(f"Truck 2 mileage: {truck2.mileage:.2f} miles")
print(f"Truck 3 mileage: {truck3.mileage:.2f} miles")
print("-" * 35)

total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
print(f"TOTAL MILEAGE DRIVEN: {total_mileage:.2f} miles\n")


def cli_loop():
    """
    Runs the Command-Line Interface (CLI) loop for user interaction.

    Allows the user to:
    1. Look up a single package by ID at a specific time.
    2. View all package statuses at a specific time.
    3. Display total mileage traveled by all trucks.
    4. Exit the program.
    """
    while True:
        print("\n--- WGUPS Delivery CLI ---")
        print("1. Look up a single package at a specific time")
        print("2. Look up all packages at a specific time")
        print("3. View total mileage driven by all trucks")
        print("4. Exit")

        choice = input("Enter choice (1–4): ")
        print("\n" * 3)

        if choice == "1":
            # Look up a single package at a specific time
            try:
                pkg_id = int(input("Enter Package ID (1–40): "))
                time_str = input("Enter time to query (e.g., 08:35 AM): ")
                query_time = datetime.strptime(time_str, "%I:%M %p").replace(year=2024, month=1, day=1)

                package = package_map.search(pkg_id)
                if not package:
                    print("Package not found.")
                    continue

                print(f"\n===== PACKAGE {package.pkg_id} AT {query_time.strftime('%I:%M %p')} =====")
                print(f"Address: {package.get_address_at(query_time)}")
                print(f"City: {package.city}")
                print(f"State: {package.state}")
                print(f"ZIP: {package.pkg_zip}")
                print(f"Deadline: {package.deadline}")
                print(f"Weight: {package.weight} KG")
                if package.departure_time and query_time >= package.departure_time:
                    print(f"Truck: {package.truck}")
                else:
                    print("Truck: N/A")
                print(f"Status: {package.get_status_at(query_time)}")

            except ValueError:
                print("Invalid input. Please enter a number and time in HH:MM AM/PM format.")

        elif choice == "2":
            # View status of all packages at a given time
            try:
                time_str = input("Enter time to query all packages (e.g., 09:30 AM): ")
                query_time = datetime.strptime(time_str, "%I:%M %p").replace(year=2024, month=1, day=1)

                print(f"\n===== ALL PACKAGE STATUSES AT {time_str.upper()} =====")
                for pkg_id in range(1, 41):
                    package = package_map.search(pkg_id)
                    status = package.get_status_at(query_time)
                    print(f"\n--- PACKAGE {pkg_id} ---")
                    print(f"Address: {package.get_address_at(query_time)}")
                    print(f"Deadline: {package.deadline}")
                    print(f"Status: {package.get_status_at(query_time)}")
                    if package.departure_time and query_time >= package.departure_time:
                        print(f"Truck: {package.truck}")
                    else:
                        print("Truck: N/A")

            except ValueError:
                print("Invalid time format. Use HH:MM AM/PM.")

        elif choice == "3":
            # Display mileage for each truck and total mileage
            total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
            print("\n===== TRUCK MILEAGE REPORT =====")
            print(f"Truck 1 mileage: {truck1.mileage:.2f} miles")
            print(f"Truck 2 mileage: {truck2.mileage:.2f} miles")
            print(f"Truck 3 mileage: {truck3.mileage:.2f} miles")
            print("-" * 30)
            print(f"Total mileage: {total_mileage:.2f} miles")



        elif choice == "4":
            # Exit the CLI loop
            print("Goodbye.")
            break

        else:
            # Handle invalid menu selection
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

cli_loop()
