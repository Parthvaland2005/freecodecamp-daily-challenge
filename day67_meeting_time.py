def get_meeting_time(schedule):

    for hour in range(24):

        everyone_free = True

        for person in schedule:

            available = False

            for start, end in person:

                if start <= hour and hour + 1 <= end:
                    available = True
                    break

            if not available:
                everyone_free = False
                break

        if everyone_free:
            return hour

    return None

print(get_meeting_time([
    [[10, 12], [15, 16]],
    [[11, 14], [15, 16]]
]))

print(get_meeting_time([
    [[9, 10], [12, 15]],
    [[10, 11], [13, 14]],
    [[9, 11], [10, 14]]
]))

print(get_meeting_time([
    [[7, 8], [9, 11], [12, 14], [15, 16]],
    [[8, 11], [12, 13], [14, 15]]
]))

print(get_meeting_time([
    [[7, 8], [10, 12], [13, 15]],
    [[8, 11], [12, 13], [14, 15]],
    [[6, 7], [8, 9], [12, 13]]
]))

print(get_meeting_time([
    [[1, 3], [4, 6], [8, 10], [20, 23]],
    [[15, 16], [17, 18], [19, 22], [23, 24]],
    [[14, 16], [17, 23]],
    [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]
]))