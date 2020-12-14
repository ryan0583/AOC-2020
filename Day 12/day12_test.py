import unittest

from day12 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1010, part1())

    def test_part2(self):
        self.assertEqual(52742, part2())
