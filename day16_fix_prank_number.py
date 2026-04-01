def fix_prank_number(arr):
    
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    d = max(set(diffs), key=diffs.count)

    if arr[1] - arr[0] == d:
        start = arr[0]
    elif arr[2] - arr[1] == d:
        start = arr[1] - d
    else:
        start = arr[0]

    result = [start]
    for i in range(1, len(arr)):
        result.append(result[-1] + d)

    return result

print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([0, 100, 200, 300, 150, 500]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))