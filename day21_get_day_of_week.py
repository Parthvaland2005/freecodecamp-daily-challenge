def get_day_of_week(timestamp):
    
    seconds = timestamp / 1000
    
    days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    
    total_days = int(seconds // 86400)
    
    return days[total_days % 7]

print(get_day_of_week(1775492249000))   # Monday
print(get_day_of_week(1766246400000))   # Saturday
print(get_day_of_week(33791256000000))  # Tuesday
print(get_day_of_week(1773576000000))   # Sunday
print(get_day_of_week(0))               # Thursday