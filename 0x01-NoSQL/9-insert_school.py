#!/usr/bin/env python3
"""
    Module implementing a function that inserts a new
    document to a collection
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document to a database collection"""
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
