def find_sum(arr, target):
    
    n = len(arr)
    
    def backtrack(start, path, total):
    
        if total == target and len(path) >= 2:
            return path
        
        for i in range(start, n):
            result = backtrack(i + 1, path + [arr[i]], total + arr[i])
            if result:
                return result
        
        return None
    
    res = backtrack(0, [], 0)
    return res if res else "Sum not found"

print(find_sum([1, 3, 5, 7], 6))
print(find_sum([1, 2, 3, 4, 5], 5))
print(find_sum([1, 2, 3, 4, 5], 6))
print(find_sum([-1, -2, 3, 4], 1))
print(find_sum([3, 1, 4, 1, 5, 9, 2, 6], 10))
print(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20))
print(find_sum([7, 9, 4, 2, 5], 10))