class Moon:
    def __init__(self, x, y, z, vel_x, vel_y, vel_z):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.vel_z = vel_z

    @staticmethod
    def copy(moon):
        return Moon(moon.x, moon.y, moon.z, moon.vel_x, moon.vel_y, moon.vel_z)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.vel_x) + ", " + str(
            self.vel_y) + ", " + str(self.vel_z)

    def __eq__(self, other):
        return self.x == other.x \
               and self.y == other.y \
               and self.z == other.z \
               and self.vel_x == other.vel_x \
               and self.vel_y == other.vel_y \
               and self.vel_z == other.vel_z


class MoonState:
    def __init__(self, moons):
        self.moon1 = Moon.copy(moons[0])
        self.moon2 = Moon.copy(moons[1])
        self.moon3 = Moon.copy(moons[2])

    def __str__(self):
        return str(self.moon1) + ":" + str(self.moon2) + ":" + str(self.moon3)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.moon1 == other.moon1 \
               and self.moon2 == other.moon2 \
               and self.moon3 == other.moon3


def create_moons():
    def create_moon(line):
        x = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        y = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        z = int(line[line.index("=") + 1:])
        return Moon(x, y, z, 0, 0, 0)

    lines = open("input.txt", "r").readlines()
    lines = list(map(lambda line: line.strip(), lines))
    lines = list(map(lambda line: line[1:len(line) - 1], lines))

    moons = list(map(create_moon, lines))
    return moons


def adjust_velocity(moons):
    def adjust_axis_velocity(coord, other_coord, vel):
        if coord < other_coord:
            return vel + 1
        elif coord > other_coord:
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
        # print((abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z)))
        energy += (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z))
    return energy


def loop_inner(moons, time_steps):
    adjust_velocity(moons)
    for moon in moons:
        moon.move()
        # print(moon)
    # print("\n\n")
    return time_steps + 1


def part1():
    moons = create_moons()
    time_steps = 0
    while time_steps < 1000:
        time_steps = loop_inner(moons, time_steps)

    print(get_energy(moons))


def part2():
    moons = create_moons()
    current_moon_state = MoonState(moons)
    moon_states = set()
    time_steps = 0

    while str(current_moon_state) not in moon_states:
        if time_steps % 100000 == 0:
            print(time_steps)
        moon_states.add(str(current_moon_state))
        time_steps = loop_inner(moons, time_steps)
        current_moon_state = MoonState(moons)
        # print(current_moon_state)

    print(time_steps)


# part1()
part2()
