#!/usr/bin/env python3
"""
    Module implening a function that updates document topics
    based on given name
"""


def update_topics(mongo_collection, name, topics):
    """Updates all document topics based on name provided"""
    updated = mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )
    return updated.modified_count
