import unittest

from day20 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(68781323018729, part1())

    def test_part2(self):
        self.assertEqual(1629, part2())
