import unittest

from day8 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1206, part1())

    def test_part2(self):
        expected = \
              "########      ####  ######      ####    ######    \n" \
            + "##              ##  ##    ##  ##    ##  ##    ##  \n" \
            + "######          ##  ##    ##  ##        ##    ##  \n" \
            + "##              ##  ######    ##  ####  ######    \n" \
            + "##        ##    ##  ##  ##    ##    ##  ##        \n" \
            + "########    ####    ##    ##    ######  ##        \n"
        self.assertEqual(expected, part2())
