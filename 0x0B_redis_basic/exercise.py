#!/usr/bin/env python3
"""exercice module"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache():
    """class named Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Callable = None) -> Union[str, bytes, int, float]:
        """take a key string argument and an optional Callable"""
        my_key = self._redis.get(key)
        if my_key is not None:
            if fn is not None:
                return fn(my_key)
            else:
                return my_key
        return None

    def get_str(self, key: str) -> str:
        """get str function"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """get int function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value

def count_calls(method: Callable = None) -> Callable:
    """count_calls function"""
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper
