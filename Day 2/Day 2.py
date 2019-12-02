def partOne(ints) :
    ints[1] = 12
    ints[2] = 2
    index = 0
    opcode = ints[index]
    while opcode != 99 :
        print(opcode)
        val = 0
        index1 = ints[index + 1]
        index2 = ints[index + 2]
        index3 = ints[index + 3]
        val1 = ints[index1]
        val2 = ints[index2]
        if opcode == 1 :
            val = val1 + val2
        else :
            val = val1 * val2
        ints[index3] = val
        index = index + 4
        opcode = ints[index]
    print(ints[0])

file = open("input.txt", "r")
ints = list(map(int, file.read().split(",")))
print(ints)
partOne(ints)

                
