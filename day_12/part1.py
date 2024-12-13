from typing import List, Dict
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
    
    def getPerimeter(self, region:str) -> int:
        if self.region != region: return 1
        
        if self.checkedPerimeter: return 0
        
        perimeter = 0
        self.checkedPerimeter = True
        
        for direction in ["up", "down", "left", "right"]:
            perimeter += self.neighbours[direction].getPerimeter(region) if self.neighbours[direction] else 1
        
        return perimeter
    
    def getCost(self) -> int:
        return self.getArea(self.region) * self.getPerimeter(self.region)
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y} -> {self.region})"

    def __hash__(self):
        return hash(f"{self.x} {self.y} {self.region}")


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
        totalCost += point.getCost()

print(totalCost)