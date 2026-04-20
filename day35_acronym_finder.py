def find_org(acronym):
    
    orgs = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]
    
    for org in orgs:
        words = org.split()
        first_letters = "".join(word[0] for word in words)
        
        if first_letters == acronym:
            return org
    
    return None

print(find_org("NASA"))
print(find_org("CIA"))
print(find_org("FBI"))
print(find_org("DOJ"))
print(find_org("WHO"))
print(find_org("EPA"))