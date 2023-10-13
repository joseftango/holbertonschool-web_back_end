#!/usr/bin/env python3
"""2-hypermedia_pagination module"""
import csv
import math
from typing import Tuple, List, Dict, Union


class Server:
    """Server class"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset function"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """index_range function"""
        end: int = page * page_size
        start: int = 0
        for i in range(page - 1):
            start += page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page function"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(dataset):
            return []
        return [list(dataset[row]) for row in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List], None, int]]:
        """get_hyper function"""
        data: List = self.get_page(page, page_size)
        size_dataset: int = len(self.dataset())
        totalPage = math.ceil(size_dataset / page_size)
        if page - 1 == 0:
            prev_page = None
        else:
            prev_page = page - 1

        if page + 1 > size_dataset or data == []:
            next_page = None
        else:
            next_page = page + 1

        if data is not []:
            pageSize = page_size

        hateoas: Dict = {'page_size': pageSize,
                         'page': page,
                         'data': data,
                         'next_page': next_page,
                         'prev_page': prev_page,
                         'total_pages': totalPage}
        return hateoas
