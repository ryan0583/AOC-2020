from Utils.file_reader import read_lines


def read_hands():
    lines = read_lines('Input.txt')
    player2_index = lines.index('Player 2:')
    player1_cards = [int(line) for line in lines[1:player2_index - 1]]
    player2_cards = [int(line) for line in lines[player2_index + 1:]]
    return [player1_cards, player2_cards]


def part1_game(player1_cards, player2_cards):
    def play_round():
        player1_top_card = player1_cards.pop(0)
        player2_top_card = player2_cards.pop(0)
        if player1_top_card > player2_top_card:
            player1_cards.append(player1_top_card)
            player1_cards.append(player2_top_card)
        else:
            player2_cards.append(player2_top_card)
            player2_cards.append(player1_top_card)

    while len(player1_cards) > 0 and len(player2_cards) > 0:
        play_round()


def part1():
    [player1_cards, player2_cards] = read_hands()

    part1_game(player1_cards, player2_cards)

    result = 0
    winning_hand = (player1_cards if len(player1_cards) > 0 else player2_cards)[::-1]
    print(winning_hand)

    for index, card in enumerate(winning_hand):
        result += (index + 1) * card

    print(result)


def part2_game(player1_cards, player2_cards, game_number):
    def play_round():
        player1_top_card = player1_cards.pop(0)
        player2_top_card = player2_cards.pop(0)

        this_round_cards = (player1_top_card, player2_top_card)
        if this_round_cards in previous_rounds_cards:
            return 1
        else:
            previous_rounds_cards.add(this_round_cards)

        if len(player1_cards) < player1_top_card or len(player2_cards) < player2_top_card:
            if player1_top_card > player2_top_card:
                round_winning_player = 1
            else:
                round_winning_player = 2
        else:
            round_winning_player = part2_game(player1_cards[:player1_top_card], player2_cards[:player2_top_card], game_number + 1)

        if round_winning_player == 1:
            player1_cards.append(player1_top_card)
            player1_cards.append(player2_top_card)
        else:
            player2_cards.append(player2_top_card)
            player2_cards.append(player1_top_card)

        return 0

    print('GAME: ' + str(game_number))
    winning_player = 0
    previous_rounds_cards = set()
    round_number = 1
    while winning_player == 0:
        print('ROUND: ' + str(round_number))
        winning_player = play_round()
        if winning_player == 0:
            if len(player1_cards) == 0:
                winning_player = 2
            if len(player2_cards) == 0:
                winning_player = 1
        round_number += 1

    return winning_player


def part2():
    [player1_cards, player2_cards] = read_hands()

    winning_player = part2_game(player1_cards, player2_cards, 1)

    result = 0
    winning_hand = (player1_cards if winning_player == 1 else player2_cards)[::-1]
    print(winning_hand)

    for index, card in enumerate(winning_hand):
        result += (index + 1) * card

    print(result)


# part1()
part2()
