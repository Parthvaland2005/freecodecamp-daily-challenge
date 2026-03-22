def detect_roast(beans):
    values = {"'": 1, "-": 2, ".": 3}
    
    total = sum(values[ch] for ch in beans)
    avg = total / len(beans)
    
    if avg < 1.75:
        return "Light"
    elif avg <= 2.5:
        return "Medium"
    else:
        return "Dark"

if __name__ == "__main__":
    print(detect_roast("''-''''''-'-''--''''"))