# -*- coding: utf-8 -*-
import json


def get_keys(data):
    """
    Return a list of tuples. Each tuple has 2 elements, the parent and a list of children keys.
    example:
    --------
    data = {'a': 'apple',
            'b': 'bat',
            'c': {
                 'first': 'rose',
                 'second': "magnolia",
                 'third': {
                     "month": "December",
                     "day": "Monday"
                 }
             }
         }
    Return:
    -------
    [(None, ['a', 'b', 'c']), ('c', ['first', 'second', 'third']), ('third', ['month, 'day'])]
    """
    data = json.load(data)
    return get_keys_recurse(None, data, [])


def get_keys_recurse(parent, children, flattened_keys):
    """
    Return a list of keys for each parent from the entire data recursively.
    Args:
    -----
    parent: parent key, starts with None for the outer most structure
    children : value for the parent key
    flattened_keys : list which contains all the keys.
    """
    keys = children.keys()
    current_children = []
    for key in keys:
        # iterate through the keys of the children and if a value is a dict, then recursively call this again
        if isinstance(children[key], dict):
            current_children.append(key)
            get_keys_recurse(key, children[key], flattened_keys)
        else:
            current_children.append(key)
    flattened_keys.append((parent, current_children))
    return flattened_keys

