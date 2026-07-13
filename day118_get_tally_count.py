def get_tally_count(tally):
    count = 0

    for char in tally:
        if char == "|":
            count += 1
        elif char == "/":
            count += 1

    return count
print(get_tally_count("||||"))
print(get_tally_count("||||/"))
print(get_tally_count("||||/ |||"))
print(get_tally_count("||||/ ||||/ ||||/ ||"))
print(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"))