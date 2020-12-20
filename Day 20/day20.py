from Utils.file_reader import read_chunks
from Utils.debug_tools import debug_print
import math


class Tile:
    def __init__(self, index, image):
        self.index = index
        self.image = image
        self.top_match = None
        self.right_match = None
        self.bottom_match = None
        self.left_match = None

    def get_match_count(self):
        match_list = [self.top_match, self.right_match, self.bottom_match, self.left_match]
        match_list.remove(None)
        return len(match_list)


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


def populate_edge_matches(tile, other_tiles):
    tile_image = tile.image
    top_row = get_top_row(tile_image)
    bottom_row = get_bottom_row(tile_image)
    left_edge = get_left_edge(tile_image)
    right_edge = get_right_edge(tile_image)

    top_match = False
    bottom_match = False
    right_match = False
    left_match = False

    for other_tile in other_tiles:
        if tile.index == other_tile.index:
            continue
        if not top_match:
            top_match = check_match(top_row, other_tile)
            if top_match:
                tile_image.top_match = other_tile
        if not bottom_match:
            bottom_match = check_match(bottom_row, other_tile)
            if bottom_match:
                tile_image.bottom_match = other_tile
        if not left_match:
            left_match = check_match(left_edge, other_tile)
            if left_match:
                tile_image.left_match = other_tile
        if not right_match:
            right_match = check_match(right_edge, other_tile)
            if right_match:
                tile_image.right_match = other_tile


def part1():
    chunks = read_chunks('Input.txt')

    tiles = [Tile(int(tile[tile.index('Tile ') + 5:tile.index(':\n')]), tile[tile.index(':\n') + 2:]) for tile in
             chunks]

    for tile in tiles:
        populate_edge_matches(tile, tiles)

    corner_indexes = [tile.index for tile in tiles if tile.get_match_count() == 2]

    print(math.prod(corner_indexes))


def part2():
    chunks = read_chunks('TestInput.txt')

    tiles = [Tile(int(tile[tile.index('Tile ') + 5:tile.index(':\n')]), tile[tile.index(':\n') + 2:]) for tile in
             chunks]

    tile_map = {tile.index: tile.image for tile in tiles}

    corners = [tile for tile in tile_map.keys() if is_corner(tile, tile_map)]

    print(corners)

    sides = [tile for tile in tile_map.keys() if is_side(tile, tile_map)]

    print(sides)

    middle = [tile for tile in tile_map.keys() if tile not in sides and tile not in corners]

    print(middle)


part1()
# part2()
