import unittest

from day7 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(246, part1())

    def test_part2(self):
        self.assertEqual(2976, part2())
