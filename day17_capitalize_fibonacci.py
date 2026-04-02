def capitalize_fibonacci(s):

    fib = [0, 1]
    while fib[-1] < len(s):
        fib.append(fib[-1] + fib[-2])
    
    fib_set = set(fib)  

    result = ""

    for i in range(len(s)):
        ch = s[i]

        if ch.isalpha():
            if i in fib_set:
                result += ch.upper()
            else:
                result += ch.lower()
        else:
            result += ch  

    return result

print(capitalize_fibonacci("hello world"))
print(capitalize_fibonacci("HELLO WORLD"))
print(capitalize_fibonacci("hello, world!"))
print(capitalize_fibonacci("The quick brown fox jumped over the lazy dog."))