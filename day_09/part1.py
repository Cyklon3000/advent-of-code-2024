diskSpacing = []

with open("day_09/input.txt", "r") as file:
    for char in file.read():
        if char.strip() == "": continue
        if not char.isnumeric(): continue
        diskSpacing.append(int(char))

# print(storage)

storage = []
isGap = True
currentId = 0

for size in diskSpacing:
    isGap = not isGap
    if isGap:
        storage.extend([None for _ in range(size)])
    else:
        storage.extend([currentId for _ in range(size)])
        currentId += 1

# print(storage[:1000])

nextEmptySpace = 0
nextDataSpace = len(storage) - 1

while True:
    while storage[nextEmptySpace] != None:
        nextEmptySpace += 1
    while storage[nextDataSpace] == None:
        nextDataSpace -= 1
    
    if nextDataSpace <= nextEmptySpace:
        break
    
    storage[nextEmptySpace] = storage[nextDataSpace]
    storage[nextDataSpace] = None

storage = storage[:nextDataSpace+1]
# print(storage)

checkSum = 0
for position, data in enumerate(storage):
    checkSum += position * data

print(f"Check sum : {checkSum}")