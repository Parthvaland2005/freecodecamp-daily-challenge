def alarm_check(alarm, wake):
    
    a_h, a_m = map(int, alarm.split(":"))
    w_h, w_m = map(int, wake.split(":"))
    
    alarm_min = a_h * 60 + a_m
    wake_min = w_h * 60 + w_m

    if wake_min < alarm_min:
        return "early"
    elif wake_min <= alarm_min + 10:
        return "on time"
    else:
        return "late"

print(alarm_check("07:00", "06:45"))
print(alarm_check("06:30", "06:30"))
print(alarm_check("08:10", "08:15"))
print(alarm_check("09:30", "09:45"))
print(alarm_check("08:15", "08:25"))
print(alarm_check("05:45", "05:56"))
print(alarm_check("04:30", "04:00"))