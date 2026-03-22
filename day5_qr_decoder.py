def rotate(matrix):
    return ["".join(row[i] for row in matrix[::-1]) for i in range(len(matrix))]


def is_valid(matrix):
    if matrix[0][0] == matrix[0][1] == matrix[1][0] == matrix[1][1] == "1":
        return True
    if matrix[0][4] == matrix[0][5] == matrix[1][4] == matrix[1][5] == "1":
        return True
    if matrix[4][0] == matrix[4][1] == matrix[5][0] == matrix[5][1] == "1":
        return True
    return False


def decode(matrix):
    for _ in range(4):
        if is_valid(matrix):
            return "".join(matrix[2:4])
        matrix = rotate(matrix)


if __name__ == "__main__":
    sample = [
        "110011",
        "110011",
        "000000",
        "000000",
        "110001",
        "110001"
    ]
    print(decode(sample))