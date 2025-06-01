# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Modified for Key:Value and adapted for use with Package objects in WGUPS simulation.

class ChainingHashTable:
    def __init__(self, initial_capacity=40):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, package):  # handles both insert and update
        # Get the bucket list where this package will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Update key if it already exists in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = package
                return True

        # If not found, insert the new key-value pair
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # Get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # return value (e.g., a Package object)
        return None

    def remove(self, key):
        # Get the bucket list where this package will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the package if present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv)
                return True
        return False

    def __str__(self):
        output = []
        for i, bucket in enumerate(self.table):
            output.append(f"Bucket {i}: {bucket}")
        return "\n".join(output)

    def all_items(self):
        for bucket in self.table:
            if bucket:
                for item in bucket:
                    yield item[0], item[1]
