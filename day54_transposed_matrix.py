def transpose(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for c in range(cols):

        new_row = []

        for r in range(rows):
            new_row.append(matrix[r][c])

        result.append(new_row)

    return result

print(transpose([[1, 2, 3], [4, 5, 6]]))

print(transpose([[1, 2], [3, 4], [5, 6]]))

print(transpose([[1, 2], [3, 4], [5, 6], [7, 8]]))

print(transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]))

print(transpose([
    [True, False, True, False],
    [False, True, False, True],
    [True, True, False, False],
    [False, False, True, True],
    [True, False, False, True]
]))