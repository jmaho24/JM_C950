import csv


from package import Package

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
            status = "AT HUB"
            delivery_time = None

            package = Package(pkg_id, address, city, state, zip_code, deadline, weight,notes, status, delivery_time)

            package_map.insert(pkg_id, package)





