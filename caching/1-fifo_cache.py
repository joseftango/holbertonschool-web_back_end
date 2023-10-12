#!/usr/bin/python3
"""1-fifo_cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
