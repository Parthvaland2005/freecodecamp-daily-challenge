def prime_factorization(n):
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors

print(prime_factorization(20))      # [2, 2, 5]
print(prime_factorization(17))      # [17]
print(prime_factorization(15))      # [3, 5]
print(prime_factorization(35))      # [5, 7]
print(prime_factorization(999))     # [3, 3, 3, 37]
print(prime_factorization(360))     # [2, 2, 2, 3, 3, 5]
print(prime_factorization(510510))  # [2, 3, 5, 7, 11, 13, 17]