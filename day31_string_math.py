def do_math(s):
    
    import re
    
    nums = list(map(int, re.findall(r'\d+', s)))
    
    parts = re.split(r'\d+', s)
    
    result = nums[0]
    
    for i in range(1, len(nums)):
        separator = parts[i]
        
        if len(separator) % 2 == 0:
            result += nums[i]
        else:
            result -= nums[i]
    
    return result

print(do_math("3ab10c8"))  
print(do_math("6MINUS4"))  
print(do_math("9plus3"))  
print(do_math("5fkwo#10i#%.<>15P=@20!#B/25"))  