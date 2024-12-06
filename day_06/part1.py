from mymath import Vector2D
from typing import Set
from time import sleep, time
from mytiming import timeit

obstacles:Set['Vector2D'] = set()
guardPosition:Vector2D = None
guardDirection:Vector2D = Vector2D.DOWN() # the directions are fliped, due to the way the axies point

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
                guardPosition = Vector2D(x, y)

# print(len(list(obstacles)))
# print(mapDimensions)

@timeit
def main():
    global guardPosition
    
    visitedPosition = set()

    while True:
        if (guardPosition.x >= mapDimensions.x) or (guardPosition.y >= mapDimensions.y) or (guardPosition.x < 0) or (guardPosition.y < 0):
            break
        
        visitedPosition.add(guardPosition)

        inFrontOfGuard:Vector2D = guardPosition + guardDirection

        if inFrontOfGuard in obstacles:
            rotateGuard()
            continue

        guardPosition += guardDirection

    print(len(visitedPosition))

main()