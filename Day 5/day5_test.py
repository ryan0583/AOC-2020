import unittest

from day5 import process_instruction


class Test(unittest.TestCase):

    def test_instruction_processing_1char(self):
        instruction = process_instruction("1")
        self.assertEqual("1", instruction.get_opcode())
        self.assertEqual("0", instruction.get_param1_mode())
        self.assertEqual("0", instruction.get_param2_mode())

    def test_instruction_processing_2char(self):
        instruction = process_instruction("01")
        self.assertEqual("1", instruction.get_opcode())
        self.assertEqual("0", instruction.get_param1_mode())
        self.assertEqual("0", instruction.get_param2_mode())

    def test_instruction_processing_3char(self):
        instruction = process_instruction("101")
        self.assertEqual("1", instruction.get_opcode())
        self.assertEqual("1", instruction.get_param1_mode())
        self.assertEqual("0", instruction.get_param2_mode())

    def test_instruction_processing_4char(self):
        instruction = process_instruction("1101")
        self.assertEqual("1", instruction.get_opcode())
        self.assertEqual("1", instruction.get_param1_mode())
        self.assertEqual("1", instruction.get_param2_mode())
