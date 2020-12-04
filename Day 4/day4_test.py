import unittest

from day4 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(192, part1())

    def test_part2(self):
        self.assertEqual(101, part2())
