def fizz_buzz_count(start, end):

    fizz = 0
    buzz = 0

    for num in range(start, end + 1):

        if num % 3 == 0:
            fizz += 1

        if num % 5 == 0:
            buzz += 1

    return {
        "fizz": fizz,
        "buzz": buzz
    }

print(fizz_buzz_count(1, 11))

print(fizz_buzz_count(14, 41))

print(fizz_buzz_count(24, 100))

print(fizz_buzz_count(-635, -14))

print(fizz_buzz_count(-5432, 6789))