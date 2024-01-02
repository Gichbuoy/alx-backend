#!/usr/bin/env python3
"""Basic cache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class represents a simple caching system without a size limit.

    Attributes:
    - cache_data (dict): A dictionary to store key-value pairs.

    Methods:
    - put(key, item): Assigns the item value to the dictionary
    self.cache_data for the given key.
      If key or item is None, this method does nothing.

    - get(key): Returns the value in self.cache_data linked to the given key.
      If key is None or the key doesn't exist in self.cache_data, it
      returns None.
    """

    def put(self, key, item):
        """
        Assigns the item value to the dictionary self.cache_data for
        the given key.

        Parameters:
        - key (hashable): The key to be associated with the item.
        - item: The value to be stored in the cache.

        Returns:
        None
        """
        if key and item is not None:
            self.cache_data[key] = item

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

    if __name__ == '__main__':
        my_cache = BasicCache()
        my_cache.print_cache()
        my_cache.put("A", "Hello")
        my_cache.put("B", "World")
        my_cache.put("C", "Holberton")
        my_cache.print_cache()
        print(my_cache.get("A"))
        print(my_cache.get("B"))
        print(my_cache.get("C"))
        print(my_cache.get("D"))
        my_cache.print_cache()
        my_cache.put("D", "School")
        my_cache.put("E", "Battery")
        my_cache.put("A", "Street")
        my_cache.print_cache()
        print(my_cache.get("A"))
