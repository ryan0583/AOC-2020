from Utils.file_reader import read_chunks


def get_any_yes_count(chunk: str) -> int:
    return len(set(chunk.replace("\n", "")))


def get_all_yes_count(chunk: str) -> int:
    return len(set.intersection(*[set(line) for line in chunk.split("\n")]))


def part1():
    return sum([get_any_yes_count(chunk) for chunk in read_chunks("Input.txt")])


def part2():
    return sum([get_all_yes_count(chunk) for chunk in read_chunks("Input.txt")])


print(part1())
print(part2())
