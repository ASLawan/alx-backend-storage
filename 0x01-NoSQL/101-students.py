#!/usr/bin/env python3
"""
    Module implementing a function that returns students
    sorted by average score

"""


def top_students(mongo_collection):
    """Returns list of students sorted by average score """
    students = list(mongo_collection.find({}))

    for student in students:
        topics = student.get('topics', [])
        if topics:
            avg_scr = sum(topic['score'] for topic in topics) / len(topics)
            student['averageScore'] = avg_scr
        else:
            student['averageScore'] = 0

    sorted_scores = sorted(students,
                           key=lambda x: x['averageScore'], reverse=True)

    return sorted_scores
