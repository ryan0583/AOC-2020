from Utils.file_reader import read_chunks


def get_any_yes_count(chunk: str) -> int:
    return len(set(chunk.replace("\n", "")))


def get_all_yes_count(chunk: str) -> int:
    return len(set.intersection(*map(set, chunk.split("\n"))))


def part1():
    return sum(list(map(get_any_yes_count, read_chunks("Input.txt"))))


def part2():
    return sum(list(map(get_all_yes_count, read_chunks("Input.txt"))))


if __name__ == '__main__':
    print(part1())
    print(part2())
