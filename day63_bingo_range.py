def get_bingo_range(letter):

    ranges = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    start, end = ranges[letter]

    return list(range(start, end + 1))

print(get_bingo_range("B"))

print(get_bingo_range("I"))

print(get_bingo_range("N"))

print(get_bingo_range("G"))

print(get_bingo_range("O"))