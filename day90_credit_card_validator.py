def is_valid_card(card_number):
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        num = int(digit)

        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9

        total += num

    return total % 10 == 0

print(is_valid_card("4532015112830366"))  # True
print(is_valid_card("5425233430109903"))  # True
print(is_valid_card("371449635398431"))   # True
print(is_valid_card("6011111111111117"))  # True
print(is_valid_card("4532015112830367"))  # False
print(is_valid_card("1234567890123456"))  # False
print(is_valid_card("4532015112830368"))  # False