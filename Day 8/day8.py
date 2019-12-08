class Layer:
    def __init__(self):
        self.pixels = []

    def add_pixel(self, pixel):
        self.pixels.append(pixel)

    def get_pixels(self):
        return self.pixels


def process_layers():
    def process_layer():
        layer = Layer()
        for i in range(start_index, start_index + width * height):
            layer.add_pixel(all_pixels[i])
        return layer

    # all_pixels = open("testinput3.txt", "r").read()
    all_pixels = open("input.txt", "r").read()
    layers = []
    start_index = 0
    # width = 2
    # height = 2
    width = 25
    height = 6
    while start_index < len(all_pixels):
        layers.append(process_layer())
        start_index += width * height
    return layers


def get_0_count(layer):
    zero_count = 0
    for i in range(0, len(layer.pixels)):
        if layer.pixels[i] == "0":
            zero_count += 1
    return zero_count


def get_min_0_layer(layers):
    max_0_layer = None
    max_0_count = None

    for layer in layers:
        current_0_count = get_0_count(layer)
        if max_0_count is None or current_0_count < max_0_count:
            max_0_layer = layer
            max_0_count = current_0_count

    return max_0_layer


def get_output(layer):
    one_count = 0
    two_count = 0

    for i in range(0, len(layer.pixels)):
        if layer.pixels[i] == "1":
            one_count += 1
        elif layer.pixels[i] == "2":
            two_count += 1

    print(one_count * two_count)
    return one_count * two_count


def part1():
    return get_output(get_min_0_layer(process_layers()))


def part2():

    def get_final_layer(layers):
        _final_layer = Layer()

        for i in range(0, width * height):
            final_pixel = None
            for layer in layers:
                final_pixel = layer.get_pixels()[i]
                if final_pixel != transparent:
                    break
            _final_layer.add_pixel(final_pixel)

        return _final_layer

    transparent = "2"
    # width = 2
    # height = 2
    width = 25
    height = 6
    final_layer = get_final_layer(process_layers())
    pixel = 0
    start_row = 0
    row = ""
    while start_row < width * height - 1:
        for pixel in range(start_row, start_row + width):
            row += final_layer.get_pixels()[pixel] + ","
        print(row)
        row = ""
        start_row = pixel + 1


part2()
