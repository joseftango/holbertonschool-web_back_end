#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document
    in a collection based on kwargs"""
    my_dict = {}
    for k, v in kwargs.items():
        my_dict[k] = v
    return mongo_collection.insert_one(my_dict)
