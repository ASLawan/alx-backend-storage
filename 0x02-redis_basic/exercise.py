#!/usr/bin/env python3
"""
    Module implementing a Cache class with various function methods.
"""
import redis
import uuid
from typing import Union


class Cache:
    """Instantiates instances of redis client"""
    def __init__(self):
        """initializes the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float, None]:
        """Converts data back to desired format"""
        result = self._redis.get(key)
        if result is None:
            return None
        if fn:
            return fn(result)
        return result

    def get_str(self, key: str) -> Union[str, None]:
        """Returns string"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Returns an integer"""
        return self.get(key, int)
