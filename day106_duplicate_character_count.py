def duplicate_character_count(first, second):
    first_chars = set(first)
    count = 0

    for char in second:
        if char in first_chars:
            count += 1

    return count

print(duplicate_character_count("aloha", "hei"))
print(duplicate_character_count("jambo", "bonjour"))
print(duplicate_character_count("hello", "hola"))
print(duplicate_character_count("ola", "hej"))
print(duplicate_character_count("ciao", "konnichiwa"))
print(duplicate_character_count("merhaba", "xin chao"))
print(duplicate_character_count("hello world", "hello to everyone around the world"))