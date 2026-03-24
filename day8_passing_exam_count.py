def passing_count(scores, passing_score):
    count = 0
    for score in scores:
        if score >= passing_score:
            count += 1
    return count

scores = list(map(int, input("Enter scores: ").split(",")))

passing_score = int(input("Enter Passing Score: "))

result = passing_count(scores, passing_score)

print("Number of students passed:", result)