def get_rotation(n):

    s = str(n)
    length = len(s)

    for i in range(length):
        num = int(s)

        if num % length == 0:
            return i

        s = s[1:] + s[0]

    return "none"

print(get_rotation(123))          # 0
print(get_rotation(13579))        # 3
print(get_rotation(24681))        # none
print(get_rotation(84138789345))  # 6