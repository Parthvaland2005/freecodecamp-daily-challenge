def format_coffee_order(order):

    menu = [
        ("cold brew", 4.50),
        ("oat latte", 5.00),
        ("cappuccino", 4.75),
        ("espresso", 3.00),
        ("vanilla syrup", 0.75),
        ("caramel drizzle", 0.60),
        ("extra shot", 0.50),
        ("oat milk", 0.75),
        ("cream", 0.75)
    ]

    order_lower = order.lower()

    items = []
    total = 0

    for item, price in menu:

        if item in order_lower:
            items.append(item)
            total += price

    return f"{' + '.join(items)}: ${total:.2f}"

print(format_coffee_order(
    "I'd like an oat latte with vanilla syrup and an extra shot please."
))

print(format_coffee_order(
    "Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk."
))

print(format_coffee_order(
    "Can I get a cold brew with some cream and an extra shot."
))

print(format_coffee_order(
    "Just an espresso please."
))

print(format_coffee_order(
    "I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle."
))