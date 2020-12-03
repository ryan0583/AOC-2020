import unittest

from day3 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(252, part1())

    def test_part2(self):
        self.assertEqual(2608962048, part2())
