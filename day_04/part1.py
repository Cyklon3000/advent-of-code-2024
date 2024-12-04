grid = []

with open("day_04\input.txt", "r") as file:
    for line in file.readlines():
        grid.append(line.strip())

print(f"Width: {len(grid[0])}, Height: {len(grid)}")
# If current is 'X' test all 4 possible directions (right, diag. down right, down, diag. down left)

def xRoutine(x, y):
    routineSum = 0
    if x + 3 < len(grid[0]): # right
        routineSum += 1 if grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S' else 0
    if x + 3 < len(grid[0]) and y + 3 < len(grid): # diag. down right
        routineSum += 1 if grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == 'S' else 0
    if y + 3 < len(grid): # down
        routineSum += 1 if grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S' else 0
    if x >= 3 and y + 3 < len(grid): # diag. down left
        routineSum += 1 if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S' else 0
    return routineSum

def sRoutine(x, y):
    routineSum = 0
    if x + 3 < len(grid[0]): # right
        routineSum += 1 if grid[y][x+1] == 'A' and grid[y][x+2] == 'M' and grid[y][x+3] == 'X' else 0
    if x + 3 < len(grid[0]) and y + 3 < len(grid): # diag. down right
        routineSum += 1 if grid[y+1][x+1] == 'A' and grid[y+2][x+2] == 'M' and grid[y+3][x+3] == 'X' else 0
    if y + 3 < len(grid): # down
        routineSum += 1 if grid[y+1][x] == 'A' and grid[y+2][x] == 'M' and grid[y+3][x] == 'X' else 0
    if x >= 3 and y + 3 < len(grid): # diag. down left
        routineSum += 1 if grid[y+1][x-1] == 'A' and grid[y+2][x-2] == 'M' and grid[y+3][x-3] == 'X' else 0
    return routineSum


totalSum = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'X':
            totalSum += xRoutine(x, y)
        
        if char == 'S':
            totalSum += sRoutine(x, y)

print(totalSum)