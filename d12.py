import re

if __name__ == "__main__":
    vertices = set()
    edges = {}
    regex = re.compile(r"\d+")

    with open("input_12.txt") as fhandle:
        for line in fhandle:
            src_str, *dst_strs = regex.findall(line)
            src = int(src_str)
            vertices.add(src)
            for dst_str in dst_strs:
                dst = int(dst_str.strip())
                edges[src] = edges.get(src, set())
                edges[src].add(dst)

    def build_group(vertex):
        group = set([vertex])
        todo = [vertex]

        while todo:
            current = todo.pop()
            for dst in edges[current]:
                if dst not in group:
                    group.add(dst)
                    todo.append(dst)

        return group

    print(len(build_group(0)))

    groups = []
    while vertices:
        groups.append(build_group(next(iter(vertices))))
        vertices = vertices - groups[-1]

    print(len(groups))
