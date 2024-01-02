#!/usr/bin/env python3
"""
LIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a caching system using the Last In,
    First Out (LIFO) eviction policy.

    Attributes:
    - cache_data (dict): A dictionary to store key-value pairs.

    Methods:
    - put(key, item): Assigns the item value to the dictionary
    self.cache_data for the given key.
      If key or item is None, this method does nothing.
      If the number of items in self.cache_data exceeds
      BaseCaching.MAX_ITEMS, it discards the last item (LIFO).

    - get(key): Returns the value in self.cache_data linked to
    the given key.
      If key is None or the key doesn't exist in self.cache_data,
      it returns None.
    """

    def __init__(self):
        """ Initiliazes the LIFOChache instance """
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
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(-2)
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """
        Returns the value in self.cache_data linked to the given key.

        Parameters:
        - key (hashable): The key associated with the desired value.

        Returns:
        - The value linked to the key if it exists, None otherwise.
        """
        return self.cache_data.get(key, None)
