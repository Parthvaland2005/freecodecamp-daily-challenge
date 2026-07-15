def chunk_array(arr, size):
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])

    return result

print(chunk_array([1, 2, 3, 4, 5, 6], 3))
print(chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2))
print(chunk_array([1, 2, 3, 4, 5], 3))
print(chunk_array(["a", "b", "c", "d", "e"], 1))
print(chunk_array([1, 2, 3], 5))