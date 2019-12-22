def deal_new_stack(deck):
    new_stack = list(deck)
    new_stack.reverse()
    return new_stack


def cut(deck, cut_point):
    cut_deck = []
    if cut_point > 0:
        cut_deck.extend(deck[cut_point:])
        cut_deck.extend(deck[0:cut_point])
    else:
        cut_deck.extend(deck[len(deck) + cut_point:])
        cut_deck.extend(deck[0:len(deck) + cut_point])

    return cut_deck


def deal_with_increment(deck, increment):
    new_stack = list(deck)
    stack_pos = 0
    for card in deck:
        new_stack[stack_pos] = card
        stack_pos += increment
        if stack_pos >= len(deck):
            stack_pos -= len(deck)

    return new_stack


def part1():
    deck = list(range(0, 10007))

    instructions = open("input.txt", "r").readlines()

    for instruction in instructions:
        instruction = instruction.strip()
        if "new stack" in instruction:
            deck = deal_new_stack(deck)
        elif "increment" in instruction:
            words = instruction.split(" ")
            increment = int(words[len(words) - 1])
            deck = deal_with_increment(deck, increment)
        elif "cut" in instruction:
            words = instruction.split(" ")
            cut_point = int(words[len(words) - 1])
            deck = cut(deck, cut_point)
        else:
            print("Unrecognised Instruction - " + instruction)

    print(deck)

    for i, card in enumerate(deck):
        if card == 2019:
            print(i)


def part2():
    deck = list(range(0, 5965785875702))

    print(deck)

    instructions = open("input.txt", "r").readlines()

    for i in range(0, 101741582076661):
        print(i)
        for instruction in instructions:
            instruction = instruction.strip()
            if "new stack" in instruction:
                deck = deal_new_stack(deck)
            elif "increment" in instruction:
                words = instruction.split(" ")
                increment = int(words[len(words) - 1])
                deck = deal_with_increment(deck, increment)
            elif "cut" in instruction:
                words = instruction.split(" ")
                cut_point = int(words[len(words) - 1])
                deck = cut(deck, cut_point)
            else:
                print("Unrecognised Instruction - " + instruction)

    # print(deck)

    print(deck[2020])

# part1()
part2()
