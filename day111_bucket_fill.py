def bucket_fill(grid, start, new_value):
    rows = len(grid)
    cols = len(grid[0])

    r, c = start
    old_value = grid[r][c]

    if old_value == new_value:
        return grid

    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if grid[x][y] != old_value:
            return

        grid[x][y] = new_value

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    dfs(r, c)
    return grid

print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))
print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
print(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"))
print(bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"))
print(bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"))