def get_roommates(people):
    groups = {}

    for person in people:
        group = person["group"]
        name = person["name"]

        if group not in groups:
            groups[group] = []

        groups[group].append(name)

    rooms = []

    for names in groups.values():
        i = 0
        while i < len(names):
            if i + 1 < len(names):
                rooms.append(f"{names[i]} and {names[i + 1]}")
                i += 2
            else:
                rooms.append(names[i])
                i += 1

    return rooms

print(get_roommates([
    {"name": "Alice", "group": "A"},
    {"name": "Bob", "group": "B"},
    {"name": "Carol", "group": "A"}
]))

print(get_roommates([
    {"name": "John", "group": "C"},
    {"name": "Julia", "group": "C"},
    {"name": "Jim", "group": "C"}
]))