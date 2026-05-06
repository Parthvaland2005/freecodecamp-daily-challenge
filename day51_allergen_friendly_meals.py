def get_allergen_friendly_meals(meals, avoid):
    
    result = []
    
    for meal, allergens in meals:
        safe = True
        
        for a in allergens:
            if a in avoid:
                safe = False
                break
        
        if safe:
            result.append(meal)
    
    return result

print(get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]))
print(get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]))
print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"]))
print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"]))