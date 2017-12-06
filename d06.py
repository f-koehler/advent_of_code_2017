from copy import copy

if __name__ == "__main__":
    with open("input_06.txt") as fhandle:
        banks = [int(bank) for bank in fhandle.read().strip().split()]

    number_of_banks = len(banks)
    known_configurations = [copy(banks)]
    number_of_cycles = 0
    while True:
        blocks = max(banks)
        i_max = banks.index(blocks)
        i = (i_max + 1) % number_of_banks
        banks[i_max] = 0
        while blocks > 0:
            banks[i] += 1
            blocks -= 1
            i = (i + 1) % number_of_banks
        number_of_cycles += 1
        if banks in known_configurations:
            period = number_of_cycles - known_configurations.index(banks)
            break
        known_configurations.append(copy(banks))

    print(number_of_cycles)
    print(period)
