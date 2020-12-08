import unittest

from day8 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1928, part1())

    def test_part2(self):
        self.assertEqual(1319, part2())
