def is_in_crossword(ch):
    
    grid = [
        [0,1,0,0,0,0,0,1],
        [0,1,1,0,1,1,1,1],
        [0,1,0,0,0,1,0,0],
        [0,1,1,0,0,1,0,1],
        [0,1,0,1,0,0,1,0],
        [0,1,0,1,0,1,0,0],
        [0,1,1,0,1,0,0,0],
        [1,0,1,0,1,1,1,0]
    ]
    
    target = format(ord(ch), '08b')
    
    for row in grid:
        s = ''.join(map(str, row))
        if target in s or target in s[::-1]:
            return True
    
    for col in range(8):
        s = ''.join(str(grid[row][col]) for row in range(8))
        if target in s or target in s[::-1]:
            return True
    
    return False

print(is_in_crossword("I"))  # True
print(is_in_crossword("D"))  # True
print(is_in_crossword("0"))  # True
print(is_in_crossword("u"))  # True
print(is_in_crossword("Y"))  # False
print(is_in_crossword("p"))  # False
print(is_in_crossword("1"))  # False
print(is_in_crossword("Q"))  # False