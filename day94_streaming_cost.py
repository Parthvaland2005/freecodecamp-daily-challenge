def get_streaming_bill(cart, tier):
    prices = {
        "HD": {"rent": 3.99, "buy": 12.99},
        "4K": {"rent": 5.99, "buy": 19.99}
    }

    discounts = {
        "none": 0.0,
        "basic": 0.10,
        "premium": 0.25
    }

    total = 0

    for item in cart:
        total += prices[item["format"]][item["type"]]

    total *= (1 - discounts[tier])

    return "${:.2f}".format(round(total + 1e-9, 2))

print(get_streaming_bill([
    {"format": "HD", "type": "rent"},
    {"format": "4K", "type": "rent"},
    {"format": "HD", "type": "buy"},
    {"format": "4K", "type": "buy"},
    {"format": "HD", "type": "buy"}
], "basic"))