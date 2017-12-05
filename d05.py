if __name__ == "__main__":
    with open("input_05.txt") as fhandle:
        instructions = [int(line.strip()) for line in fhandle]

    position = 0
    steps = 0
    while position < len(instructions):
        offset = instructions[position]
        instructions[position] += 1
        position += offset
        steps += 1

    print(steps)

    with open("input_05.txt") as fhandle:
        instructions = [int(line.strip()) for line in fhandle]

    position = 0
    steps = 0
    while position < len(instructions):
        offset = instructions[position]
        if offset >= 3:
            instructions[position] -= 1
        else:
            instructions[position] += 1
        position += offset
        steps += 1

    print(steps)
