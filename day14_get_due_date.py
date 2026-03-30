from datetime import datetime
import calendar

def get_due_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    year = date.year
    month = date.month + 9
    day = date.day

    if month > 12:
        year += month // 12
        month = month % 12
        if month == 0:
            month = 12
            year -= 1

    last_day = calendar.monthrange(year, month)[1]

    day = min(day, last_day)

    return f"{year:04d}-{month:02d}-{day:02d}"

print(get_due_date("2025-03-30"))  # 2025-12-30
print(get_due_date("2025-04-27"))  # 2026-01-27
print(get_due_date("2024-05-31"))  # 2025-02-28 (Feb doesn't have 31)