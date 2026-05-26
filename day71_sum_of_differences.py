def sum_of_differences(numbers):

    total = 0

    for i in range(len(numbers) - 1):

        total += numbers[i + 1] - numbers[i]

    return total

print(sum_of_differences([1, 3, 4]))

print(sum_of_differences([5, -3, 3, 9, 10]))

print(sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]))

print(sum_of_differences([
    50, 102, -46, 82, -49, 29,
    71, 902, -237, 111, -61, 75
]))