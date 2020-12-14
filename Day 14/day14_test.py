import unittest

from day14 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(15172047086292, part1())

    def test_part2(self):
        self.assertEqual(4197941339968, part2())
