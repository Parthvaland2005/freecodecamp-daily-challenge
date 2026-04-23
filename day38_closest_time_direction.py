def get_direction(t1, t2):
    
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))
    
    start = h1 * 60 + m1
    end = h2 * 60 + m2
    
    forward = (end - start) % (24 * 60)
    
    backward = (start - end) % (24 * 60)
    
    if forward < backward:
        return "forward"
    elif backward < forward:
        return "backward"
    else:
        return "equal"

print(get_direction("10:00", "12:00"))  # forward
print(get_direction("11:00", "05:00"))  # backward
print(get_direction("00:00", "12:00"))  # equal
print(get_direction("15:45", "01:10"))  # forward
print(get_direction("03:30", "19:50"))  # backward
print(get_direction("06:30", "18:30"))  # equal