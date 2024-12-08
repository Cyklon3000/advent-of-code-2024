from mymath import Vector2D

antennas:dict = {}
mapDimensions:Vector2D

with open("day_08/input.txt", "r") as map:
    for y, row in enumerate(map.readlines()):
        for x, point in enumerate(row.strip()):
            mapDimensions = Vector2D(x+1, y+1)
            
            if point == '.':
                continue
            if point in antennas.keys():
                antennas[point].append(Vector2D(x, y))
            else:
                antennas[point] = [Vector2D(x, y)]

print(f"Map Dimensions: {mapDimensions}")
print([len(a) for a in antennas.values()], end="\n\n")

antinodes = set()

for frequency in antennas.keys():
    frequencyAntennas = antennas[frequency]
    
    # Loop over every antenna pair
    for a1, antenna1Pos in enumerate(frequencyAntennas):
        antinodes.add(antenna1Pos)
        for a2, antenna2Pos in enumerate(frequencyAntennas[a1+1:]):
            antennaDelta = antenna2Pos - antenna1Pos
            
            antinode1Pos = antenna1Pos - antennaDelta
            while (antinode1Pos >= Vector2D.ZERO()) and (antinode1Pos < mapDimensions):
                antinodes.add(antinode1Pos)
                antinode1Pos = antinode1Pos - antennaDelta
            
            antinode2Pos = antenna2Pos + antennaDelta
            while (antinode2Pos >= Vector2D.ZERO()) and (antinode2Pos < mapDimensions):
                antinodes.add(antinode2Pos)
                antinode2Pos = antinode2Pos + antennaDelta

print(f"Unique Antinodes: {len(antinodes)}")