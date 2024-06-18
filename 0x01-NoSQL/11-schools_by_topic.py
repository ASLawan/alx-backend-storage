#!/usr/bin/env python3
"""
    Module with function that returns all schools with given name

"""


def schools_by_topic(mongo_collection, topic):
    """Returns all the schools with given topic"""
    schools = mongo_collection.find({'topics': topic})
    # schools = [school['name'] for school in cursor]
    return schools
