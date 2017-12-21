if __name__ == "__main__":
    with open("input_16.txt") as fhandle:
        moves = fhandle.read().strip().split(",")

    initial_permutation = [i for i in range(16)]
    initial_programs = [chr(97 + i) for i in range(16)]

    permutation = [i for i in range(16)]
    substitution = initial_programs[:]

    for move in moves:
        if move[0] == "s":
            size = int(move[1:])
            permutation = permutation[-size:] + permutation[:-size]
        elif move[0] == "x":
            i, j = map(int, move[1:].split("/"))
            permutation[i], permutation[j] = permutation[j], permutation[i]
        else:
            i, j = map(substitution.index, move[1:].split("/"))
            substitution[i], substitution[j] = substitution[j], substitution[i]

    def apply_permutation(a, b):
        return [a[i] for i in b]

    def compose_substitution(a, b):
        return [b[initial_programs.index(p)] for p in a]

    def apply_dance(repititions):
        # this uses exponentiation by squaring
        # see: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
        x_perm = permutation
        x_subst = substitution
        y_perm = initial_permutation
        y_subst = initial_programs

        while repititions > 1:
            if repititions % 2 == 0:
                x_perm = apply_permutation(x_perm, x_perm)
                x_subst = compose_substitution(x_subst, x_subst)
                repititions //= 2
            else:
                y_perm = apply_permutation(x_perm, y_perm)
                y_subst = compose_substitution(x_subst, y_subst)
                x_perm = apply_permutation(x_perm, x_perm)
                x_subst = compose_substitution(x_subst, x_subst)
                repititions = (repititions - 1) // 2

        total_perm = apply_permutation(x_perm, y_perm)
        total_subst = compose_substitution(x_subst, y_subst)
        return apply_permutation(
            compose_substitution(initial_programs, total_subst), total_perm)

    print("".join(apply_dance(1)))
    print("".join(apply_dance(1000000000)))
