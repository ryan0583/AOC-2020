from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.x = PositionAndVelocity(x, 0)
        self.y = PositionAndVelocity(y, 0)
        self.z = PositionAndVelocity(z, 0)

    def move(self):
        self.x.position += self.x.velocity
        self.y.position += self.y.velocity
        self.z.position += self.z.velocity

    def __str__(self):
        return str(self.x.position) + ", " + str(self.y.position) + ", " + str(self.z.position)


class PositionAndVelocity:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __eq__(self, other):
        return self.position == other.position and self.velocity == self.position

    def __str__(self):
        return str(self.position) + "," + str(self.velocity)


class AxisState:
    def __init__(self):
        self.positions_and_velocities = []

    def add_position_and_velocity(self, position_and_velocity):
        self.positions_and_velocities.append(position_and_velocity)

    def __eq__(self, other):
        equal = True
        for i, position_and_velocity in enumerate(self.positions_and_velocities):
            if position_and_velocity != other.positions_and_velocities[i]:
                equal = False
                break
        return equal

    def __str__(self):
        output = ""
        for position_and_velocity in self.positions_and_velocities:
            output += str(position_and_velocity) + " : "
        return output


def create_moons():
    def create_moon(line):
        x = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        y = int(line[line.index("=") + 1:line.index(",")])
        line = line[line.index(",") + 1:]
        z = int(line[line.index("=") + 1:])
        return Moon(x, y, z)

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
            moon.x.velocity = adjust_axis_velocity(moon.x.position, otherMoon.x.position, moon.x.velocity)
            moon.y.velocity = adjust_axis_velocity(moon.y.position, otherMoon.y.position, moon.y.velocity)
            moon.z.velocity = adjust_axis_velocity(moon.z.position, otherMoon.z.position, moon.z.velocity)


def get_energy(moons):
    energy = 0
    for moon in moons:
        energy += (abs(moon.x.position) + abs(moon.y.position) + abs(moon.z.position)) * (
                abs(moon.x.velocity) + abs(moon.y.velocity) + abs(moon.z.velocity))
    return energy


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def adjust_velocity_and_move(moons):
    adjust_velocity(moons)
    for moon in moons:
        moon.move()


def part1():
    moons = create_moons()
    time_steps = 0
    while time_steps < 1000:
        adjust_velocity_and_move(moons)
        time_steps += 1

    return get_energy(moons)


def part2():
    def update_period(period, axis_state, seen):
        if period is None and str(axis_state) in seen:
            period = time_steps
        else:
            seen.add(str(axis_state))
        return period

    def create_axis_states():
        _x_axis_state = AxisState()
        _y_axis_state = AxisState()
        _z_axis_state = AxisState()
        for moon in moons:
            _x_axis_state.add_position_and_velocity(PositionAndVelocity(moon.x.position, moon.x.velocity))
            _y_axis_state.add_position_and_velocity(PositionAndVelocity(moon.y.position, moon.y.velocity))
            _z_axis_state.add_position_and_velocity(PositionAndVelocity(moon.z.position, moon.z.velocity))
        return _x_axis_state, _y_axis_state, _z_axis_state

    moons = create_moons()
    x_seen = set()
    y_seen = set()
    z_seen = set()
    x_period = None
    y_period = None
    z_period = None
    time_steps = 0

    while x_period is None or y_period is None or z_period is None:
        adjust_velocity_and_move(moons)

        x_axis_state, y_axis_state, z_axis_state = create_axis_states()

        x_period = update_period(x_period, x_axis_state, x_seen)
        y_period = update_period(y_period, y_axis_state, y_seen)
        z_period = update_period(z_period, z_axis_state, z_seen)
        time_steps += 1

    return lcm(x_period, lcm(y_period, z_period))


# print(part1())
# print(part2())
