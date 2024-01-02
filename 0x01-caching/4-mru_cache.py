#!/usr/bin/env python3
"""
Most Recently Used Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class represents a caching system using the
    Most Recently Used (MRU) eviction policy.

    Attributes:
    - cache_data (OrderedDict): An ordered dictionary to store
    key-value pairs with MRU tracking.

    Methods:
    - put(key, item): Assigns the item value to the dictionary
    self.cache_data for the given key.
      If key or item is None, this method does nothing.
      If the number of items in self.cache_data exceeds
      BaseCaching.MAX_ITEMS, it discards the most recently used item.

    - get(key): Returns the value in self.cache_data linked to the given key.
      If key is None or the key doesn't exist in self.cache_data,
      it returns None.
      This method updates the order of the accessed key, marking it as
      the most recently used.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance
        """
        super().__init__()
        self.mru = []

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
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru.remove(key)
        self.cache_data[key] = item
        self.mru.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.mru.pop(-2)
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
        if key is None or key not in self.cache_data:
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]
