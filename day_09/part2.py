diskSpacing = []

with open("day_09/testinput.txt", "r") as file:
    for char in file.read():
        if char.strip() == "": continue
        if not char.isnumeric(): continue
        diskSpacing.append(int(char))

# print(storage)

data = []
gaps = []
isGap = True
currentId = 0
currentPosition = 0

class Block:
    def __init__(self, id:int, size:int, position:int):
        self.id = id
        self.size = size
        self.position = position
    
    def getCheckSum(self):
        checkSum = 0
        for index in range(self.position, self.position+self.size):
            checkSum += index*self.id
        return checkSum
    
    def __str__(self):
        if self.id == None:
            return f"Gap from {self.position} to {self.position+self.size-1}"
        return f"ID: {self.id} from {self.position} to {self.position+self.size-1}"

for size in diskSpacing:
    isGap = not isGap
    if isGap:
        gaps.append(Block(None, size, currentPosition))
    else:
        data.append(Block(currentId, size, currentPosition))
        currentId += 1
    currentPosition += size

for block in data[::-1]:
    for gap in gaps:
        if gap.position > block.position: continue
        if block.size > gap.size: continue
        
        # Move data to correct position
        block.position = gap.position
        
        # Adjust gap properties
        gap.position += block.size
        gap.size -= block.size
        break

checkSum = 0
for block in data:
    checkSum += block.getCheckSum()

print(f"Check sum : {checkSum}")