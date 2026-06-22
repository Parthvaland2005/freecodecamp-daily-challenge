def make_leet(text):
    leet = {
        "a": "4",
        "e": "3",
        "g": "9",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }

    return "".join(leet.get(char, char) for char in text)

print(make_leet("cool"))                     # c001
print(make_leet("leet"))                     # 1337
print(make_leet("hacker"))                   # h4ck3r
print(make_leet("satellite"))                # 547311173
print(make_leet("abcdefghijklmnopqrstuvwxyz"))
# 4bcd3f9h1jk1mn0pqr57uvwxyz