# -*- coding: utf-8 -*-

"""
test_json_keys
----------------------

Tests of the `json_key_helper` module.

"""

import unittest

from json_keys.json_key_helper import get_keys


class TestJsonKeys(unittest.TestCase):
    """
    Tests for json_key_helper

    """
    def setUp(self):
        self.data = open('tests/test_data/test.json')

    def test_get_all_keys_from_json(self):
        """
        When a memoized property has not been accessed, the decorated loading function should not
        have been called.
        """
        all_keys = get_keys(self.data)
        expected_keys = [(u'batters', [u'batter']), (None, [u'topping', u'name', u'batters', u'ppu', u'type', u'id'])]
        self.data.close()
        self.assertEqual(all_keys, expected_keys)


if __name__ == '__main__':
    unittest.main()
