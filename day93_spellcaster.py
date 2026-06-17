def cast(spells):
    spell_data = {
        "f": (3, "Destruction"),
        "l": (3, "Destruction"),
        "i": (2, "Control"),
        "w": (2, "Control"),
        "h": (1, "Restoration"),
        "s": (1, "Restoration")
    }

    total_score = 0
    multiplier = 1
    prev_category = None

    for spell in spells:
        base_score, category = spell_data[spell]

        if prev_category is not None:
            if category != prev_category:
                multiplier += 1
            else:
                multiplier = 1

        total_score += base_score * multiplier
        prev_category = category

    return total_score

print(cast("fihwl"))              # 33
print(cast("lwswfi"))             # 45
print(cast("wislhfl"))            # 37
print(cast("sihwlih"))            # 50
print(cast("wishlfihwslwifihl"))  # 101