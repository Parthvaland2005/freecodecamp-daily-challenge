def get_zone_violations(grid):
    restrictions = {
        "i": {"R", "I"},
        "A": {"C"},
        "R": {"i", "C"},
        "I": {"i"},
        "C": {"R", "A"},
        "": set()
    }

    rows = len(grid)
    cols = len(grid[0])
    violations = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            zone = grid[r][c]

            if zone == "":
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor = grid[nr][nc]

                    if neighbor in restrictions[zone]:
                        violations.append([r, c])
                        break

    return violations

print(get_zone_violations([["R", "C"], ["", "C"]]))
print(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]))
print(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]))
print(get_zone_violations([["R", "R", "C", "R", "R"],
                           ["R", "I", "C", "", "A"],
                           ["R", "R", "", "i", "A"]]))