# Importing Os module
import os
from typing import List


def list_dir(loc):
    """
    This function will take input path as type str, use / to avoid errors
    """
    temp_list: List[str] = []
    for item in os.listdir(loc):
        str_len = len(item)
        if item[(str_len - 4):] == '.pdf':
            temp_list.append(item)
    return loc, temp_list
