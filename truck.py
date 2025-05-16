# Class for Truck objects.

from package import Package

class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id            #required at creation
        self.time = start_time              #required at creation

        self.packages = []                  #default empty list
        self.location ="Hub"                #default location
        self.mileage = 0.0                  #each truck starts at 0 miles
        self.speed = 18                     #mph value provided by task
        self.max_capacity = 16              #fixed limit of packages per truck

    def __str__(self):
        return f"Truck: {self.truck_id} | Packages on board: {len(self.packages)}  Mileage: {self.mileage} Time: {self.time.strftime('%I:%M %p')}"

    def load_package(self, package):
        if len(self.packages) < self.max_capacity:
            self.packages.append(package)
        else:
            print("Truck is at max capacity.")
