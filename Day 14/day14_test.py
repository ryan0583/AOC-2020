import unittest

from day14 import part1, part2


class Test(unittest.TestCase):

    def test_part1_example1(self):
        self.assertEqual("31", str(part1("testinput.txt")))

    def test_part1_example2(self):
        self.assertEqual("165", str(part1("testinput2.txt")))

    def test_part1_example3(self):
        self.assertEqual("13312", str(part1("testinput3.txt")))

    def test_part1_example4(self):
        self.assertEqual("180697", str(part1("testinput4.txt")))

    def test_part1_example5(self):
        self.assertEqual("2210736", str(part1("testinput5.txt")))

    def test_part1_example6(self):
        self.assertEqual("1", str(part1("testinput6.txt")))

    def test_part1_real(self):
        self.assertEqual("741927", str(part1("input.txt")))

    def test_part2_example5(self):
        self.assertEqual("460664", str(part2("testinput5.txt")))
