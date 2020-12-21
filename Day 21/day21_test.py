import unittest

from day21 import part1, part2


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2659, part1())

    def test_part2(self):
        self.assertEqual('rcqb,cltx,nrl,qjvvcvz,tsqpn,xhnk,tfqsb,zqzmzl', part2())
