def rook_bishop_attack(rook, bishop):
        
    r_col, r_row = rook[0], int(rook[1])
    b_col, b_row = bishop[0], int(bishop[1])
  
    if r_col == b_col or r_row == b_row:
        return "rook"
    
    if abs(ord(r_col) - ord(b_col)) == abs(r_row - b_row):
        return "bishop"
    
    return "neither"

print(rook_bishop_attack("A1", "A5"))  # rook
print(rook_bishop_attack("C3", "F6"))  # bishop
print(rook_bishop_attack("D4", "D7"))  # rook
print(rook_bishop_attack("B7", "H1"))  # bishop
print(rook_bishop_attack("B3", "C5"))  # neither
print(rook_bishop_attack("G3", "E8"))  # neither