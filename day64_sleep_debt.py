def sleep_debt(hours, target):

    needed = target * (len(hours) + 1)

    slept = sum(hours)

    debt = needed - slept

    return max(0, debt)

print(sleep_debt([6, 6, 6, 6, 6, 6], 8))

print(sleep_debt([6, 7, 8, 4, 8, 6], 7))

print(sleep_debt([10, 10, 9, 10, 9, 11], 9))

print(sleep_debt([8, 7, 6, 7, 6, 8], 6))

print(sleep_debt([8, 9, 10, 9, 10, 7], 7))