class Policy:
    def __init__(self, policy_str):
        self._num1 = int(policy_str.split("-")[0])
        self._num2 = int(policy_str.split("-")[1].split(" ")[0])
        self._letter = policy_str.split("-")[1].split(" ")[1]

    def get_num1(self):
        return self._num1

    def get_num2(self):
        return self._num2

    def get_letter(self):
        return self._letter


class PolicyAndPassword:
    def __init__(self, line):
        line_parts = line.split(":")
        self._policy = Policy(line_parts[0])
        self._password = line_parts[1].lstrip()

    def get_policy(self):
        return self._policy

    def get_password(self):
        return self._password


def part1_isvalid(policy_and_password):
    policy = policy_and_password.get_policy()
    actual_letter_count = int(policy_and_password.get_password().count(policy.get_letter()))
    if policy.get_num1() <= actual_letter_count <= policy.get_num2():
        return True
    return False


def part2_isvalid(policy_and_password):
    password = policy_and_password.get_password()
    policy = policy_and_password.get_policy()
    pos_1_match = password[policy.get_num1() - 1] == policy.get_letter()
    pos_2_match = password[policy.get_num2() - 1] == policy.get_letter()
    both_match = pos_1_match and pos_2_match
    one_matches = pos_1_match or pos_2_match

    if one_matches and not both_match:
        return True
    return False


def process(is_valid):
    return len(
        list(
            filter(
                is_valid,
                map(
                    PolicyAndPassword,
                    open("Input.txt", "r").readlines()
                )
            )
        )
    )


def part1():
    return process(part1_isvalid)


def part2():
    return process(part2_isvalid)


print(part1())
print(part2())
