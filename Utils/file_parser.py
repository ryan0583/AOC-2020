from Utils.file_reader import read_lines
from Utils.point import Point


class FileParser:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def read_points(self, char):
        points = []
        for y, line in enumerate(self.lines):
            for x, this_char in enumerate(line):
                if this_char == char:
                    points.append(Point(x, y))
        return points

    def read_points_map(self, char):
        points = {}
        for y, line in enumerate(self.lines):
            for x, this_char in enumerate(line):
                if this_char == char:
                    points[Point(x, y)] = char
        return points

    def parse_boot_code(self):
        def process_command(command, number):
            if command == ACCUMULATOR:
                return[1, number]
            elif command == JUMP:
                return[number, 0]
            elif command == NO_OP:
                return[1, 0]

        def parse_line(lines, current_instruction, accumulator, processed_lines):
            line = lines[current_instruction]
            command_and_number = line.split(' ')
            command = command_and_number[0]
            number = int(command_and_number[1])
            result = process_command(command, number)
            next_instruction = current_instruction + result[0]
            accumulator += result[1]

            if next_instruction in processed_lines:
                return [1, accumulator]

            if next_instruction >= len(lines):
                return [0, accumulator]

            processed_lines.add(next_instruction)
            return parse_line(lines, next_instruction, accumulator, processed_lines)

        return parse_line(self.lines, 0, 0, {0})

    def replace(self, find, replacement, occurrence_to_replace):
        found = 0
        for i, line in enumerate(self.lines):
            command_and_number = line.split(' ')
            command = command_and_number[0]
            if command == find:
                found += 1
            if found == occurrence_to_replace:
                self.lines[i] = line.replace(find, replacement)
                return True
        return False


ACCUMULATOR = 'acc'
JUMP = 'jmp'
NO_OP = 'nop'
