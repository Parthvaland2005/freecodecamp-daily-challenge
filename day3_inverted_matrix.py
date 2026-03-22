def invert_matrix(matrix):
    values = set()

    for row in matrix:
        for val in row:
            values.add(val)

    v1, v2 = list(values)

    result = []

    for row in matrix:
        new_row = []
        for val in row:
            if val == v1:
                new_row.append(v2)
            else:
                new_row.append(v1)
        result.append(new_row)

    return result


if __name__ == "__main__":
    matrix = [["a", "b"], ["b", "a"]]
    print(invert_matrix(matrix))