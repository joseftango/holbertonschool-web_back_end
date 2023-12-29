#!/usr/bin/env python3
"""11-schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of
    school having a specific topic"""
    query = mongo_collection.find({"topics": topic})
    my_list = list(query)
    return my_list