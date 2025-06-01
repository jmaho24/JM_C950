import csv
import datetime
import re

from package import Package
from datetime import datetime

def load_package_data (filepath,package_map):

    with open(filepath, mode='r') as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            pkg_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7] if len(row) > 7 else ""
            truck = None
            package = Package(pkg_id, address, city, state, zip_code, deadline, weight, truck, notes)
            package.available_time = datetime.strptime("08:00 AM", "%I:%M %p").replace(year=2024, month=1, day=1)
            package.status = "At Hub"

            # Look for a delay *and* a time
            if "delayed" in notes.lower():
                match = re.search(r'until (\d{1,2}:\d{2} ?[ap]m)', notes.lower())
                if match:
                    time_str = match.group(1)
                    package.available_time = datetime.strptime(time_str, "%I:%M %p").replace(year=2024, month=1, day=1)
                    package.status = "Delayed – Not Yet Available"

            package_map.insert(pkg_id, package)





