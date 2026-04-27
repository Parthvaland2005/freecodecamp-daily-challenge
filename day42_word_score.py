def get_word_score(word):
    
    total = 0
    
    for ch in word:
        if ch.isalpha():   
            total += ord(ch.lower()) - ord('a') + 1
    
    return total

print(get_word_score("hi"))            # 17
print(get_word_score("hello"))         # 52
print(get_word_score("hippopotamus"))  # 169
print(get_word_score("freeCodeCamp"))  # 94