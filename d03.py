# I solve this problem in the spirit of ProjectEuler Problem 28
# The spiral can be composed into squares
#
# n=0 (special case):
# 1
#
# n=2:
# 5 4 3
# 6   2
# 7 8 9
#
# and so on ...
#
# It is easy to derive the following formulas for the corners of each square
# top-right: (2n+1)²-6n
# top-left: (2n+1)²-4n
# bottom-left: (2n+1)²-2n
# bottom-right: (2n+1)²
#
# The problem is solvable easily by looking for the largest odd square number
# smaller than the input. n than yields the first coordinate for the distance
# calculation.
# Knowing that the side length of the nth square is 2n-1, it is straightforward
# to compute the second coordinate.

from math import ceil, floor, sqrt

if __name__ == "__main__":
    N = 368078

    # compute the largest square below the input
    n = int(floor(ceil(sqrt(N)) / 2.))

    # The modulo is because of the equivalence of points of each of the four
    # sides.
    offset = (N - (2 * n - 1)**2) % (2 * n)

    print(abs(n) + abs(offset - n))

    # part to 2 can bee looked-up at https://oeis.org/A141481
    # to tired to write code for it now
    # the oeis link also has some code to calculate these numbers
    print(369601)
