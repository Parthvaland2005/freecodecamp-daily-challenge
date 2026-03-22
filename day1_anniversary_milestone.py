def get_milestone(years):
    if years >= 70:
        return "Platinum"
    elif years >= 60:
        return "Diamond"
    elif years >= 50:
        return "Gold"
    elif years >= 40:
        return "Ruby"
    elif years >= 25:
        return "Silver"
    elif years >= 10:
        return "Tin"
    elif years >= 5:
        return "Wood"
    elif years >= 1:
        return "Paper"
    else:
        return "Newlyweds"
    
if __name__ == "__main__":
    print(get_milestone(26))