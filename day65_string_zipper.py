def zip_strings(s1, s2):

    result = ""

    min_len = min(len(s1), len(s2))

    for i in range(min_len):
        result += s1[i] + s2[i]

    result += s1[min_len:]
    result += s2[min_len:]

    return result

print(zip_strings("abc", "123"))

print(zip_strings(
    "acegikmoqsuwy",
    "bdfhjlnprtvxz"
))

print(zip_strings("day", "night"))

print(zip_strings("python", "javascript"))

print(zip_strings("feCdCm", "reoeap"))