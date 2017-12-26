import re
import numpy
import bisect

if __name__ == "__main__":
    regex = re.compile(r"^p=<(.+)>,\s+v=<(.+)>,\s+a=<(.+)>$")
    with open("input_20.txt") as fhandle:
        lines = fhandle.read().splitlines()

    r0 = numpy.zeros(shape=(len(lines), 3), dtype=numpy.int64)
    v0 = numpy.zeros(shape=(len(lines), 3), dtype=numpy.int64)
    a = numpy.zeros(shape=(len(lines), 3), dtype=numpy.int64)
    for i, line in enumerate(lines):
        m = regex.match(line)
        r0[i] = [int(f) for f in m.group(1).split(",")]
        v0[i] = [int(f) for f in m.group(2).split(",")]
        a[i] = [int(f) for f in m.group(3).split(",")]

    def manhattan_distances(a):
        return numpy.abs(a[:, 0]) + numpy.abs(a[:, 1]) + numpy.abs(a[:, 2])

    # find the lowest accelerations (Manhattan metric)
    a_abs_manhattan = manhattan_distances(a)
    indices = numpy.argwhere(
        a_abs_manhattan == a_abs_manhattan.min()).flatten()

    # calculate distances for large times for these cases
    t_final = 1e6
    r_final = 0.5 * a[indices, :] * (
        t_final**2) + v0[indices, :] * t_final + r0[indices, :]
    closest = indices[manhattan_distances(r_final).argmin()]
    print(closest)

    # active_particles = list(range(len(lines)))
    r = r0
    v = v0
    for i in range(0, int(1e3)):
        v += a
        r += v
        _, unique_indices, unique_counts = numpy.unique(r, axis=0, return_index=True, return_counts=True)
        unique_indices = [index for i, index in enumerate(unique_indices) if unique_counts[i] == 1]
        a = a[unique_indices]
        v = v[unique_indices]
        r = r[unique_indices]

    print(r.shape)
