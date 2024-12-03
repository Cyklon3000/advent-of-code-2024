values1 = []
values2 = []

with open("input.txt", "r") as input:
    for line in input:
        values1.append(int(line.split("   ")[0]))
        values2.append(int(line.split("   ")[1]))

sorted1 = sorted(values1)
sorted2 = sorted(values2)

index1 = 0
index2 = 0

totalSum = 0
lastSum = 0

while index1 < len(sorted1):    
    value1 = sorted1[index1]
    if index1 > 0 and value1 == sorted1[index1 - 1]:
        totalSum += lastSum
        continue
    
    while index2 < len(sorted2) and value1 > sorted2[index2]:
        index2 += 1
    
    lastSum = 0
    while index2 < len(sorted2) and value1 == sorted2[index2]:
        index2 += 1
        lastSum += value1
    
    totalSum += lastSum
    index1 += 1

print(totalSum)