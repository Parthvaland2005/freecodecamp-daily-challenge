def truncate_text(s):
    
    def w(c):
        if c in "ilI":
            return 1
        elif c in "fjrt":
            return 2
        elif c in "ABCDEFGHKMNOPQRSTUVWXYZ":
            return 4
        elif c == " ":
            return 2
        elif c == ".":
            return 1
        else:
            return 3
    total = 0
    for c in s:
        total += w(c)
    if total <= 50:
        return s
    res = ""
    width = 0

    for c in s:
        if width + w(c) + 3 > 60: 
            break
        res += c
        width += w(c)

    return res + "..."

print(truncate_text("The quick brown fox"))
print(truncate_text("The silky smooth sloth"))
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(truncate_text("The fast striped zebra"))
print(truncate_text("The big black bear"))