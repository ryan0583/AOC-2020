from Utils.file_reader import read_chunks


def get_any_yes_count(chunk):
    return len(set(chunk.replace("\n", "")))


def get_all_yes_count(chunk):
    def find_common():
        return list(set(person_answers).intersection(common_answers))

    all_person_answers = chunk.split("\n")
    common_answers = all_person_answers[0]

    for person_answers in all_person_answers:
        common_answers = find_common()

    return len(common_answers)


def part1():
    return sum(list(map(get_any_yes_count, read_chunks("Input.txt"))))


def part2():
    return sum(list(map(get_all_yes_count, read_chunks("Input.txt"))))


print(part1())
print(part2())
