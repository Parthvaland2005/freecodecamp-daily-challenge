def get_unique_climbs(n):
    
    if n <= 2:
        return n
    
    a, b = 1, 2 
    
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

print(get_unique_climbs(4))   # 5
print(get_unique_climbs(5))   # 8
print(get_unique_climbs(10))  # 89
print(get_unique_climbs(18))  # 4181
print(get_unique_climbs(29))  # 832040
print(get_unique_climbs(50))  # 20365011074