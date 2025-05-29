import csv

# Global structures
distance_matrix = []
address_index = {}

# Automatically load when this file is imported
with open("data/distance_matrix.csv", mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)[1:]  # Skip the first cell, grab address headers

    for i, row in enumerate(reader):
        address = row[0].strip()
        address_index[address] = i

        distances = [float(x) if x else 0.0 for x in row[1:]]
        distance_matrix.append(distances)

# Simple distance lookup function
def get_distance(from_address, to_address):
    from_index = address_index[from_address]
    to_index = address_index[to_address]

    distance = distance_matrix[from_index][to_index]
    if distance == 0.0 and from_index != to_index:
        distance = distance_matrix[to_index][from_index]

    return float(distance)