#!/usr/bin/env python3
"""3-hypermedia_del_pagination module"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = {}

    def dataset(self) -> List[List]:
        """dataset method"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index method """
        items = len(self.dataset())
        total_pages = math.ceil(items / page_size)

        if index is None or index < 0 or index >= total_pages:
            return {
                "page_size": page_size,
                "page": 0,
                "total_pages": total_pages,
                "page_size": 0,
                "items": items,
                "start_index": 0
            }

        start_index = index * page_size
        page = start_index // page_size + 1
        next_index = (index + 1) if (index + 1) < total_pages else None
    
        if index is not None and index in self.__indexed_dataset:
            del self.__indexed_dataset[index]

        return {
            "page_size": page_size,
            "page": page,
            "total_pages": total_pages,
            "items": items,
            "start_index": start_index,
            "next_index": next_index
        }

    def indexed_dataset(self) -> Dict[int, List]:
        """indexed_dataset method"""
        items = len(self.dataset())
        indexed_data = {}
        for i in range(items):
            indexed_data[i] = self.dataset()[i]
        return indexed_data
