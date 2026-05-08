def medication_reminder(medications, current_time):

    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    current = to_minutes(current_time)

    schedules = {
        "Deployxitrin": [8 * 60, 16 * 60],
        "Debuggamanizole": [7 * 60, 13 * 60, 21 * 60]
    }

    best_name = ""
    best_diff = float("inf")

    for name, last_taken in medications:

        if name == "Mergeflictamine":
            next_time = to_minutes(last_taken) + 240

            if next_time >= 1440:
                next_time -= 1440

            diff = (next_time - current) % 1440

        else:
            diff = float("inf")

            for t in schedules[name]:
                d = (t - current) % 1440

                if d == 0:
                    continue

                if d < diff:
                    diff = d

        if diff < best_diff:
            best_diff = diff
            best_name = name

    hours = best_diff // 60
    minutes = best_diff % 60

    return f"{best_name} in {hours}h {minutes}m"

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"))

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"))

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"))

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"))

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"))

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"))