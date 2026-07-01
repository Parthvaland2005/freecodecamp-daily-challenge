def get_lucky_number(name):
    vowels = "aeiou"

    first, last = name.split()

    def counts(word):
        v = sum(1 for ch in word.lower() if ch in vowels)
        c = sum(1 for ch in word.lower() if ch.isalpha() and ch not in vowels)
        return v, c, len(word)

    v1, c1, l1 = counts(first)
    v2, c2, l2 = counts(last)

    smaller_vowels = min(v1, v2)
    larger_vowels = max(v1, v2)

    smaller_consonants = min(c1, c2)
    larger_consonants = max(c1, c2)

    smaller_length = min(l1, l2)
    larger_length = max(l1, l2)

    small_value = smaller_vowels * smaller_consonants * smaller_length
    large_value = larger_vowels * larger_consonants * larger_length

    lucky = large_value - small_value

    return 13 if lucky == 0 else lucky

print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))