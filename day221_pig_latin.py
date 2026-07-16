def pig_latin(text):
    vowels = "aeiou"

    def convert(word):
        if word[0].lower() in vowels:
            return word + "way"

        i = 0
        while i < len(word) and word[i].lower() not in vowels:
            i += 1

        result = word[i:] + word[:i] + "ay"

        if word[0].isupper():
            result = result.capitalize()

        return result

    return " ".join(convert(word) for word in text.split())

print(pig_latin("universe"))
print(pig_latin("hello"))
print(pig_latin("hello universe"))
print(pig_latin("Hello universe"))
print(pig_latin("Pig Latin is fun"))
print(pig_latin("The quick brown fox jumped over the lazy dog"))