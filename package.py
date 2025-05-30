# Class for Package objects.

class Package:
    def __init__(self, pkg_id, address, city, state, pkg_zip, deadline, weight,notes,status,delivery_time):


        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.pkg_zip = pkg_zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = delivery_time


    def __str__(self):
        return (
            f"{self.pkg_id},{self.address},{self.city},{self.state},"
            f"{self.pkg_zip},{self.deadline},{self.weight},{self.notes},{self.status},{self.delivery_time}"
        )
