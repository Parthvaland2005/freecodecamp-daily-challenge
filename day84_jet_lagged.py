def get_jet_lag_hours(departure, arrival, flight_duration, direction):
    timezones = {
        "Los Angeles": -8,
        "New York": -5,
        "London": 0,
        "Istanbul": 3,
        "Dubai": 4,
        "Hong Kong": 8,
        "Tokyo": 9
    }

    timezone_difference = abs(timezones[arrival] - timezones[departure])

    multiplier = 1.5 if direction == "east" else 1.0

    jet_lag = timezone_difference + (flight_duration * 0.1 * multiplier)

    return round(jet_lag, 1)

print(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"))      # 6.5
print(get_jet_lag_hours("London", "New York", 8, "west"))          # 5.8
print(get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east"))          # 1.6
print(get_jet_lag_hours("Dubai", "London", 7, "west"))             # 4.7
print(get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west"))   # 17.5
print(get_jet_lag_hours("Tokyo", "Dubai", 9, "west"))              # 5.9
print(get_jet_lag_hours("New York", "Istanbul", 10, "east"))       # 9.5