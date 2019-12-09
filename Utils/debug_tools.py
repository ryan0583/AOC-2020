def debug_print(debug, to_print):
    if debug:
        print(to_print)


def print_grid(debug, grid):
    debug_print(debug, '\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))


def create_grid(x_dimension, y_dimension):
    return [x[:] for x in [["."] * x_dimension] * y_dimension]


def raise_(ex):
    raise ex
