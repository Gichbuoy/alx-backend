#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Calculate the start and end indices for a given page and page size.

        Parameters:
        - page (int): The 1-indexed page number.
        - page_size (int): The number of items per page.

        Returns:
        tuple: A tuple containing the start and end indices (1-indexed)
        for the requested page.
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.

        Parameters:
        - page (int): The 1-indexed page number. Default is 1.
        - page_size (int): The number of items per page. Default is 10.

        Returns:
        list: A list containing rows of data for the specified page.
        Empty list if out of range.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = self.index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]
