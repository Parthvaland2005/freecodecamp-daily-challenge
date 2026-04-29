def parse_url_query(url):
    
    result = {}
    
    if "?" not in url:
        return result
    
    query = url.split("?")[1]
    
    pairs = query.split("&")
    
    for pair in pairs:
        key, value = pair.split("=")
        result[key] = value
    
    return result

print(parse_url_query("https://example.com/search?name=Alice&age=30"))
print(parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python"))
print(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"))
print(parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now"))