# Class for Package objects.

class Package:
    def __init__(self, pkg_id, address, city, state, pkg_zip, deadline, weight,truck,notes,status,available_time,delivery_time):


        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.pkg_zip = pkg_zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = truck
        self.status = status
        self.available_time = available_time
        self.delivery_time = delivery_time

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
