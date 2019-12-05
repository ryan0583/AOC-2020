import unittest

from day5 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(6761139, part1())

    def test_part2(self):
        self.assertEqual(9217546, part2())
