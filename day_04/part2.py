grid = []

with open("day_04\input.txt", "r") as file:
    for line in file.readlines():
        grid.append(line.strip())

print(f"Width: {len(grid[0])}, Height: {len(grid)}")

def isXMas(x, y):
    if not (x + 2 < len(grid[0]) and y + 2 < len(grid)):
        return False
    lineDownRight:str = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2]
    lineDownLeft:str = grid[y][x+2] + grid[y+1][x+1] + grid[y+2][x]
    
    isLineDownRightValid = lineDownRight == "MAS" or lineDownRight == "SAM"
    isLineDownLeftValid = lineDownLeft == "MAS" or lineDownLeft == "SAM"
    
    return isLineDownRightValid and isLineDownLeftValid


totalSum = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        totalSum += int(isXMas(x, y))

print(totalSum)