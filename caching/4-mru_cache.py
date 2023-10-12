#!/usr/bin/python3
"""4-mru_cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put function"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data.keys()))
                print(f"DISCARD: {discarded_key}")
                self.cache_data.popitem(last=False)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is not None:
            if key in self.cache_data:
                value = self.cache_data[key]
                self.cache_data.move_to_end(key)
                return value
        return None
