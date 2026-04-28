def get_number_words(n):
    
    ones = [
        "zero","one","two","three","four","five","six","seven","eight","nine",
        "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
        "seventeen","eighteen","nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    
    if n < 20:
        return ones[n]
        
    t = n // 10
    o = n % 10
    
    if o == 0:
        return tens[t]
    else:
        return tens[t] + "-" + ones[o]

print(get_number_words(0))    # zero
print(get_number_words(10))   # ten
print(get_number_words(19))   # nineteen
print(get_number_words(30))   # thirty
print(get_number_words(53))   # fifty-three
print(get_number_words(7))    # seven
print(get_number_words(12))   # twelve
print(get_number_words(60))   # sixty
print(get_number_words(67))   # sixty-seven
print(get_number_words(98))   # ninety-eight