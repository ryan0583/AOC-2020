import unittest

from day6 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(6521, part1())

    def test_part2(self):
        self.assertEqual(3305, part2())
