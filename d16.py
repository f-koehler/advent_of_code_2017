if __name__ == "__main__":
    with open("input_16.txt") as fhandle:
        moves = fhandle.read().strip().split(",")

    length = 16
    initial_programs = [chr(97 + i) for i in range(16)]
    programs = initial_programs

    def spin(size):
        return programs[-size:] + programs[:-size]

    def exchange(i, j):
        programs[j], programs[i] = programs[i], programs[j]
        return programs

    def partner(a, b):
        return exchange(programs.index(a), programs.index(b))

    for move in moves:
        if move[0] == "s":
            programs = spin(int(move[1:]))
        elif move[0] == "x":
            programs = exchange(*map(int, move[1:].split("/")))
        else:
            programs = partner(*move[1:].split("/"))

    print("".join(programs))
