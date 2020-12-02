import unittest

from day2 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(607, part1())

    def test_part2(self):
        self.assertEqual(321, part2())
