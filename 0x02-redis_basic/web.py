#!/usr/bin/env python3
"""
    Module implementing a function that an expiring web
    tracker
"""
import requests
import redis
import time


redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Returns url content"""
    cached_content = redis_client.get(url)
    if cached_content:
        print(f"Returning cached content for {url}")
        return cached_content.decode('utf-8')

    print(f"Fetching content from {url}")
    response = requests.get(url)
    html_content = response.text

    redis_client.setex(url, 10, html_content)

    redis_client.incr(f"count:{url}")

    return html_content
