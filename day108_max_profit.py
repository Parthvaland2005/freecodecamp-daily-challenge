import math

def get_max_profit(prices, budget):
    max_profit = 0

    for buy_day in range(len(prices)):
        shares = int(budget // prices[buy_day])

        if shares == 0:
            continue

        for sell_day in range(buy_day + 1, len(prices)):
            profit = shares * (prices[sell_day] - prices[buy_day])

            if profit > max_profit:
                max_profit = profit

    max_profit = math.floor(max_profit * 100) / 100

    return f"{max_profit:.2f}"

print(get_max_profit([5, 6], 50))
print(get_max_profit([8, 2, 5, 10], 20))
print(get_max_profit([4, 5, 3, 6], 20))
print(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200))
print(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80))
print(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25))