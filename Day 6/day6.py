from Utils.file_reader import read_chunks


def get_yes_count(chunk):
    return len(set(chunk.replace("\n", "")))


def part1():
    return sum(list(map(get_yes_count, read_chunks())))


print(part1())
