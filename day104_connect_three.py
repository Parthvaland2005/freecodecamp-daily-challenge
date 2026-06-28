def connect_three(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (0, 1),   
        (1, 0),   
        (1, 1),  
        (1, -1)   
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "":
                continue

            player = grid[r][c]

            for dr, dc in directions:
                coords = []

                for k in range(3):
                    nr = r + dr * k
                    nc = c + dc * k

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break

                    if grid[nr][nc] != player:
                        break

                    coords.append([nr, nc])

                if len(coords) == 3:
                    return [player] + coords

    return []

print(connect_three([
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "Y", "", ""],
    ["Y", "R", "R", "R"]
]))

print(connect_three([
    ["", "", "", ""],
    ["", "Y", "Y", ""],
    ["", "Y", "R", "R"],
    ["", "Y", "R", "R"]
]))