import unittest

from day1 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1013211, part1())

    def test_part2(self):
        self.assertEqual(13891280, part2())
