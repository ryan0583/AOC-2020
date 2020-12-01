def part_one(lines):
    done = False
    for line1 in lines:
        for line2 in lines:
            result = int(line1) + int(line2)
            if result == 2020:
                print(int(line1) * int(line2))
                done = True
                break
        if done:
            break


def part_two(lines):
    done = False
    for line1 in lines:
        for line2 in lines:
            sum2 = int(line1) + int(line2)
            if sum2 < 2020:
                for line3 in lines:
                    result = sum2 + int(line3)
                    if result == 2020:
                        print(int(line1) * int(line2) * int(line3))
                        done = True
                        break
            if done:
                break
        if done:
            break


file = open("Input.txt", "r")
rows = file.readlines()
part_one(rows)
part_two(rows)
