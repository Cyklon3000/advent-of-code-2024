values1 = []
values2 = []

with open("input.txt", "r") as input:
    for line in input:
        values1.append(int(line.split("   ")[0]))
        values2.append(int(line.split("   ")[1]))

sorted1 = sorted(values1)
sorted2 = sorted(values2)

differenceSum = 0
for i in range(len(sorted1)):
    differenceSum += abs(sorted1[i] - sorted2[i])

print(differenceSum)