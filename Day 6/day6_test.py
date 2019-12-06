import unittest

from day6 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(344238, part1())

    def test_part2(self):
        self.assertEqual(436, part2())
