class ImageByteProcessor:
    class __Layer:
        def __init__(self, pixels, width, height):
            self.pixels = pixels
            self.width = width
            self.height = height

        def add_pixel(self, pixel):
            self.pixels.append(pixel)

        def get_black_transparent_count(self):
            return self.pixels.count(BLACK) * self.pixels.count(TRANSPARENT)

        def __str__(self):
            def to_pixel_char(pixel):
                return "##" if pixel == BLACK else "  "

            def get_row():
                return "".join(map(to_pixel_char, self.pixels[start_row:start_row + self.width]))

            start_row = 0
            output = ""
            while start_row < self.width * self.height - 1:
                output += get_row()
                output += "\n"
                start_row += self.width
            return output

    def __init__(self, all_pixels, width, height):
        self.__layers = []
        self.__all_pixels = all_pixels
        self.__width = width
        self.__height = height

    def __process_layers(self):
        def process_layer():
            layer_pixels = self.__all_pixels[start_index:end_layer_index]
            return self.__Layer(layer_pixels, self.__width, self.__height)

        start_index = 0
        while start_index < len(self.__all_pixels):
            end_layer_index = start_index + self.__width * self.__height
            layer = process_layer()
            self.__layers.append(layer)
            start_index += len(layer.pixels)

    def __get_min_white_layer(self):
        def get_white_count(layer):
            return layer.pixels.count(WHITE)

        layer_white_counts = map(get_white_count, self.__layers)
        min_count, min_index = min((white_count, index) for index, white_count in enumerate(layer_white_counts))
        return self.__layers[min_index]

    def get_black_transparent_count_of_min_white_layer(self):
        self.__process_layers()
        return self.__get_min_white_layer().get_black_transparent_count()

    def __get_final_layer(self):
        final_layer = self.__Layer([], self.__width, self.__height)

        for i in range(0, self.__width * self.__height):
            final_pixel = None
            for layer in self.__layers:
                final_pixel = layer.pixels[i]
                if final_pixel != TRANSPARENT:
                    break
            final_layer.add_pixel(final_pixel)

        return final_layer

    def print_image(self):
        self.__process_layers()
        final_layer = self.__get_final_layer()
        print(final_layer)
        return str(final_layer)


WHITE = "0"
BLACK = "1"
TRANSPARENT = "2"
