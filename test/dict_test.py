import unittest
from dict import *

class json_search_test(unittest.TestCase):
    def test_id(self):
        self.assertTrue([]!=fetch(f))
    def test_test1(self):
        for i in list1:
            a = i
            b = fetch(f)[a]
            self.assertEqual(type(b), str)

    def test_test2(self):
        self.assertEqual(dict1, fetch(f))