from Utils.file_reader import read_lines
import re


def get_regex(rule, rule_map, depth):
    # print(rule)
    regex = ''

    if rule == 'a' or rule == 'b':
        regex = rule
    else:
        if depth > 13:
            return regex

        if '|' in rule:
            regex += '('
        rule_entries = [entry for entry in rule.split(' ')]
        for entry in rule_entries:
            if entry == '|':
                regex += entry
            else:
                regex += get_regex(rule_map[int(entry)], rule_map, depth + 1)
        if '|' in rule:
            regex += ')'

    return regex


def part1():
    lines = [line.replace('\n', '').replace('"', '') for line in read_lines("Input.txt")]
    rule_end_index = lines.index('')
    rules = lines[:rule_end_index]
    rule_map = {int(line.split(': ')[0]): line.split(': ')[1] for line in rules}
    regex = re.compile('^' + get_regex(rule_map[0], rule_map, 0) + '$')
    lines_to_validate = lines[rule_end_index + 1:]
    print(len([match for match in lines_to_validate if regex.match(match)]))


def part2():
    lines = [line.replace('\n', '').replace('"', '') for line in read_lines("Input.txt")]
    rule_end_index = lines.index('')
    rules = lines[:rule_end_index]
    rule_map = {int(line.split(': ')[0]): line.split(': ')[1] for line in rules}
    rule_map[8] = '42 | 42 8'
    rule_map[11] = '42 31 | 42 11 31'
    regex = re.compile('^' + get_regex(rule_map[0], rule_map, 0) + '$')
    lines_to_validate = lines[rule_end_index + 1:]
    print(len([match for match in lines_to_validate if regex.match(match)]))


# part1()
part2()
