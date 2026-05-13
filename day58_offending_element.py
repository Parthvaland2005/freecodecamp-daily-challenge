def find_offender(arr):

    n = len(arr)

    for i in range(n - 1):

        if arr[i] > arr[i + 1]:

            if i == 0 or arr[i - 1] <= arr[i + 1]:
                return i

            return i + 1

    return -1

print(find_offender([1, 6, 2, 3, 4, 5]))         
print(find_offender([1, 2, 3, 5, 4, 5]))          
print(find_offender([2, 1]))                    
print(find_offender([2, 4, 1, 6, 8]))             
print(find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]))  