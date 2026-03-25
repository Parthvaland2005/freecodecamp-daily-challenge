from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    finish = datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")
    current = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
    
    return (current - finish) >= timedelta(days=2)

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))  # True
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))  # False