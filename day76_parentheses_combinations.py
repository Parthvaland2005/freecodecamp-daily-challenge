from math import factorial

def get_combinations(n):
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))

print(get_combinations(2))   # 2
print(get_combinations(3))   # 5
print(get_combinations(5))   # 42
print(get_combinations(8))   # 1430
print(get_combinations(13))  # 742900