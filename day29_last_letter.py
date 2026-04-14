def get_last_letter(s):
    
    max_char = ""
    
    for ch in s:
        if ch.isalpha():
            if max_char == "" or ch.lower() > max_char.lower():
                max_char = ch
    
    return max_char

print(get_last_letter("world"))   # w
print(get_last_letter("Hello World"))  # W
print(get_last_letter("The quick brown fox jumped over the lazy dog."))  # z
print(get_last_letter("HeLl0"))   # L
print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))  # T