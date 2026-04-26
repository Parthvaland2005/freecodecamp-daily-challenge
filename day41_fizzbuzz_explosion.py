def explode_fizzbuzz(target):
    
    z_count = 4      
    length = 8
    steps = 0
    
    while z_count < target:
        new_length = 0
        new_z = 0
        
        for i in range(1, length + 1):
            
            if i % 15 == 0:
                new_length += 8
                new_z += 4
            elif i % 3 == 0:
                new_length += 4
                new_z += 2
            elif i % 5 == 0:
                new_length += 4
                new_z += 2
            else:
                new_length += 1
            
                if (i % 8) in [3, 4, 7, 0]:   
                    new_z += 1
        
        length = new_length
        z_count = new_z
        steps += 1
    
    return steps

print(explode_fizzbuzz(9))        # 1
print(explode_fizzbuzz(15))       # 2
print(explode_fizzbuzz(51))       # 3
print(explode_fizzbuzz(52))       # 4
print(explode_fizzbuzz(359))      # 5
print(explode_fizzbuzz(789))      # 6
print(explode_fizzbuzz(54482))    # 11
print(explode_fizzbuzz(1000000))  # 14