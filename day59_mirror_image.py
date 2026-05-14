def is_mirror_image(s1, s2):

    mirror = {
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '<': '>',
        '>': '<',
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
        '(': ')',
        ')': '('
    }

    symmetric = set(
        "WTYUIOHAXVMwoxv08=+:|-_*^!. "
    )

    mirrored = ""

    for ch in reversed(s1):

        if ch in mirror:
            mirrored += mirror[ch]

        elif ch in symmetric:
            mirrored += ch

        else:
            return False

    return mirrored == s2

print(is_mirror_image("[HOW]", "[WOH]"))   # True
print(is_mirror_image("MOM", "MOM"))       # True
print(is_mirror_image("vow", "wov"))       # True
print(is_mirror_image("TIM", "TIM"))       # False
print(is_mirror_image("{WOW}", "}WOW{"))   # False
print(is_mirror_image("XXVII", "IIV%X"))   # False
print(is_mirror_image("><(((*>", "<*)))><"))  # True

print(is_mirror_image(
    "WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()",
    "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"
))  # True