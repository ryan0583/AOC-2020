from Utils.intcode_computer import IntcodeComputer


class Packet:
    def __init__(self, address):
        self.address = address
        self.x = None
        self.x_processed = False
        self.y = None


def setup():
    computers = []

    for i in range(0, 50):
        computer = IntcodeComputer([i], "input.txt", True)
        computers.append(computer)
        computer.next_instruction = IntcodeComputer.Instruction(str(computer.ints[computer.index]))
        computer.opcode = computer.next_instruction.opcode

    return computers


def all_idle(computers):
    idle = False
    for computer in computers:
        idle = computer.is_idle()

    return idle


def main_loop(computers, computer_instruction_map, written_ys, nat_packet, idle_count):
    done = False

    for i, computer in enumerate(computers):
        output = computer.process_single_instruction()

        if output is not None:
            existing_packet = computer_instruction_map.get(i)
            if existing_packet is not None:
                if existing_packet.x is None:
                    existing_packet.x = output
                else:
                    existing_packet.y = output
                    if existing_packet.address == 255:
                        nat_packet = existing_packet
                    else:
                        print(str(existing_packet.address) + ", " + str(existing_packet.x) + ", " + str(existing_packet.y))
                        computers[existing_packet.address].append_input(existing_packet.x)
                        computers[existing_packet.address].append_input(existing_packet.y)
                    del computer_instruction_map[i]
            else:
                packet = Packet(output)
                computer_instruction_map[i] = packet
            computer.opcode = computer.next_instruction.opcode
            idle_count = 0
        elif nat_packet is not None and all_idle(computers):
            if idle_count == 10000:
                print("all idle")
                computers[0].append_input(nat_packet.x)
                computers[0].append_input(nat_packet.y)
                print(nat_packet.y)
                if nat_packet.y == written_ys[len(written_ys) - 1]:
                    print("*************************")
                    print(nat_packet.y)
                    print("*************************")
                    done = True
                written_ys.append(nat_packet.y)
                idle_count = 0
            else:
                # print(idle_count)
                idle_count += 1

    return nat_packet, idle_count, done


def part1():
    computers = setup()

    computer_instruction_map = {}
    answered = False

    while not answered:
        nat_packet, idle_count, done = main_loop(computers, computer_instruction_map, [-1], None, 0)
        if nat_packet is not None:
            print(nat_packet.y)
            break


def part2():
    computers = setup()

    nat_packet = None
    computer_instruction_map = {}
    written_ys = [-1]
    idle_count = 0
    done = False

    while not done:
        nat_packet, idle_count, done = main_loop(computers, computer_instruction_map, written_ys, nat_packet, idle_count)


part1()
# part2()
