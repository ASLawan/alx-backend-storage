#!/usr/bin/env python3
"""
    Module implementing code that retrieves stats about nginx
    logs

"""
from pymongo import MongoClient


try:
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['logs']
    collection = db['nginx']
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    space = " " * 4
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"{space}method {method}: {count}")
    get_collection = collection.find({"method": "GET", "path": "/status"})
    count = 0
    for item in get_collection:
        count += 1
    print(f"{count} status check")
except Exception as e:
    print(f"Error as {e}")
finally:
    client.close()
