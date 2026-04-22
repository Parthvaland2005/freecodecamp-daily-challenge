def get_cleanup_score(items):
    
    values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }
    
    total = 0
    prev = None
    streak = 0
    
    for i, item in enumerate(items):
        
        if isinstance(item, list):
            base = item[1]
            streak = 0
            prev = None   
        
        else:
            base = values[item]
            
            if item == prev:
                streak += 1
            else:
                streak = 0
            
            base += streak
            prev = item
        
        if (i + 1) % 5 == 0:
            multiplier = (i + 1) // 5 + 1
            base *= multiplier
        
        total += base
    
    return total

print("Test 1:", get_cleanup_score(["bottle", "straw", "shoe", "battery"]), "Expected: 44")
print("Test 2:", get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]), "Expected: 58")
print("Test 3:", get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]), "Expected: 79")
print("Test 4:", get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]), "Expected: 358")
print("Test 5:", get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]), "Expected: 383")