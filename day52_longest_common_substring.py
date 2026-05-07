def get_longest_substring(s):

    longest = ""
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):

            sub = s[i:j]

            if s.find(sub, i + 1) != -1:

                if len(sub) > len(longest):
                    longest = sub

    return longest

print(get_longest_substring("abracadabra"))
print(get_longest_substring("hello world hello"))
print(get_longest_substring("mississippi"))
print(get_longest_substring("ha ha ha ha ha ha ha"))
print(get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"))