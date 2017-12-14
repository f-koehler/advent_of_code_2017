if __name__ == "__main__":
    with open("input_11.txt") as fhandle:
        steps = fhandle.read().strip().split(",")

    # relevant article: https://www.redblobgames.com/grids/hexagons

    position = (0, 0)
    vectors = {
        "n": (1, 0),
        "ne": (0, 1),
        "se": (-1, 1),
        "s": (-1, 0),
        "sw": (0, -1),
        "nw": (1, -1)
    }

    def distance(position):
        x, z = position
        y = -x - z
        return max(abs(x), abs(y), abs(z))

    max_distance = 0
    for step in steps:
        position = (position[0] + vectors[step][0],
                    position[1] + vectors[step][1])
        max_distance = max(max_distance, distance(position))

    distance = distance(position)
    print(distance)
    print(max_distance)
