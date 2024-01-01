#!/usr/bin/env python
"""
function index_range
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    - page (int): The 1-indexed page number.
    - page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start and end indices (1-indexed)
    for the requested page.
    """
    # calculate limit
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return(start_index, end_index)

    if __name__ == '__main__':
        res = index_range(1, 7)
        print(type(res))
        print(res)

        res = index_range(page=3, page_size=15)
        print(type(res))
        print(res)
