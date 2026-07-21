def blend_words(word1, word2):
    first = len(word1) // 2
    second = len(word2) // 2

    return word1[:first] + word2[second:]

print(blend_words("turtle", "toucan"))      # turcan
print(blend_words("chipmunk", "flamingo"))  # chipingo
print(blend_words("falcon", "pelican"))     # falican
print(blend_words("hyena", "iguana"))       # hyana
print(blend_words("scorpion", "gorilla"))   # scorilla
print(blend_words("platypus", "wolverine")) # platerine