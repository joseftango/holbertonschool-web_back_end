#!/usr/bin/python3
"""2-lifo_cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class named LIFOCache"""
    def __init__(self):
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.lifo.pop()
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.lifo.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
