# ISBN-10 Validator
# Given a string, determine if it's a valid ISBN-10.

# An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

# The first 9 characters must be digits, and
# The final character may be a digit or the letter "X", which represents the number 10.
# To validate it:

# Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
# Add all the results together.
# If the total is divisible by 11, it's valid.

def is_valid_isbn10(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    total = 0
    
    for i in range(10):
        if i == 9 and isbn[i] == 'X':
            value = 10
        elif isbn[i].isdigit():
            value = int(isbn[i])
        else:
            return False
        
        total += value * (i + 1)
    
    return total % 11 == 0


if __name__ == "__main__":
    isbn = input("Enter ISBN-10: ")
    print(is_valid_isbn10(isbn))