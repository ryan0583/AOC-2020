import unittest

from day11 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2211, part1())

    def test_part2(self):
        self.assertEqual(1995, part2())
