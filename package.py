# Class for Package objects.

import datetime

class Package:
    def __init__(self, pkg_id, address, city, state, pkg_zip, deadline, weight,truck,notes):


        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.pkg_zip = pkg_zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = truck
        self.status = None

        # Default status times
        self.available_time = datetime.datetime(2024, 1, 1, 8, 0)
        self.departure_time = None
        self.delivery_time = None



    def __str__(self):

        available_str = self.available_time.strftime("%I:%M %p") if self.available_time else "Available"
        delivery_str = self.delivery_time.strftime("%I:%M %p") if self.delivery_time else "Not Delivered"

        # Custom status wording
        if "Delivered" in self.status and self.truck:
            status_str = f"Delivered by Truck {self.truck} at {delivery_str}"
        else:
            status_str = self.status

        return (
            f"Package {self.pkg_id}:\n"
            f"  Address: {self.address}, {self.city}, {self.state} {self.pkg_zip}\n"
            f"  Status: {status_str}\n"
            f"  Deadline: {self.deadline}\n"
            f"  Weight (KG): {self.weight} | Truck: {self.truck}\n"
            f"  Available Time: {available_str}\n"
            f"  Delivery Time: {delivery_str}\n"
            f"  Notes: {self.notes if self.notes else 'None'}\n")

    def get_status_at(self, query_time):

        if query_time < self.available_time:
            return f"Delayed – Not Yet Available (Available at {self.available_time.strftime('%H:%M')})"
        elif query_time < self.departure_time:
            return "At Hub"
        elif query_time < self.delivery_time:
            return "En Route"
        else:
            return f"Delivered at {self.delivery_time.strftime('%I:%M %p')}"

    def get_address_at(self, query_time):
        if self.pkg_id == 9 and query_time < datetime.datetime(2024, 1, 1, 10, 20):
            return "300 State St (Wrong Address)"
        return self.address

