# -*- coding: utf-8 -*-

from . json_key_helper import get_keys


def get_all_keys(data):
    """
    Return a flat list of all keys from the json data along with the
    respective parent key."""
    return get_keys(data)
