#!/usr/bin/env python3
"""
    Module implementing code that retrieves stats about nginx
    logs

"""
from pymongo import MongoClient


def print_logs():
    """Prints log stats"""
    try:
        client = MongoClient('mongodb://127.0.0.1:27017/')
        db = client['logs']
        collection = db['nginx']
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")
        print("Methods:")
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            count = collection.count_documents({'method': method})
            print(f"\tmethod {method}: {count}")
        get_collection = collection.find({"method": "GET", "path": "/status"})
        count = 0
        for item in get_collection:
            count += 1
        print(f"{count} status check")

        top_IPs = collection.aggregate([
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
            ])
        print("IPs:")
        for ip in top_IPs:
            print(f"\t{ip['_id']}: {ip['count']}")
    except Exception as e:
        print(f"Error as {e}")
    finally:
        client.close()


if __name__ == "__main__":
    print_logs()
