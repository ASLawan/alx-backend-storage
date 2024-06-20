#!/usr/bin/env python3
"""
    Module implementing a Cache class with various function methods.
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Returns number of times a method has been called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Keeps a history of the called functions"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable):
    """Returns history of calls for a partyn method"""
    def wrapper(instance: Cache):
        """Wrapper function"""
        method_name = method.__qualname__
        input_keys = f"{method_name}:inputs"
        output_keys = f"{method_name}:outputs"

        inputs = instance._redis.lrange(input_keys, 0, -1)
        outputs = instance._redis.lrange(output_keys, 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")

        for inp, out in zip(inputs, outputs):
            arg_str = inp.decode('utf-8')
            output_key = out.decode('utf-8')
            print(f"{method_name}(*{arg_str}) -> {output_key}")
    return wrapper


class Cache:
    """Instantiates instances of redis client"""
    def __init__(self):
        """initializes the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
