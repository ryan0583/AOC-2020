def part_one(lines):
    valid_count = 0
    for line in lines:
        line_parts = line.split(":")
        policy = line_parts[0]
        password = line_parts[1]
        letter_counts = policy.split("-")
        max_count_and_letter = letter_counts[1].split(" ")
        min_count = int(letter_counts[0])
        print(min_count)
        max_count = int(max_count_and_letter[0])
        print(max_count)
        letter = max_count_and_letter[1]
        print(letter)
        actual_letter_count = int(password.count(letter))
        print(actual_letter_count)
        if min_count <= actual_letter_count <= max_count:
            valid_count = valid_count + 1
    print(valid_count)


file = open("Input.txt", "r")
rows = file.readlines()
part_one(rows)
