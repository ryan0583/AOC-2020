from Utils.file_reader import read_lines


def convert_to_binary_and_pad(decimal):
    return bin(decimal).replace("0b", "").zfill(36)


def part1_process(decimal_number, result, mem_address, mask):
    def put_number_at_position(binary):
        result_number = ""
        for index, c in enumerate(mask):
            result_number += binary[index] if c == X else c
        result[mem_address] = int(result_number, 2)

    put_number_at_position(convert_to_binary_and_pad(decimal_number))


def part2_process(decimal_number, result, mem_address, mask):
    def get_memory_addresses():
        def get_first_x_replacement_combinations(addresses):
            new_addresses = []
            for address in addresses:
                try:
                    x_index = address.index(X)
                    address_with_1 = address[:x_index] + "1" + address[x_index + 1:]
                    address_with_0 = address[:x_index] + "0" + address[x_index + 1:]
                    new_addresses.append(address_with_1)
                    new_addresses.append(address_with_0)
                except ValueError:
                    return []
            return new_addresses

        memory_address_binary_with_wildcards = convert_to_binary_and_pad(int(mem_address))
        result_address = ""
        for index, c in enumerate(mask):
            result_address += c if c == X or c == '1' else memory_address_binary_with_wildcards[index]

        final_addresses = [result_address]
        next_addresses = final_addresses
        while len(next_addresses) > 0:
            final_addresses = next_addresses
            next_addresses = get_first_x_replacement_combinations(final_addresses)
        return final_addresses

    mem_addresses = get_memory_addresses()
    for addr in mem_addresses:
        result[int(addr, 2)] = decimal_number


def parse_input(process):
    def parse_line():
        new_mask = mask
        parts = line.split(" = ")
        line_type = parts[0]
        if line_type == MASK:
            new_mask = parts[1].replace("\n", "")
        else:
            mem_address = parts[0].split("[")[1].replace("]", "")
            process(int(parts[1].replace("\n", "")), result, mem_address, new_mask)
        return new_mask

    lines = read_lines('Input.txt')
    mask = ""
    result = {}
    for line in lines:
        mask = parse_line()

    return sum(result.values())


def part1():
    return parse_input(part1_process)


def part2():
    return parse_input(part2_process)


MASK = "mask"
X = "X"

print(part1())
print(part2())
