def sort_and_swap(arr):
    
    arr = sorted(arr)
    
    for i in range(len(arr)):
        if i % 3 == 0 and i != 0:

            arr[i], arr[i-1] = arr[i-1], arr[i]
    
    return arr

print(sort_and_swap([3, 1, 2, 4, 6, 5]))
print(sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8]))
print(sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]))
print(sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25]))
print(sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2]))