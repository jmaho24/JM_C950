import csv
import datetime
import re

from package import Package
from datetime import datetime


# Loads package data from CSV and populates the hash table with Package objects.
# This function parses each row and creates a Package instance with the provided fields.
# It also sets the correct availability and status for delayed packages based on notes.
def load_package_data(filepath, package_map):
    # Open the CSV file containing package data
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Process each row and create a Package object
        for row in reader:
            pkg_id = int(row[0])  # Unique package ID (used as key)
            address = row[1]  # Delivery address
            city = row[2]  # Delivery city
            state = row[3]  # Delivery state
            zip_code = row[4]  # ZIP code
            deadline = row[5]  # Delivery deadline
            weight = row[6]  # Weight of package
            notes = row[7] if len(row) > 7 else ""  # Optional notes (e.g., delays or wrong address)

            truck = None  # Truck assignment will be determined later in the simulation

            # Create the Package object
            package = Package(pkg_id, address, city, state, zip_code, deadline, weight, truck, notes)

            # Default available time is 8:00 AM unless delay is detected
            package.available_time = datetime.strptime("08:00 AM", "%I:%M %p").replace(year=2024, month=1, day=1)
            package.status = "At Hub"

            # Check for delay note and parse the delayed time if present
            if "delayed" in notes.lower():
                # Extract time from notes using regex pattern (e.g., "Delayed until 9:05 am")
                match = re.search(r'until (\d{1,2}:\d{2} ?[ap]m)', notes.lower())
                if match:
                    time_str = match.group(1)
                    package.available_time = datetime.strptime(time_str, "%I:%M %p").replace(year=2024, month=1, day=1)
                    package.status = "Delayed – Not Yet Available"

            # Insert the package into the custom hash map using package ID as the key
            package_map.insert(pkg_id, package)





