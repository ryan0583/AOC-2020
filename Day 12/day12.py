class Moon:
    def __init__(self, line):
        self.x = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        self.y = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        self.z = int(line[line.index("=") + 1:])
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)


def createMoons():
    lines = open("testinput.txt", "r").readlines()
    lines = list(map(lambda line: line.strip(), lines))
    lines = list(map(lambda line: line[1:len(line) - 1], lines))
    moons = list(map(lambda line: Moon(line), lines))
    return moons


def adjust_velocity(moons):
    def adjust_axis_velocity(coord, other_coord, vel):
        if coord < other_coord:
            return vel + 1
        elif moon.x > otherMoon.x:
            return vel - 1
        return vel

    for moon in moons:
        for otherMoon in moons:
            moon.vel_x = adjust_axis_velocity(moon.x, otherMoon.x, moon.vel_x)
            moon.vel_y = adjust_axis_velocity(moon.y, otherMoon.y, moon.vel_y)
            moon.vel_z = adjust_axis_velocity(moon.z, otherMoon.z, moon.vel_z)


def get_energy(moons):
    energy = 0
    for moon in moons:
        print((abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z)))
        energy += (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z))
    return energy


def part1():
    moons = createMoons()
    time_steps = 0
    while time_steps < 100:
        adjust_velocity(moons)
        for moon in moons:
            moon.move()
        time_steps += 1

    print(get_energy(moons))


part1()
