from itertools import islice


def generate_A(previous):
    while True:
        previous = (previous * 16807) % 2147483647
        yield previous


def generate_B(previous):
    while True:
        previous = (previous * 48271) % 2147483647
        yield previous


def check_match(args):
    return (args[0] & 0xffff) == (args[1] & 0xffff)


if __name__ == "__main__":
    with open("input_15.txt") as fhandle:
        initial_A = int(fhandle.readline().split()[-1])
        initial_B = int(fhandle.readline().split()[-1])

    part1 = islice(zip(generate_A(initial_A), generate_B(initial_B)), 40000000)
    part2 = islice(
        zip(
            filter(lambda n: not n % 4, generate_A(initial_A)),
            filter(lambda n: not n % 8, generate_B(initial_B))), 5000000)

    print(sum(map(check_match, part1)))
    print(sum(map(check_match, part2)))
