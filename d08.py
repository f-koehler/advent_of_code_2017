import re

regex_instruction = re.compile(
    r"^(\w+)\s+(inc|dec)\s+(-?\d+)\s+if\s+(\w+)\s+(>|<|<=|>=|==|!=)\s+(-?\d+)$"
)

if __name__ == "__main__":
    with open("input_08.txt") as fhandle:
        instructions = [
            (match.group(1), match.group(2), int(match.group(3)),
             match.group(4), match.group(5), int(match.group(6)))
            for match in [regex_instruction.match(line) for line in fhandle]
        ]

    registers = {}

    def check_condition(register, operator, value):
        registers[register] = registers.get(register, 0)
        if operator == ">":
            return registers[register] > value
        if operator == "<":
            return registers[register] < value
        if operator == ">=":
            return registers[register] >= value
        if operator == "<=":
            return registers[register] <= value
        if operator == "!=":
            return registers[register] != value
        if operator == "==":
            return registers[register] == value
        raise RuntimeError("Unknown operator \"{}\"".format(operator))

    maxvalue = 0
    for instruction in instructions:
        if not check_condition(instruction[3], instruction[4], instruction[5]):
            continue

        if instruction[1] == "inc":
            registers[instruction[0]] = registers.get(instruction[0],
                                                      0) + instruction[2]
            maxvalue = max(maxvalue, registers[instruction[0]])
            continue

        if instruction[1] == "dec":
            registers[instruction[0]] = registers.get(instruction[0],
                                                      0) - instruction[2]
            maxvalue = max(maxvalue, registers[instruction[0]])
            continue

        raise RuntimeError("Unknown operation \"{}\"".format(instruction[1]))

    print(registers[max(registers, key=registers.get)])
    print(maxvalue)
