def is_valid_isbn_13(s):

    for ch in s:
        if not (ch.isdigit() or ch == "-"):
            return False

    digits = s.replace("-", "")

    if len(digits) != 13:
        return False

    total = 0

    for i in range(13):

        num = int(digits[i])

        if i % 2 == 0:
            total += num
        else:
            total += num * 3

    return total % 10 == 0

print(is_valid_isbn_13("9780306406157"))
print(is_valid_isbn_13("97803064061570"))
print(is_valid_isbn_13("978-0-13-595705-9"))
print(is_valid_isbn_13("978-030-64061A-4"))
print(is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9"))