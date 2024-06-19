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
