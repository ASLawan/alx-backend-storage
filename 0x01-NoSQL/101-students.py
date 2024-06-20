#!/usr/bin/env python3
"""
    Module implementing a function that returns students
    sorted by average score

"""


def top_students(mongo_collection):
    """Returns list of students sorted by average score """
    pipeline = [
            {
                "$addFields":{
                    "averageScore": {
                        "$avg": "$scores.score"
                        }
                    }
            },
            {
                "$sort": {
                    "averageScore": -1
                    }
                }
            ]
    cursor = mongo_collection.aggregate(pipeline)
    students = list(cursor)
    return students
