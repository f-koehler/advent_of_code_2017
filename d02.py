if __name__ == "__main__":
    with open("input_02.txt") as fhandle:
        sheet = [[int(col) for col in row.strip().split()] for row in fhandle]

    print(sum([max(row) - min(row) for row in sheet]))

    def process_row(row):
        for i in range(len(row)):
            for j in range(i):
                if row[i] % row[j] == 0:
                    return row[i] // row[j]
                elif row[j] % row[i] == 0:
                    return row[j] // row[i]

    print(sum([process_row(row) for row in sheet]))
