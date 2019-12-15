with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


class Computer:
    def __init__(self, code):
        self.mem = (code[:] + [0] * 10000)[:10000]
        self.index = 0
        self.relative = 0

    def parameter_mode(self, op, param):
        if op[3 - param] == "0":
            return self.mem[self.index + param]
        elif op[3 - param] == "1":
            return self.index + param
        elif op[3 - param] == "2":
            return self.mem[self.index + param] + self.relative

    def run_program(self, inp):
        while self.index in range(len(self.mem)):
            opcode = str(self.mem[self.index]).zfill(5)
            if opcode.endswith("99"):
                break
            first = self.parameter_mode(opcode, 1)
            second = self.parameter_mode(opcode, 2)
            third = self.parameter_mode(opcode, 3)
            if opcode.endswith("1"):
                self.mem[third] = self.mem[second] + self.mem[first]
                self.index += 4
            elif opcode.endswith("2"):
                self.mem[third] = self.mem[second] * self.mem[first]
                self.index += 4
            elif opcode.endswith("3"):
                self.mem[first] = inp
                self.index += 2
            elif opcode.endswith("4"):
                self.index += 2
                return self.mem[first]
            elif opcode.endswith("5"):
                self.index = self.mem[second] if self.mem[first] != 0 else self.index + 3
            elif opcode.endswith("6"):
                self.index = self.mem[second] if self.mem[first] == 0 else self.index + 3
            elif opcode.endswith("7"):
                self.mem[third] = 1 if self.mem[first] < self.mem[second] else 0
                self.index += 4
            elif opcode.endswith("8"):
                self.mem[third] = 1 if self.mem[first] == self.mem[second] else 0
                self.index += 4
            elif opcode.endswith("9"):
                self.relative += self.mem[first]
                self.index += 2


def calculate_new_position(direction_to_move, current_position):
    if direction_to_move == 1:
        return current_position[0], current_position[1] + 1
    elif direction_to_move == 2:
        return current_position[0], current_position[1] - 1
    elif direction_to_move == 3:
        return current_position[0] - 1, current_position[1]
    elif direction_to_move == 4:
        return current_position[0] + 1, current_position[1]


def backtrack(from_direction):
    if from_direction == 1:
        return 2
    elif from_direction == 2:
        return 1
    elif from_direction == 3:
        return 4
    elif from_direction == 4:
        return 3


def unseen_neighbor(p):
    neighbors = [(p[0] - 1, p[1]),  (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]
    return any(n for n in neighbors if n not in distances.keys())


droid = Computer(ops)
position = (0, 0)
distances = {position: 0}
movement_history = []
proceed = True
while proceed:
    for direction in [1, 2, 3, 4]:
        new_position = calculate_new_position(direction, position)
        if new_position not in distances.keys():
            status = droid.run_program(direction)
            if status == 0:
                distances[new_position] = -1
            elif status == 1:
                movement_history.append(direction)
                if new_position not in distances.keys():
                    distances[new_position] = distances[position] + 1
                elif distances[new_position] > distances[position] + 1:
                    distances[new_position] = distances[position] + 1
                position = new_position
                break
            elif status == 2:
                # part one
                print("Found oxygen at distance %d" % (distances[position] + 1))
                distances[new_position] = 0
                for key, value in distances.items():
                    if value > 0:
                        distances.pop(key)
                movement_history = []
                position = new_position
                break
        elif direction == 4 and position != new_position:
            while not unseen_neighbor(position):
                if len(movement_history) == 0:
                    proceed = False
                    # part two
                    print("Maximum distance from oxygen point: %d" % max(distances.values()))
                    break
                backtrack_move = backtrack(movement_history.pop())
                droid.run_program(backtrack_move)
                position = calculate_new_position(backtrack_move, position)
