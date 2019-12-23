from Utils.intcode_computer import IntcodeComputer


class Packet:
    def __init__(self, address):
        self.address = address
        self.x = None
        self.x_processed = False
        self.y = None


def part1():
    computers = []

    for i in range(0, 50):
        computer = IntcodeComputer([i], "input.txt", True)
        computers.append(computer)
        computer.next_instruction = IntcodeComputer.Instruction(str(computer.ints[computer.index]))
        computer.opcode = computer.next_instruction.opcode

    computer_instruction_map = {}
    answered = False

    while not answered:
        for i, computer in enumerate(computers):
            output = computer.process_single_instruction()

            if output is not None:
                existing_packet = computer_instruction_map.get(i)
                if existing_packet is not None:
                    if existing_packet.x is None:
                        existing_packet.x = output
                    else:
                        print("output: " + str(existing_packet.address))
                        print("x: " + str(existing_packet.x))
                        print("y: " + str(output))
                        if existing_packet.address == 255:
                            print(output)
                            answered = True
                            break
                        existing_packet.y = output
                        computers[existing_packet.address].append_input(existing_packet.x)
                        computers[existing_packet.address].append_input(existing_packet.y)
                        del computer_instruction_map[i]
                else:
                    packet = Packet(output)
                    computer_instruction_map[i] = packet
                computer.opcode = computer.next_instruction.opcode


part1()
