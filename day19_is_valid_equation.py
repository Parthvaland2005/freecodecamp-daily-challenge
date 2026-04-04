def is_valid_equation(eq):
    
    left, right = eq.split("=")
    
    left = left.strip()
    right = int(right.strip())
    
    try:
        result = eval(left)
    except:
        return False

    return result == right

print(is_valid_equation("2 + 2 = 4"))          # True
print(is_valid_equation("2 + 3 - 1 = 4"))      # True
print(is_valid_equation("8 / 2 = 4"))          # True
print(is_valid_equation("10 * 5 = 50"))        # True
print(is_valid_equation("2 - 2 = 0"))          # True
print(is_valid_equation("2 + 9 / 3 = 5"))      # True
print(is_valid_equation("20 - 2 * 3 = 14"))    # True
print(is_valid_equation("2 + 5 = 6"))          # False
print(is_valid_equation("10 - 2 * 3 = 24"))    # False
print(is_valid_equation("3 + 9 / 3 = 4"))      # False