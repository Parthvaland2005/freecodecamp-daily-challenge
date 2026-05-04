def convert_parsecs(n):
    
    if n % 2 == 0:   
        return n * 3
    else:            
        return n * 2

print(convert_parsecs(1))   # 2
print(convert_parsecs(2))   # 6
print(convert_parsecs(31))  # 62
print(convert_parsecs(88))  # 264
print(convert_parsecs(17))  # 34
print(convert_parsecs(14))  # 42