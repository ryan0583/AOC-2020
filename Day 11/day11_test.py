import unittest

from day11 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual("2336", str(part1()))

    def test_part2(self):
        self.assertEqual(
            "..	##	..	..	##	..	##	##	##	##	..	..	##	##	..	..	##	##	##	##	..	##	..	..	##	..	##	##	##	..	..	##	..	..	..	..	##	##	##	..	..	..	..\n" \
          + "..	##	..	..	##	..	..	..	..	##	..	##	..	..	##	..	##	..	..	..	..	##	..	##	..	..	##	..	..	##	..	##	..	..	..	..	##	..	..	##	..	..	..\n" \
          + "..	##	..	..	##	..	..	..	##	..	..	##	..	..	##	..	##	##	##	..	..	##	##	..	..	..	##	##	##	..	..	##	..	..	..	..	##	..	..	##	..	..	..\n" \
          + "..	##	..	..	##	..	..	##	..	..	..	##	##	##	##	..	##	..	..	..	..	##	..	##	..	..	##	..	..	##	..	##	..	..	..	..	##	##	##	..	..	..	..\n" \
          + "..	##	..	..	##	..	##	..	..	..	..	##	..	..	##	..	##	..	..	..	..	##	..	##	..	..	##	..	..	##	..	##	..	..	..	..	##	..	..	..	..	##	..\n" \
          + "..	..	##	##	..	..	##	##	##	##	..	##	..	..	##	..	##	##	##	##	..	##	..	..	##	..	##	##	##	..	..	##	##	##	##	..	##	..	..	..	..	..	.." \
            , str(part2()))
