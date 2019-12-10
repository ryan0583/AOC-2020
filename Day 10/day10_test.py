import unittest

from day10 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual("26, 36: 347", str(part1()))

    def test_part2(self):
        self.assertEqual("8, 29: 318", str(part2()))
