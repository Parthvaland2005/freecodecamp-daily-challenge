def horoscope_match(sign1, sign2):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    compatibility = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    i = signs.index(sign1)
    j = signs.index(sign2)

    distance = abs(i - j)
    distance = min(distance, 12 - distance)

    return compatibility[distance]

print(horoscope_match("Libra", "Sagittarius"))
print(horoscope_match("Gemini", "Scorpio"))
print(horoscope_match("Pisces", "Aries"))
print(horoscope_match("Capricorn", "Cancer"))
print(horoscope_match("Aquarius", "Aquarius"))
print(horoscope_match("Virgo", "Taurus"))
print(horoscope_match("Leo", "Scorpio"))