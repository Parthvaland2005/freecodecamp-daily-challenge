def round_to_nearest_multiple(number, multiple):
    lower = (number // multiple) * multiple
    upper = lower + multiple

    if number - lower < upper - number:
        return lower
    else:
        return upper

print(round_to_nearest_multiple(5, 3))
print(round_to_nearest_multiple(17, 4))
print(round_to_nearest_multiple(43, 5))
print(round_to_nearest_multiple(38, 11))
print(round_to_nearest_multiple(93, 12))