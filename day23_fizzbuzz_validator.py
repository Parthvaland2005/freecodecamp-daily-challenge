def is_fizz_buzz(arr):
    
    for i, val in enumerate(arr):
        if isinstance(val, int):
            start = val - i
            break
    
    for i, val in enumerate(arr):
        num = start + i
        
        if num % 15 == 0:
            expected = "FizzBuzz"
        elif num % 3 == 0:
            expected = "Fizz"
        elif num % 5 == 0:
            expected = "Buzz"
        else:
            expected = num
        
        if val != expected:
            return False
    
    return True

print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))                  # True
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))              # True
print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))                      # False
print(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]))  # True
print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]))                 # False
print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]))# False
print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"])) # True