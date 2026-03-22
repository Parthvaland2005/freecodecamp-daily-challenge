def get_shadow(time):
    hour, minute = map(int, time.split(":"))

    t = hour + minute / 60

    if t <= 6 or t >= 18 or t == 12:
        return "No shadow"

    hours_away = abs(t - 12)

    length = hours_away ** 3

    if length.is_integer():
        length = int(length)

    if t < 12:
        direction = "west"
    else:
        direction = "east"

    return f"{length}ft {direction}"

if __name__ == "__main__":
    print(get_shadow("10:00"))