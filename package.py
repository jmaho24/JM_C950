# Class for Package objects.

import datetime

class Package:
    """
    Represents a delivery package with full tracking and status functionality
    for the WGUPS delivery simulation.
    """

    def __init__(self, pkg_id, address, city, state, pkg_zip, deadline, weight,truck,notes):
        """
        Initializes a Package object with full delivery details and tracking status.

        Args:
            pkg_id (int): Unique package identifier (used as the hash table key).
            address (str): Delivery street address.
            city (str): City of delivery.
            state (str): State of delivery.
            pkg_zip (str): ZIP code for delivery.
            deadline (str): Delivery deadline (e.g., "EOD", "10:30 AM").
            weight (str): Weight of the package in kilograms.
            truck (int): Truck number assigned for delivery.
            notes (str): Any special instructions or notes (e.g., delays, wrong address).
        """

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
        """
        Returns a human-readable string summarizing the package details,
        including address, deadline, status, and assigned truck.
        """
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
        """
        Returns the delivery status of the package at a specific time in the simulation.

        Args:
            query_time (datetime): The simulation time to check status at.

        Returns:
            str: A string indicating if the package is Delayed, At Hub, En Route, or Delivered.
        """

        # Handle delayed packages
        if "delayed" in self.notes.lower():
            if query_time < self.available_time:
                return f"Delayed – Not Yet Available (Available at {self.available_time.strftime('%I:%M %p')})"

        # If query is before package becomes available, but it's not delayed
        if query_time < self.available_time:
            return "At Hub"

        if query_time < self.departure_time:
            return "At Hub"
        elif query_time < self.delivery_time:
            return "En Route"
        else:
            return f"Delivered at {self.delivery_time.strftime('%I:%M %p')}"

    def get_address_at(self, query_time):
        """
        Returns the package address at a specific time. This is used to handle address corrections
        (e.g., package 9's wrong address before 10:20 AM).

        Args:
            query_time (datetime): The simulation time to check the address at.

        Returns:
            str: The address to use at that moment in time.
        """

        if self.pkg_id == 9 and query_time < datetime.datetime(2024, 1, 1, 10, 20):
            return "300 State St (Wrong Address)"
        return self.address

