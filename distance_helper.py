import csv

def load_distance_data (filepath):

    distance_matrix = []
    address_index = {}

    # Step 1: Read CSV (using csv.reader
    with open(filepath, mode='r') as file:

        reader = csv.reader(file)
        header = next(reader)[1:]  # Skip top-left blank, grab address headers

        for i,row in enumerate(reader):
            address = row[0].strip() # First column = address
            address_index[address] = i # iMap address to row index

            distances = [float(x) if x else 0.0 for x in row[1:]]
            distance_matrix.append(distances)


    return distance_matrix, address_index


def get_distance(from_address, to_address,matrix,address_index):

    from_index = address_index[from_address]
    to_index = address_index[to_address]

    distance = matrix[from_index][to_index]

    #if cell is empty or 0.0, try reverse

    if distance == 0.0 and from_index != to_index:
        distance = matrix[to_index][from_index]

    return float(distance)