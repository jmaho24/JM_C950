# Class for Truck objects.

from datetime import datetime, timedelta
from routing import HUB_ADDRESS


# Class for Truck objects.
class Truck:
    """
    Represents a delivery truck used by WGUPS.

    Attributes:
        truck_id (int): Unique identifier for the truck.
        time (datetime): The current time for the truck's simulation.
        packages (list): A list of package objects currently on the truck.
        location (str): The truck's current address location.
        mileage (float): Total distance the truck has traveled.
        speed (int): Speed of the truck in miles per hour (fixed at 18 MPH).
        max_capacity (int): Maximum number of packages the truck can carry (fixed at 16).
    """
    def __init__(self, truck_id, start_time):
        """
        Initializes a Truck object with a unique ID and start time.

        Args:
            truck_id (int): Unique identifier for the truck.
            start_time (datetime): The starting time for the truck's delivery route.
        """
        self.truck_id = truck_id            #required at creation
        self.time = start_time              #required at creation

        self.packages = []                  #default empty list
        self.location =HUB_ADDRESS                #default location
        self.mileage = 0.0                  #each truck starts at 0 miles
        self.speed = 18                     #mph value provided by task
        self.max_capacity = 16              #fixed limit of packages per truck


    def __str__(self):
        """
        Returns a formatted string representation of the truck's current status,
        including ID, number of packages, mileage, and time.

        Returns:
            str: Summary of the truck's status.
        """
        return f"Truck: {self.truck_id} | Packages on board: {len(self.packages)}  Mileage: {self.mileage} Time: {self.time.strftime('%I:%M %p')}"


    # Method to add packages to a truck and set package status to.
    def load_package(self, package):
        """
        Loads a package onto the truck if capacity allows. Also updates the
        package's status, truck assignment, and departure time.

        Args:
            package (Package): The package object to be loaded.
        """
        if len(self.packages) < self.max_capacity:
            self.packages.append(package)

            # Updates package status and departure time.
            package.status = "EN ROUTE"
            package.truck = self.truck_id
            package.departure_time = self.time


        # Prints error message if a package is added to a truck at max capacity.
        else:
            print("Truck is at max capacity.")


    def deliver_package(self, package,distance):
        """
        Delivers a package by updating the truck’s location, mileage, and
        the package’s status and delivery time.

        Args:
            package (Package): The package to be delivered.
            distance (float): Distance traveled from current location to the package’s address.
        """

        # Updates truck location.
        self.location = package.address
        # Updates truck mileage.
        #  self.mileage += distance
        # Updates package delivery time.
        package.delivery_time = self.time
        # Updates package status as delivered with delivery time.
        package.status = f"Delivered at {self.time.strftime('%I:%M %p')}"
        print(f"[Truck {self.truck_id}]: Package {package.pkg_id} to {package.address}   {package.status}")
        # Updates package list.
        self.packages.remove(package)


      # Method to update truck time.
    def update_time(self, distance):
        """
        Advances the truck's internal clock based on the distance traveled
        at the truck's fixed speed (18 MPH).

        Args:
            distance (float): Distance traveled in miles.
        """

        #Calculates travel time in hours.
        travel_time = distance / self.speed
        #Converts hours to minutes.
        minutes = int(travel_time * 60)
        #Adds the time to the truck's time.
        self.time += timedelta(minutes=minutes)

