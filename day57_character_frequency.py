def get_frequency(text):

    freq = {}

    for ch in text:

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

print(get_frequency("test"))

print(get_frequency("mississippi"))

print(get_frequency("hello world"))

print(get_frequency("She sells seashells by the seashore."))

print(get_frequency("The quick brown fox jumps over the lazy dog."))