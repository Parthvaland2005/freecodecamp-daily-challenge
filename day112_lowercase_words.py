def get_lowercase_words(text):
    words = text.split()
    result = []

    for word in words:
        if word.islower():
            result.append(word)

    return " ".join(result)

print(get_lowercase_words("hello GOOD world"))  
print(get_lowercase_words("these are all lowercase"))  
print(get_lowercase_words("less is NoT more"))  
print(get_lowercase_words("DonT eat pizza every OTHER day"))  
print(get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"))