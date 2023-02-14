import unittest
from dict import *

class json_search_test(unittest.TestCase):
    def test_id(self):
        self.assertTrue([]!=fetch(f, key1))

    def test_id_in_dict(self):
        a = fetch(f, key2)
        self.assertTrue(a == "Оптимизация сайта (SEO)")

    def test_asseq(self):
        self.assertEqual(type(fetch(f, key1)),str)