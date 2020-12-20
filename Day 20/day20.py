from Utils.file_reader import read_chunks
import math

def is_corner(tile, tile_map):


def part1():
    chunks = read_chunks('TestInput.txt')
    # print(chunks)
    tile_map = {int(tile[tile.index('Tile ') + 5:tile.index(':\n')]): tile[tile.index(':\n') + 2:] for tile in chunks}
    print(math.prod([tile for tile in tile_map.keys()if is_corner(tile, tile_map)]))


part1()
