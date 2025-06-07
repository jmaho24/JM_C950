# Author: John Mahon
# Student ID: 001193994
# Title: C950 Task 2
# Description: Custom chaining hash table for WGUPS package storage

# Source Reference:
# Adapted from: C950 Webinar 1 – “Let’s Go Hashing” by Dr. Cemal Tepe (2020)
# Based on zyBooks Figure 7.8.2: Hash Table using Chaining
# File: W-1_ChainingHashTable_zyBooks_Key-Value.py (referenced in webinar)
# Modifications: Adjusted for storing Package objects, using WGUPS package IDs as keys


class ChainingHashTable:
    """Implements a hash table with separate chaining for collision resolution.

    Each bucket is a list that can hold multiple key-value pairs,
    allowing multiple items to be stored even if they hash to the same index.
    """

    def __init__(self, initial_capacity=40):
        """Initializes the hash table with a given number of empty buckets."""
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, package):
        """Inserts a new key-value pair or updates the value if the key exists.

        Args:
            key: The package ID (used to generate the hash).
            package: The package object to store.
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = package
                return True

        key_value = [key, package]
        bucket_list.append(key_value)
        return True


    def remove(self, key):
        """Removes the key-value pair associated with the given key.

        Args:
            key: The package ID to remove.

        Returns:
            True if the key was found and removed, False otherwise.
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv)
                return True
        return False
    def search(self, key):
        """Searches for and returns the value associated with the given key.

        Args:
            key: The package ID to search for.

        Returns:
            The package object if found, or None if not found.
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None
    def __str__(self):
        """Returns a string representation of the hash table for debugging."""
        output = []
        for i, bucket in enumerate(self.table):
            output.append(f"Bucket {i}: {bucket}")
        return "\n".join(output)

    def all_items(self):
        """Generator that yields all key-value pairs stored in the hash table."""
        for bucket in self.table:
            if bucket:
                for item in bucket:
                    yield item[0], item[1]
