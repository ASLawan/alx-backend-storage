#!/usr/bin/env python3
"""
    Module with function that lists all documents from
    a collection
"""


def list_all(mongo_collection):
    """Lists all documents from a collection"""
    cursor = mongo_collection.find({})
    documents = list(cursor)
    return documents
