import unittest

from day4 import meets_criteria_two


class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(meets_criteria_two("112233"))

    def test2(self):
        self.assertFalse(meets_criteria_two("123444"))

    def test3(self):
        self.assertFalse(meets_criteria_two("123443"))

    def test4(self):
        self.assertTrue(meets_criteria_two("112222"))

    def test5(self):
        self.assertTrue(meets_criteria_two("577788"))

    def test6(self):
        self.assertFalse(meets_criteria_two("111111"))

    def test7(self):
        self.assertFalse(meets_criteria_two("122222"))

    def test8(self):
        self.assertFalse(meets_criteria_two("234444"))


if __name__ == '__main__':
    unittest.main()
