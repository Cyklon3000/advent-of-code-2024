from mymath import Vector2D
from typing import Set
from mytiming import timeit

obstacles:Set['Vector2D'] = set()
initialGuardPosition:Vector2D = None
initialGuardDirection:Vector2D = Vector2D.DOWN()
guardDirection:Vector2D = initialGuardDirection.copy() # the directions are fliped, due to the way the axies point

def rotateGuard():
    global guardDirection
    
    rotateLookup = {
        Vector2D.UP(): Vector2D.LEFT(),
        Vector2D.RIGHT(): Vector2D.UP(),
        Vector2D.DOWN(): Vector2D.RIGHT(),
        Vector2D.LEFT(): Vector2D.DOWN()
    }
    
    guardDirection = rotateLookup[guardDirection]

mapDimensions:Vector2D

with open("day_06/input.txt", "r") as file:
    fileArray = file.readlines()
    
    mapDimensions = Vector2D(len(fileArray[0])-1, len(fileArray))
    
    for y, row in enumerate(fileArray):
        for x, cell in enumerate(row):
            if cell == '#':
                obstaclePosition = Vector2D(x, y)
                obstacles.add(obstaclePosition)
            
            if cell == '^':
                initialGuardPosition = Vector2D(x, y)

print(f"Obstacles: {len(list(obstacles))}")
print(f"Map Dimensions: {mapDimensions}\n")

def isObstacleCausingCycle(customObstacle:Vector2D):
    global initialGuardPosition, mapDimensions, guardDirection
    
    guardPosition = initialGuardPosition.copy()
    guardDirection = initialGuardDirection
    
    seenGuardStates = set()
    while True:
        if (guardPosition.x >= mapDimensions.x) or (guardPosition.y >= mapDimensions.y) or (guardPosition.x < 0) or (guardPosition.y < 0):
            return False
        
        # print(f"Guard Position: {guardPosition}, Guard Direction: {guardDirection}")
        currentGuardState = hash((guardPosition, guardDirection))
        if currentGuardState in seenGuardStates:
            return True
        seenGuardStates.add(currentGuardState)

        inFrontOfGuard:Vector2D = guardPosition + guardDirection

        if (inFrontOfGuard in obstacles) or (inFrontOfGuard == customObstacle):
            rotateGuard()
            continue

        guardPosition += guardDirection

possibleObstaclePositions = 0

for y in range(mapDimensions.y):    
    for x in range(mapDimensions.x):        
        customObstacle = Vector2D(x, y)
        if customObstacle in obstacles:
            continue
        
        possibleObstaclePositions += int(isObstacleCausingCycle(customObstacle))
    
    if y > 0:
        print("\033[1A\x1b[2K", end="")
        print("\033[1A\x1b[2K", end="")
    print(f"Progress: {(100 * y / (mapDimensions.y-1)):.1f} %")
    print("▓" * int(25 * y / (mapDimensions.y-1)) + "░" * (25-int(25 * y / (mapDimensions.y-1))))

print("\nPossible Obstacle Positions:")
print(possibleObstaclePositions)