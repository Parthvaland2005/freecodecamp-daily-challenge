def group_anagrams(words):
    
    groups = {}
    
    for word in words:
        key = ''.join(sorted(word))   
        
        if key not in groups:
            groups[key] = []
        
        groups[key].append(word)
    
    return list(groups.values())

print(group_anagrams(["listen", "silent", "hello", "enlist", "world"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]))
print(group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]))