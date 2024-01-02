#!/usr/bin/env python3
"""
FIFO cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class represents a caching system using the First In,
    First Out (FIFO) eviction policy.

    Attributes:
    - cache_data (dict): A dictionary to store key-value pairs.

    Methods:
    - put(key, item): Assigns the item value to the dictionary
    self.cache_data for the given key.
      If key or item is None, this method does nothing.
      If the number of items in self.cache_data exceeds
      BaseCaching.MAX_ITEMS, it discards the first item (FIFO).

    - get(key): Returns the value in self.cache_data linked to
    the given key.
      If key is None or the key doesn't exist in self.cache_data,
      it returns None.
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance,
        calling the parent's __init__ method.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assigns the item value to the dictionary self.cache_data
        for the given key.

        Parameters:
        - key (hashable): The key to be associated with the item.
        - item: The value to be stored in the cache.

        Returns:
        None
        """
        if key and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        Returns the value in self.cache_data linked to the given key.

        Parameters:
        - key (hashable): The key associated with the desired value.

        Returns:
        - The value linked to the key if it exists, None otherwise.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
