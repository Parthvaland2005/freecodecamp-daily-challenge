# Movie Night
# Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

# The given day will be one of:

# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# "Sunday"
# The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

# Return the total cost in the format "$D.CC" using these rules:

# Weekend (Friday - Sunday): $12.00 per ticket.
# Weekday (Monday - Thursday): $10.00 per ticket.
# Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
# Tuesdays: all tickets are $5.00 each.

def get_movie_night_cost(day, showtime, tickets):
    
    time = showtime[:-2]
    period = showtime[-2:]
    
    hour, minute = map(int, time.split(":"))
    
    if period == "pm" and hour != 12:
        hour += 12
    if period == "am" and hour == 12:
        hour = 0

    if day == "Tuesday":
        price_per_ticket = 5
    else:
        if day in ["Friday", "Saturday", "Sunday"]:
            price_per_ticket = 12
        else:
            price_per_ticket = 10
        
        if hour < 17:
            price_per_ticket -= 2

    total = price_per_ticket * tickets
    
    return f"${total:.2f}"

print(get_movie_night_cost("Saturday", "10:00pm", 1))
print(get_movie_night_cost("Sunday", "10:00am", 1))
print(get_movie_night_cost("Tuesday", "7:20pm", 2)) 