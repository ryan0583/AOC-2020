from Utils.file_reader import read_chunks
from Utils.debug_tools import debug_print
import math
from pprint import pprint


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
        return len([match for match in match_list if match is not None])


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
    return edges_match(edge, get_top_row(other_tile.image)) \
           or edges_match(edge, get_right_edge(other_tile.image)) \
           or edges_match(edge, get_bottom_row(other_tile.image)) \
           or edges_match(edge, get_left_edge(other_tile.image))


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
                tile.top_match = other_tile
        if not bottom_match:
            bottom_match = check_match(bottom_row, other_tile)
            if bottom_match:
                tile.bottom_match = other_tile
        if not left_match:
            left_match = check_match(left_edge, other_tile)
            if left_match:
                tile.left_match = other_tile
        if not right_match:
            right_match = check_match(right_edge, other_tile)
            if right_match:
                tile.right_match = other_tile


def get_tiles():
    chunks = read_chunks('TestInput.txt')

    tiles = [Tile(int(tile[tile.index('Tile ') + 5:tile.index(':\n')]), tile[tile.index(':\n') + 2:].split('\n'))
             for tile in chunks]

    for tile in tiles:
        populate_edge_matches(tile, tiles)

    return tiles


def part1():
    tiles = get_tiles()
    corner_indexes = [tile.index for tile in tiles if tile.get_match_count() == 2]
    print(corner_indexes)
    print(math.prod(corner_indexes))


def matches(this_tile, other_tile):
    if other_tile is None:
        return this_tile is None
    elif this_tile is not None:
        return other_tile.index == this_tile.index
    return False


def rotate_90(image):
    return [''.join(row) for row in zip(*reversed(image))]


def get_image_below_tile_and_right_tile(this_tile, above_tile):
    def check_tile(image, top_match, right_match, bottom_match, left_match):
        # Correctly oriented
        if matches(top_match, above_tile) \
                and left_match is None:
            return [image, bottom_match, right_match]

        # Flip horizontal
        elif matches(top_match, above_tile) \
                and right_match is None:
            return [[row[::-1] for row in image], bottom_match, left_match]

        # Flip vertical
        elif matches(bottom_match, above_tile) \
                and left_match is None:
            return [image[::-1], top_match, right_match]

        return None

    # Correctly oriented
    result = check_tile(this_tile.image, this_tile.top_match, this_tile.right_match, this_tile.bottom_match,
                        this_tile.left_match)

    if result is None:
        # Rotate 90
        result = check_tile(rotate_90(this_tile.image), this_tile.left_match, this_tile.top_match,
                            this_tile.right_match,
                            this_tile.bottom_match)

    if result is None:
        # Rotate 180
        result = check_tile(rotate_90(rotate_90(this_tile.image)), this_tile.bottom_match,
                            this_tile.left_match, this_tile.top_match,
                            this_tile.right_match)

    if result is None:
        # Rotate 270
        result = check_tile(rotate_90(rotate_90(rotate_90(this_tile.image))), this_tile.right_match,
                            this_tile.bottom_match, this_tile.left_match,
                            this_tile.top_match)

    return result


def generate_full_image(corners):
    def get_row(right_tile):
        def check_image(image, top_match, right_match, bottom_match, left_match, left_tile, above_tile):
            # Correctly oriented
            if matches(left_match, left_tile) \
                    and matches(top_match, above_tile):
                image_row.append(image)
                return right_match

            # Flip horizontal
            elif matches(right_match, left_tile) \
                    and matches(top_match, above_tile):
                image_row.append([row[::-1] for row in image])
                return left_match

            # Flip vertical
            elif matches(left_match, left_tile) \
                    and matches(bottom_match, above_tile):
                image_row.append(image[::-1])
                return right_match

            return None

        def add_tile(this_tile, left_tile, above_tile):
            current_image_len = len(image_row)

            # Correctly oriented
            next_tile = check_image(this_tile.image, this_tile.top_match, this_tile.right_match, this_tile.bottom_match,
                                    this_tile.left_match, left_tile, above_tile)

            if len(image_row) == current_image_len:
                # Rotate 90
                next_tile = check_image(rotate_90(this_tile.image), this_tile.left_match, this_tile.top_match,
                                        this_tile.right_match,
                                        this_tile.bottom_match, left_tile, above_tile)

            if len(image_row) == current_image_len:
                # Rotate 180
                next_tile = check_image(rotate_90(rotate_90(this_tile.image)), this_tile.bottom_match,
                                        this_tile.left_match, this_tile.top_match,
                                        this_tile.right_match, left_tile, above_tile)

            if len(image_row) == current_image_len:
                # Rotate 270
                next_tile = check_image(rotate_90(rotate_90(rotate_90(this_tile.image))), this_tile.right_match,
                                        this_tile.bottom_match, this_tile.left_match,
                                        this_tile.top_match, left_tile, above_tile)

            return next_tile

        image_row = [start_image]
        last_tile = start_tile
        index = 1
        while right_tile is not None:
            new_above_row.append(last_tile)
            next_tile = add_tile(right_tile, last_tile, above_row[index] if len(above_row) > index else None)
            last_tile = right_tile
            right_tile = next_tile
            index += 1
        new_above_row.append(last_tile)
        return image_row

    start_corner = [corner for corner in corners if corner.right_match is not None and corner.bottom_match is not None][
        0]

    start_tile = start_corner
    start_image = start_tile.image
    right_tile = start_tile.right_match
    below_tile = start_corner.bottom_match

    complete_image = []

    above_row = []
    new_above_row = []

    while start_tile is not None:
        complete_image.append(get_row(right_tile))
        above_row = new_above_row
        if below_tile is not None:
            next_thing = get_image_below_tile_and_right_tile(below_tile, start_tile)
            if next_thing is not None:
                start_tile = below_tile
                [start_image, below_tile, right_tile] = next_thing
                new_above_row = []
            else:
                start_tile = None
        else:
            start_tile = None

    for section in complete_image:
        for i in range(1, len(section[0]) - 1):
            line = ''
            for row in section:
                line += row[i][1:len(row) - 1]
            print(line)


def part2():
    tiles = get_tiles()

    corners = [tile for tile in tiles if tile.get_match_count() == 2]

    generate_full_image(corners)


# part1()
part2()
