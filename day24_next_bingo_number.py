def get_next_bingo_number(s):
    
    letter = s[0]
    num = int(s[1:])

    bingo = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }
    letters = ["B", "I", "N", "G", "O"]
    
    start, end = bingo[letter]
    
    if num < end:
        return f"{letter}{num + 1}"
    
    idx = letters.index(letter)
    
    if idx < 4:
        next_letter = letters[idx + 1]
        return f"{next_letter}{bingo[next_letter][0]}"
    
    return "B1"
print(get_next_bingo_number("B10"))  # B11
print(get_next_bingo_number("N33"))  # N34
print(get_next_bingo_number("I30"))  # N31
print(get_next_bingo_number("G60"))  # O61
print(get_next_bingo_number("O75"))  # B1