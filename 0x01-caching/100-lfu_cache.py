#!/usr/bin/env python3
"""
Least Frequently Used (LFU) caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class represents a caching system using the Least
    Frequently Used (LFU) eviction policy.

    Attributes:
    - cache_data (OrderedDict): An ordered dictionary to store key-value
    pairs with LFU tracking.
    - frequency_count (defaultdict): A dictionary to store the frequency
    count of each key.

    Methods:
    - put(key, item): Assigns the item value to the dictionary
    self.cache_data for the given key.
      If key or item is None, this method does nothing.
      If the number of items in self.cache_data exceeds
      BaseCaching.MAX_ITEMS, it discards the least frequently used item.
      If more than one item has the same least frequency,
      the LRU algorithm is used to discard the least recently used
      among them.

    - get(key): Returns the value in self.cache_data linked to the
    given key.
      If key is None or the key doesn't exist in self.cache_data,
      it returns None.
      This method updates the frequency count of the accessed key.
    """

    def __init__(self):
        """
        Initializes the LFUCache instance
        """
        super().__init__()
        self.keys = {}

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
        if key is not None and item is not None:
            if key in self.keys:
                self.keys[key] += 1
            else:
                self.keys[key] = 1
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discard = min(self.keys, key=self.keys.get)
                    print("DISCARD: {}".format(discard))
                    self.keys.pop(discard)
                    self.cache_data.pop(discard)
                self.cache_data[key] = item

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
        self.keys[key] += 1
        return self.cache_data[key]
