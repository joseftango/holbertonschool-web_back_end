#!/usr/bin/python3
""" 0-basic_cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
