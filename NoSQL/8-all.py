#!/usr/bin/env python3
"""8-all module"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """function that extract all
    document from a collection"""
    my_list = []
    for d in mongo_collection.find():
        my_list.append(d)
    return my_list
