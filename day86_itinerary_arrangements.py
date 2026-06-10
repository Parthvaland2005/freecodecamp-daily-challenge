from math import factorial

def get_itinerary_count(stops):
    n = len(stops)
    return factorial(n) * (2 * n - 3)

print(get_itinerary_count(["library", "park"]))                                  # 2
print(get_itinerary_count(["library", "park", "arcade"]))                        # 18
print(get_itinerary_count(["library", "park", "arcade", "store"]))               # 120
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe"]))       # 840
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]))  # 55440