from datetime import datetime, timedelta

def get_rental_cost(rental_time, return_time, tier):
    rental = datetime.strptime(rental_time, "%Y-%m-%dT%H:%M:%SZ")
    returned = datetime.strptime(return_time, "%Y-%m-%dT%H:%M:%SZ")

    pricing = {
        1: (4.99, 3.99),
        3: (3.99, 2.99),
        7: (2.99, 0.99)
    }

    base_cost, late_fee = pricing[tier]

    due_date = (rental + timedelta(days=tier)).replace(
        hour=12, minute=0, second=0, microsecond=0
    )

    late_days = 0
    if returned > due_date:
        late_days = (returned - due_date).days + 1

    total = base_cost + (late_days * late_fee)

    return f"${total:.2f}"

print(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1))
print(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1))
print(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3))
print(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3))
print(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7))
print(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7))