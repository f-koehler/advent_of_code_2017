from itertools import permutations

if __name__ == "__main__":
    with open("input_04.txt") as fhandle:
        passphrases = [line.strip().split(" ") for line in fhandle]

    valid_passphrases = [
        passphrase for passphrase in passphrases
        if len(passphrase) == len(set(passphrase))
    ]
    print(len(valid_passphrases))

    def contains_anagram(passphrase):
        for word in passphrase:
            for permutation in permutations(word):
                permutation = "".join(permutation)
                if permutation == word:
                    continue
                if permutation in passphrase:
                    return True
        return False

    valid_passphrases = [
        passphrase for passphrase in valid_passphrases
        if not contains_anagram(passphrase)
    ]
    print(len(valid_passphrases))
