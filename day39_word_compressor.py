def compress(s):
    
    words = s.split()
    seen = {}
    result = []
    
    for i, word in enumerate(words):
        if word not in seen:
            seen[word] = i + 1   
            result.append(word)
        else:
            result.append(str(seen[word]))
    
    return " ".join(result)

def test_case(input_data, expected):
    result = compress(input_data)
    if result == expected:
        print("PASS")
    else:
        print("FAIL")
        print("Result  :", result)
        print("Expected:", expected)
    print("-" * 50)

test_case(
    "practice makes perfect and perfect practice makes perfect",
    "practice makes perfect and 3 1 2 3"
)

test_case(
    "hello hello hello",
    "hello 1 1"
)

test_case(
    "the cat sat on the mat on which the cat sat",
    "the cat sat on 1 mat 4 which 1 2 3"
)

test_case(
    "the more you know the more you realize you don't know",
    "the more you know 1 2 3 realize 3 don't 4"
)

test_case(
    "lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero",
    "lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"
)