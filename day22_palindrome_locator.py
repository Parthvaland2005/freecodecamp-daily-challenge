# Palindrome Characters
# Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

# A palindrome is a string that is the same forward and backward.
# If it's not a palindrome, return "none".

def palindrome_locator(s):
    
    if s != s[::-1]:
        return "none"
    
    n = len(s)
    
    if n % 2 == 1:
        return s[n // 2]     
    else:
        return s[n//2 - 1 : n//2 + 1]   

print(palindrome_locator("racecar"))     # e
print(palindrome_locator("level"))       # v
print(palindrome_locator("freecodecamp"))# none
print(palindrome_locator("noon"))        # oo
print(palindrome_locator("11100111"))    # 00