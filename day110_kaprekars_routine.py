def kaprekar(number):
    count = 0

    while number != 6174:
        digits = f"{number:04d}"

        largest = int("".join(sorted(digits, reverse=True)))
        smallest = int("".join(sorted(digits)))

        number = largest - smallest
        count += 1

    return count

print(kaprekar(1234))  # 3
print(kaprekar(2025))  # 6
print(kaprekar(7173))  # 4
print(kaprekar(3164))  # 7
print(kaprekar(8082))  # 2