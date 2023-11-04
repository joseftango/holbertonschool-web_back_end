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


def call_history(method: Callable) -> Callable:
    """call hystory"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input_str)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(method: Callable):
    """ func """
    key = method.__qualname__
    input = key + ":inputs"
    output = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    lstIn = redis.lrange(input, 0, -1)
    lstOut = redis.lrange(output, 0, -1)
    zip = list(zip(lstIn, lstOut))
    for k, v in zip:
        attr, data = k.decode("utf-8"), v.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
