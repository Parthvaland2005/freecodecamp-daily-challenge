def calculate_bmi(weight, height):
    bmi = (weight / (height ** 2)) * 703
    return round(bmi, 1)

print(calculate_bmi(180, 70))  # 25.8
print(calculate_bmi(140, 64))  # 24.0
print(calculate_bmi(160, 76))  # 19.5
print(calculate_bmi(200, 60))  # 39.1
print(calculate_bmi(150, 68))  # 22.8