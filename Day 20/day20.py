from Utils.file_reader import read_chunks
from Utils.debug_tools import debug_print
import math


def edges_match(this_edge, other_edge):
    return this_edge == other_edge or this_edge == other_edge[::-1]


def get_tile(tile_key, tile_map):
    return tile_map[tile_key].split("\n")


def get_top_row(tile):
    return tile[0]


def get_bottom_row(tile):
    return tile[-1]


def get_left_edge(tile):
    return ''.join([row[0] for row in tile])


def get_right_edge(tile):
    return ''.join([row[-1] for row in tile])


def check_match(edge, other_tile):
    return edges_match(edge, get_top_row(other_tile)) \
                or edges_match(edge, get_right_edge(other_tile)) \
                or edges_match(edge, get_bottom_row(other_tile)) \
                or edges_match(edge, get_left_edge(other_tile))

def is_corner(tile_key, tile_map):
    print_stuff = False

    this_tile = get_tile(tile_key, tile_map)
    top_row = get_top_row(this_tile)
    debug_print(print_stuff, "TOP: " + top_row)
    bottom_row = get_bottom_row(this_tile)
    debug_print(print_stuff, "BOTTOM: " + bottom_row)
    left_edge = get_left_edge(this_tile)
    debug_print(print_stuff, "LEFT: " + left_edge)
    right_edge = get_right_edge(this_tile)
    debug_print(print_stuff, "RIGHT: " + right_edge)
    debug_print(print_stuff, "==========")

    top_match = False
    bottom_match = False
    right_match = False
    left_match = False

    for other_tile_key in tile_map.keys():
        if tile_key == other_tile_key:
            continue
        other_tile = get_tile(other_tile_key, tile_map)
        if not top_match:
            top_match = check_match(top_row, other_tile)
        if not bottom_match:
            bottom_match = check_match(bottom_row, other_tile)
        if not left_match:
            left_match = check_match(left_edge, other_tile)
        if not right_match:
            right_match = check_match(right_edge, other_tile)

    debug_print(print_stuff, top_match)
    debug_print(print_stuff, right_match)
    debug_print(print_stuff, bottom_match)
    debug_print(print_stuff, left_match)

    return len([match for match in [top_match, bottom_match, right_match, left_match] if match]) == 2


def part1():
    chunks = read_chunks('Input.txt')
    # print(chunks)
    tile_map = {int(tile[tile.index('Tile ') + 5:tile.index(':\n')]): tile[tile.index(':\n') + 2:] for tile in chunks}

    # print([tile for tile in tile_map.keys() if is_corner(tile, tile_map)])

    print(math.prod([tile for tile in tile_map.keys() if is_corner(tile, tile_map)]))


part1()
