def get_odd_words(s):
    
    words = s.split()
    result = []
    
    for word in words:
        if len(word) % 2 != 0:  
            result.append(word)
    
    return " ".join(result)

print(get_odd_words("This is a super good test"))
print(get_odd_words("one two three four"))
print(get_odd_words("banana split sundae with rainbow sprinkles on top"))
print(get_odd_words("The quick brown fox jumped over the lazy river"))