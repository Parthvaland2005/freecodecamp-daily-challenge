def get_daytime_hours(latitude):
    daytime = round((12 + (latitude / 90) * 12) / 2) * 2

    sunrise = (24 - daytime) // 2
    sunset = sunrise + daytime

    result = ""

    for hour in range(24):
        if sunrise <= hour < sunset:
            result += "☀️"
        else:
            result += "🌑"

    return result

print(get_daytime_hours(0))
print(get_daytime_hours(90))
print(get_daytime_hours(-90))
print(get_daytime_hours(-33))
print(get_daytime_hours(66.5))
print(get_daytime_hours(40))
print(get_daytime_hours(-50))