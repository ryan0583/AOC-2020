import unittest

from day13 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1915, part1())

    def test_part2(self):
        self.assertEqual(294354277694107, part2())
