from typing import List, Dict, Set
garden = []


class Point:
    def __init__(self, x: int, y: int, region: str):
        self.x: int = x
        self.y: int = y
        self.region: str = region
        self.checkedArea = False
        self.checkedPerimeter = False
        
        self.neighbours: Dict[str, 'Point'] = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }
        
    def setNeighbours(self, map_2d: List[List['Point']]) -> None:
        self.neighbours["up"] = map_2d[self.y-1][self.x] if self.y > 0 else None
        self.neighbours["down"] = map_2d[self.y+1][self.x] if self.y < len(map_2d) - 1 else None
        self.neighbours["left"] = map_2d[self.y][self.x-1] if self.x > 0 else None
        self.neighbours["right"] = map_2d[self.y][self.x+1] if self.x < len(map_2d[0]) - 1 else None
    
    def getNeighbour(self, direction: str) -> 'Point':
        return self.neighbours[direction]

    def getArea(self, region:str) -> int:
        if self.checkedArea: return 0
        if self.region != region: return 0
        
        area = 1
        self.checkedArea = True
        
        for direction in ["up", "down", "left", "right"]:
            area += self.neighbours[direction].getArea(region) if self.neighbours[direction] else 0
        
        return area
    
    def getRegionPoints(self, region:str, points:Set['Point']) -> List['Point']:
        if self.region != region: return
        if self in points: return
        
        self.checkedPerimeter = True
        
        points.add(self)
        
        for direction in ["up", "down", "left", "right"]:
            if not self.neighbours[direction]: continue
            self.neighbours[direction].getRegionPoints(region, points)
        
        return list(points)
    
    def getPerimeter(self) -> int:
        # "Scan" Region from top and right directions
        # For each scanPoint in scanLine that is different from lastScanline add 1
        
        if self.checkedPerimeter: return 0
        
        regionPoints = self.getRegionPoints(self.region, set())
        
        cache = {}
        def isInRegionPoints(x, y) -> bool:
            if hash((x, y)) in cache.keys():
                return cache[hash((x, y))]
            
            for point in regionPoints:
                if point.x == x and point.y == y:
                    cache[hash((x, y))] = True
                    return True
            cache[hash((x, y))] = False
            return False
        
        regionBounds = {
            "up" : min([point.y for point in regionPoints]),
            "down" : max([point.y for point in regionPoints]),
            "left" : min([point.x for point in regionPoints]),
            "right" : max([point.x for point in regionPoints])
        }
        regionBounds["height"] = regionBounds["down"] - regionBounds["up"] + 1
        regionBounds["width"] = regionBounds["right"] - regionBounds["left"] + 1

        perimeter = 0
        # Top-Down scan
        scanLine = [False for _ in range(regionBounds["left"], regionBounds["right"]+1)]
        for y in range(regionBounds["up"], regionBounds["down"]+2):
            scanDifference = []
            for x in range(regionBounds["width"]):
                scanDifference.append(isInRegionPoints(x+regionBounds["left"], y) and not scanLine[x]) # was not in scanLine or is no more in scanLine
            # Count strait edges
            last = False
            for current in scanDifference:
                perimeter += int(not last and current)
                last = current
            
            scanDifference = []
            for x in range(regionBounds["width"]):
                scanDifference.append(not isInRegionPoints(x+regionBounds["left"], y) and scanLine[x]) # was not in scanLine or is no more in scanLine
            # Count strait edges
            last = False
            for current in scanDifference:
                perimeter += int(not last and current)
                last = current
            
            scanLine = [isInRegionPoints(x, y) for x in range(regionBounds["left"], regionBounds["right"]+1)]
        
        # Left-Right scan
        scanLine = [False for _ in range(regionBounds["up"], regionBounds["down"]+1)]
        for x in range(regionBounds["left"], regionBounds["right"]+2):
            scanDifference = []
            for y in range(regionBounds["height"]):
                scanDifference.append(isInRegionPoints(x, y+regionBounds["up"]) and not scanLine[y]) # was not in scanLine or is no more in scanLine
            # Count strait edges
            last = False
            for current in scanDifference:
                perimeter += int(not last and current)
                last = current
            
            scanDifference = []
            for y in range(regionBounds["height"]):
                scanDifference.append(not isInRegionPoints(x, y+regionBounds["up"]) and scanLine[y]) # was not in scanLine or is no more in scanLine
            # Count strait edges
            last = False
            for current in scanDifference:
                perimeter += int(not last and current)
                last = current
            
            scanLine = [isInRegionPoints(x, y) for y in range(regionBounds["up"], regionBounds["down"]+1)]
        
        return perimeter
    
    def getCost(self) -> int:
        return self.getArea(self.region) * self.getPerimeter()
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y}) -> \"{self.region}\""

    def __hash__(self):
        return hash((self.x, self.y))


garden: List[List[Point]] = []
with open("day_12/input.txt", "r") as f:
    for y, row in enumerate(f.readlines()):
        gardenRow: List[Point] = []
        for x, point in enumerate(row):
            if not point.isalpha(): continue
            gardenRow.append(Point(x, y, point))
        garden.append(gardenRow)

for row in garden:
    for point in row:
        point.setNeighbours(garden)

totalCost = 0
for row in garden:
    for point in row:
        cost = point.getCost()
        totalCost += cost

print(f"totalCost: {totalCost}")