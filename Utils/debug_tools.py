def debug_print(debug, to_print):
    if debug:
        print(to_print)


def render_grid(grid):
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid])


def print_grid(debug, grid):
    debug_print(debug, render_grid(grid))


def create_grid(x_dimension, y_dimension, char):
    return [x[:] for x in [[char] * x_dimension] * y_dimension]


def replace_char_at_positions(grid, new_char, positions):
    new_grid = grid.copy()
    for position in positions:
        row = new_grid[position.get_y()]
        row[position.get_x()] = new_char
    return new_grid


def raise_(ex):
    raise ex
