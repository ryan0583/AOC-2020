class ImageByteProcessor:
    class Layer:
        def __init__(self, pixels, width, height):
            self.pixels = pixels
            self.width = width
            self.height = height

        def add_pixel(self, pixel):
            self.pixels.append(pixel)

        def get_black_transparent_count(self):
            one_count = 0
            two_count = 0

            for i, pixel in enumerate(self.pixels):
                if pixel == BLACK:
                    one_count += 1
                elif pixel == TRANSPARENT:
                    two_count += 1

            print(one_count * two_count)
            return one_count * two_count

        def __str__(self):
            start_row = 0
            output = ""
            while start_row < self.width * self.height - 1:
                for pixel in self.pixels[start_row:start_row + self.width]:
                    output += "##" if pixel == BLACK else "  "
                output += "\n"
                start_row += self.width
            return output

    def __init__(self, all_pixels, width, height):
        self.layers = []
        self.all_pixels = all_pixels
        self.width = width
        self.height = height

    def process_layers(self):
        def process_layer():
            layer_pixels = self.all_pixels[start_index:end_layer_index]
            return self.Layer(layer_pixels, self.width, self.height)

        start_index = 0
        while start_index < len(self.all_pixels):
            end_layer_index = start_index + self.width * self.height
            layer = process_layer()
            self.layers.append(layer)
            start_index += len(layer.pixels)

    def get_min_white_layer(self):
        max_0_layer = None
        max_0_count = None

        for layer in self.layers:
            current_0_count = layer.pixels.count(WHITE)
            if max_0_count is None or current_0_count < max_0_count:
                max_0_layer = layer
                max_0_count = current_0_count

        return max_0_layer

    def get_black_transparent_count_of_min_white_layer(self):
        self.process_layers()
        return self.get_min_white_layer().get_black_transparent_count()

    def get_final_layer(self):
        final_layer = self.Layer([], self.width, self.height)

        for i in range(0, self.width * self.height):
            final_pixel = None
            for layer in self.layers:
                final_pixel = layer.pixels[i]
                if final_pixel != TRANSPARENT:
                    break
            final_layer.add_pixel(final_pixel)

        return final_layer

    def print_image(self):
        self.process_layers()
        final_layer = self.get_final_layer()
        print(final_layer)
        return str(final_layer)


WHITE = "0"
BLACK = "1"
TRANSPARENT = "2"
