if __name__ == "__main__":
    with open("input_19.txt") as fhandle:
        network = fhandle.read().splitlines()

    w = len(network[0])
    h = len(network[0])
    x = network[0].index("|")
    y = 0

    # directions:
    # 0: up
    # 1: right
    # 2: down
    # 3: left
    d = 2

    result = ""
    steps = 1

    def get_neighbors(x, y):
        result = []
        result.append(network[y - 1][x] if y > 0 else None)
        result.append(network[y][x + 1] if x < w - 1 else None)
        result.append(network[y + 1][x] if y < h - 1 else None)
        result.append(network[y][x - 1] if x > 0 else None)
        for i, neighbor in enumerate(result):
            if neighbor == " ":
                result[i] = None
        return result

    def is_letter(x, y):
        o = ord(network[y][x])
        return (o > 64) and (o < 91)

    while True:
        if is_letter(x, y):
            result += network[y][x]

        if network[y][x] == "+":
            neighbors = get_neighbors(x, y)
            if d % 2 == 0:
                if neighbors[1] is not None:
                    d = 1
                else:
                    d = 3
            else:
                if neighbors[0] is not None:
                    d = 0
                else:
                    d = 2

        if d == 0:
            y -= 1
        elif d == 1:
            x += 1
        elif d == 2:
            y +=1
        else:
            x -= 1
        if is_letter(x, y) or (network[y][x] in ["+", "-", "|"]):
            steps += 1
            continue
        break

    print(result)
    print(steps)
