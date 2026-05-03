def get_greeting(time_str):
    
    hour = int(time_str.split(":")[0])
    
    if 5 <= hour <= 11:
        return "Good morning"
    elif 12 <= hour <= 17:
        return "Good afternoon"
    elif 18 <= hour <= 21:
        return "Good evening"
    else:
        return "Good night"

print(get_greeting("06:30"))  # Good morning
print(get_greeting("12:00"))  # Good afternoon
print(get_greeting("21:59"))  # Good evening
print(get_greeting("00:01"))  # Good night
print(get_greeting("11:30"))  # Good morning