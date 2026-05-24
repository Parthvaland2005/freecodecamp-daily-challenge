def fix_numerals(s):

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for ch in s:
        total += values[ch]

    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, numeral in roman_map:

        while total >= value:
            result += numeral
            total -= value

    return result

print(fix_numerals("XIIIII"))

print(fix_numerals("IIIILX"))

print(fix_numerals("XXVVVIIIII"))

print(fix_numerals("MDCCLXXXXVIIII"))

print(fix_numerals("IIIIVVVVXXXXLLLLCCDD"))

print(fix_numerals("ILCDMIVDIIXLCVCXDL"))