import unittest

from day9 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2204990589, part1())

    def test_part2(self):
        self.assertEqual(50008, part2())
