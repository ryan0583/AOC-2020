from Utils.image_byte_processor import ImageByteProcessor


def part1():
    image_byte_processor = ImageByteProcessor(open("input.txt", "r").read(), 25, 6)
    return image_byte_processor.get_black_transparent_count_of_min_white_layer()


def part2():
    image_byte_processor = ImageByteProcessor(open("input.txt", "r").read(), 25, 6)
    return image_byte_processor.print_image()
