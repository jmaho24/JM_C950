# Class for Truck objects.

from datetime import datetime, timedelta

from routing import HUB_ADDRESS


# Class for Truck objects.
class Truck:

    def __init__(self, truck_id, start_time):

        self.truck_id = truck_id            #required at creation
        self.time = start_time              #required at creation

        self.packages = []                  #default empty list
        self.location =HUB_ADDRESS                #default location
        self.mileage = 0.0                  #each truck starts at 0 miles
        self.speed = 18                     #mph value provided by task
        self.max_capacity = 16              #fixed limit of packages per truck


    # Prints truck info.
    def __str__(self):
        return f"Truck: {self.truck_id} | Packages on board: {len(self.packages)}  Mileage: {self.mileage} Time: {self.time.strftime('%I:%M %p')}"


    # Method to add packages.
    def load_package(self, package):
        if len(self.packages) < self.max_capacity:
            self.packages.append(package)
        else:
            print("Truck is at max capacity.")


    # Method to deliver packages.
    def deliver_package(self, package,distance):

        # Update location.
        self.location = package.address
        # Update mileage.
        self.mileage += distance
        # Update package list.
        self.packages.remove(package)


      # Method to update truck time.
    def update_time(self, distance):

        #Calculates travel time in hours.
        travel_time = distance / self.speed
        #Converts hours to minutes.
        minutes = int(travel_time * 60)
        #Adds the time to the truck's time.
        self.time += timedelta(minutes=minutes)

