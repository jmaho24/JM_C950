"""
distance_helper.py

Provides functionality for loading and accessing delivery distances between addresses.
This module loads a distance matrix from a CSV file and offers a function to look up
the distance between any two addresses using their indices.

Used globally by the routing simulation for delivery optimization.
"""

import csv

# Global data structures for address-distance lookup
distance_matrix = []
address_index = {}

# Automatically load distance matrix and address mapping from CSV
# This block runs as soon as this module is imported
with open("data/distance_matrix.csv", mode='r') as file:
    reader = csv.reader(file)

    # Skip the header label in top-left corner, extract just the addresses from the top row
    header = next(reader)[1:]

    for i, row in enumerate(reader):
        address = row[0].strip()  # First cell of each row is the delivery address
        address_index[address] = i  # Map that address to its row index in the matrix

        # Convert rest of row (distances to other addresses) into floats
        # Empty cells are converted to 0.0 for symmetry lookups later
        distances = [float(x) if x else 0.0 for x in row[1:]]
        distance_matrix.append(distances)  # Append the cleaned row into the 2D matrix


def get_distance(from_address, to_address):
    """
    Looks up the distance between two addresses using their positions in the matrix.

    Handles symmetry by checking both (A → B) and (B → A) in case one is missing.

    Args:
        from_address (str): Starting location
        to_address (str): Destination location

    Returns:
        float: Distance in miles between the two addresses
    """
    from_index = address_index[from_address]  # Lookup index of starting address
    to_index = address_index[to_address]  # Lookup index of destination address

    # Try direct lookup in the matrix
    distance = distance_matrix[from_index][to_index]

    # If entry is missing (common due to lower-triangle storage), check reverse direction
    if distance == 0.0 and from_index != to_index:
        distance = distance_matrix[to_index][from_index]

    return float(distance)
