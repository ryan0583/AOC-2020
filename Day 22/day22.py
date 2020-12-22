from Utils.file_reader import read_lines


def read_hands():
    lines = read_lines('Input.txt')
    player2_index = lines.index('Player 2:')
    player1_cards = [int(line) for line in lines[1:player2_index - 1]]
    player2_cards = [int(line) for line in lines[player2_index + 1:]]
    return [player1_cards, player2_cards]


def part1():
    def round():
        player1_top_card = player1_cards.pop(0)
        player2_top_card = player2_cards.pop(0)
        if player1_top_card > player2_top_card:
            player1_cards.append(player1_top_card)
            player1_cards.append(player2_top_card)
        else:
            player2_cards.append(player2_top_card)
            player2_cards.append(player1_top_card)

    [player1_cards, player2_cards] = read_hands()

    while len(player1_cards) > 0 and len(player2_cards) > 0:
        round()

    result = 0
    winning_hand = (player1_cards if len(player1_cards) > 0 else player2_cards)[::-1]
    print(winning_hand)

    for index, card in enumerate(winning_hand):
        result += (index + 1) * card

    print(result)


part1()
