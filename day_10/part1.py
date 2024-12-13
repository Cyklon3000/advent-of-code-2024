from typing import List, Dict

class Point:
    def __init__(self, x: int, y: int, height: int):
        self.x: int = x
        self.y: int = y
        self.height: int = height
        
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
    
    def getReachableGoals(self) -> int:
        if self.height == 9:
            return set([self])
        
        goals = set()
        for direction in ["up", "down", "left", "right"]:
            point = self.getNeighbour(direction)
            if point == None: continue
            if point.height != self.height + 1: continue
            goals |= point.getReachableGoals()
        return goals
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y} -> {self.height})"

    def __hash__(self):
        return hash(f"{self.x} {self.y} {self.height}")

map_2d: List[List[Point]] = []
with open("day_10/input.txt", "r") as f:
    for y, row in enumerate(f.readlines()):
        mapRow: List[Point] = []
        for x, point in enumerate(row):
            if not point.isnumeric(): continue
            mapRow.append(Point(x, y, int(point)))
        map_2d.append(mapRow)

trailheads: List[Point] = []

for row in map_2d:
    for point in row:
        point.setNeighbours(map_2d)
        
        if point.height == 0:
            trailheads.append(point)

# print(trailheads)

total: int = 0
for trailhead in trailheads:
    total += len(trailhead.getReachableGoals())

print(total)