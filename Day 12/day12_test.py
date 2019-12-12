import unittest

from day12 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual("7722", str(part1()))

    def test_part2(self):
        self.assertEqual("292653556339368", str(part2()))
