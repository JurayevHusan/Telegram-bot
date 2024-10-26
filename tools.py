from functools import lru_cache
from fuzzywuzzy import process
from data import m, d

@lru_cache
def search(s):
    """
    Search function does... and that's all.
    :param s: text that should be found
    :return: the most similar 2 elements
    """
    a = process.extract(s, m, limit=10)
    print(s, "=>",a)
    return a
