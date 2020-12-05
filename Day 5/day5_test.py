import unittest

from day5 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(991, part1())

    def test_part2(self):
        self.assertEqual(534, part2())
