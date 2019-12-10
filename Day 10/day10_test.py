import unittest

from day10 import part1


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual("26, 36: 347", str(part1()))

    # def test_part2(self):
    #     self.assertEqual(50008, part2())
