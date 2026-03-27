# question:11 Truncate the Text 2
# Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

# Each character has a specific width:

# Letters	Width
# "ilI"	1
# "fjrt"	2
# "abcdeghkmnopqrstuvwxyzJL"	3
# "ABCDEFGHKMNOPQRSTUVWXYZ"	4
# The table above includes all upper and lower case letters. Additionally:

# Spaces (" ") have a width of 2
# Periods (".") have a width of 1
# If the given string is 50 units or less, return the string as-is, otherwise
# Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over.
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