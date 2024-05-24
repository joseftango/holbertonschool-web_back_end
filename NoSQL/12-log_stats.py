#!/usr/bin/env python3
""" 12-log_states module """
from pymongo import MongoClient


def log_infos() -> None:
    """ logs stored in MongoDB. """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(
        "{} logs".format(
            nginx.count_documents({})
        )
    )

    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({'method': method})
            )
        )

    print(
        "{} status check".format(
            nginx.count_documents({'method': 'GET', 'path': '/status'})
        )
    )


if __name__ == "__main__":
    log_infos()
