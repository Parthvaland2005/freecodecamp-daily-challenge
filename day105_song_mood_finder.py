def get_mood(genre, bpm):
    if genre == "classical":
        if 60 <= bpm <= 109:
            return "focus"
        elif 110 <= bpm <= 180:
            return "happy"

    elif genre == "electronic":
        if 60 <= bpm <= 89:
            return "focus"
        elif 90 <= bpm <= 134:
            return "happy"
        elif 135 <= bpm <= 180:
            return "hype"

    elif genre == "pop":
        if 60 <= bpm <= 180:
            return "happy"

    elif genre == "rock":
        if 60 <= bpm <= 129:
            return "happy"
        elif 130 <= bpm <= 180:
            return "hype"

print(get_mood("rock", 111))
print(get_mood("electronic", 74))
print(get_mood("classical", 180))
print(get_mood("rock", 155))
print(get_mood("electronic", 90))
print(get_mood("classical", 67))
print(get_mood("pop", 100))
print(get_mood("electronic", 135))