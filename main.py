# Required for handling start time
from datetime import datetime

# Core classes
from truck import Truck
from package import Package

# HashMap to store and look up packages

# CSV loading logic
from load_data import load_package_data  # or basic_load_packages if you're still using that

import load_data

load_data.load_package_data("data/package_data.csv")

truck1 = Truck(truck_id=1, start_time=datetime.strptime("08:00 AM", "%I:%M %p"))

truck1.load_package(1)
truck1.load_package(2)
truck1.load_package(3)

truck1.__str__()


